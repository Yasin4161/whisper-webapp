
import os
import uuid
from flask import Flask, request, send_from_directory, jsonify
import whisper
from whisper.utils import write_srt, write_vtt

app = Flask(__name__)

# Load Whisper model once at startup
model = whisper.load_model("small")  # change size if needed

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/transcribe")
def transcribe():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    fmt = request.form.get("format", "srt")
    lang = request.form.get("language", "tr")

    # Save uploaded file
    filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
    path = os.path.join(UPLOAD_DIR, filename)
    file.save(path)

    # Run Whisper transcription
    result = model.transcribe(path, language=lang)

    # Choose output format
    base = os.path.splitext(filename)[0]
    output_path = os.path.join(OUTPUT_DIR, f"{base}.{fmt}")

    if fmt == "txt":
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
    else:
        segments = result["segments"]
        if fmt == "srt":
            write_srt(segments, output_path)
        elif fmt == "vtt":
            write_vtt(segments, output_path)
        else:
            return jsonify({"error": "Unsupported format"}), 400

    return jsonify({"url": f"/download/{os.path.basename(output_path)}"})

@app.get("/download/<path:filename>")
def download(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    # For production, use a WSGI server like Gunicorn
    app.run(debug=True, host="0.0.0.0", port=5000)
  
