
# YasinTube Whisper Subtitle Studio

Bu projede OpenAI Whisper kullanarak videolardan otomatik altyazı (.srt, .vtt, .txt) üretip indirme imkanı sunan
minimal bir web uygulaması bulunmaktadır. Arayüz, YouTube'un karanlık temasını anımsatacak şekilde TailwindCSS ile tasarlanmıştır.  

## Kurulum

```bash
git clone <repo>  # veya zip'i çıkar
cd whisper_webapp
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Not:** Whisper çalışması için `ffmpeg` sisteminizde yüklü olmalıdır.  
Ubuntu/Debian: `sudo apt install ffmpeg`  
Windows: [FFmpeg indirme talimatları](https://ffmpeg.org/download.html).

## Çalıştırma

```bash
python backend/app.py
```

Ardından tarayıcınızdan `http://localhost:5000/index.html` dosyasını açın
(veya `python -m http.server` ile frontend klasörünü servis edin).

## Özelleştirme

- `backend/app.py` dosyasında `whisper.load_model("small")` satırını
  `base`, `medium`, `large` gibi modellerle değiştirebilirsiniz.
- `index.html` içinde Tailwind sınıflarıyla renk şema ve yerleşimi güncelleyebilirsiniz.

Sorularınız olursa Yasin bana sor! 😊
