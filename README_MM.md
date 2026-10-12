# Movie Recap Myanmar - ရုပ်ရှင်သုံးခြင်း မြန်မာ

**English အသံဖြင့် ရုပ်ရှင်စုံ** ကို **မြန်မာအသံဖြင့် ပြန်ထုတ်ပေးတဲ့** Professional Windows Application

## 🎬 အဓိက လုပ်ဆောင်ချက်

### 7 အဆင့် Processing Pipeline

1. **📢 နားထောင် (Whisper)** — English အသံကို စာသားပြောင်းတယ် (word timestamps ပါ)
2. **✂️ အပိုင်းခွဲ** — စာကြောင်း/အပိုဒ်/အသံရပ်တွေ ခွဲပြီး sync units ဖန်တီးတယ်
3. **🧠 ဇာတ်လမ်း မှတ်ဉာဏ် (Gemini)** — ကြီးအလုပ်ကို ဖတ်သုံးပြီး အကျိုးအရာ မျှတစေတယ်
4. **🌐 ဘာသာပြန် (Gemini)** — တစ်ခါမှာ စာပိုင်း ၄၀ စီ မြန်မာ သဘာဝကျ အသံစာ ပြန်တယ်
5. **🔊 အသံထုတ် (Edge TTS)** — Microsoft Myanmar voice (Thiha/Nilar) ဖြင့် ထုတ်တယ်
6. **⏱️ Smart Sync** — မြန်မာအသံ အရှည်အတိုင်း ရုပ်ကို ညှိတယ် (max 1.25x)
7. **🎨 ဖြည့်စွက်** — Blur boxes, Title, Logo, Zoom, Flip ထည့်တယ်

## 💾 ထွက်ပွားမှု

- **Final Video**: `jobs/<name>_<timestamp>/edge_tts_smart_sync/final_edge_tts_smart_sync.mp4`
- **Transcript**: `whisper_transcript.txt`
- **Translations**: `timestamp_translations.json`
- **Sync Plan**: `smart_sync_plan.json`
- **Logs**: `run.log`

## 🖥️ System Requirements

| အရာ | လိုအပ်ချက် |
|---|---|
| OS | Windows 10/11 (64-bit) |
| Python | 3.12 (64-bit) |
| FFmpeg | ffmpeg.exe + ffprobe.exe |
| Gemini API | Google aistudio.google.com/apikey |
| Internet | Gemini + Edge TTS အတွက် လိုတယ် |
| GPU | ရွေးချယ်တွေပါ (NVIDIA CUDA 12) |

## 📦 Installation

### 1. Repository Download
```bash
git clone https://github.com/Arkar97/movie-recap-myanmar-app.git
cd movie-recap-myanmar-app
```

### 2. Python 3.12 Install
```bash
# python.org မှ Python 3.12 64-bit Download + Install
# "Add python.exe to PATH" အမှန်ခြစ်ပါ
```

### 3. Dependencies Install
```bash
INSTALL_REQUIREMENTS.bat
```

### 4. Setup .env
```bash
copy .env.example .env
# .env ကို ပွင့်ပြီး GEMINI_API_KEY ထည့်ပါ
```

## 🚀 Usage

```bash
RUN.bat
```

### Application Window

| ကဏ္ဍ | အလုပ်များ |
|---|---|
| **အပေါ်** | Source Video ရွေးပါ (Folder batch ကျေးဇူးပြု) |
| **ဘယ်ဘက်** | Voice (Thiha/Nilar) + Speed (-50% to +100%) |
| **အလယ်** | Preview + Timeline Scrubbing + Frame Refresh |
| **ညာဘက်** | Zoom, Flip, Voice Volume, Ratio, Blur, Title |
| **အောက်** | START / RESUME / STOP SAFELY / Open Job |

## ⚙️ Configuration (config.json)

```json
{
  "max_video_speed": 1.25,
  "translation_batch_max_items": 40,
  "atomic_target_duration": 4.2,
  "atomic_max_duration": 5.6,
  "translation_audit": true,
  "title_font_path": "C:\\Windows\\Fonts\\mmrtext.ttf",
  "overlay_blur_strength": 18
}
```

## 🛠️ Troubleshooting

| ပြဿနာ | ဖြေရှင်းချက် |
|---|---|
| `Python မတွေ့` | INSTALL_REQUIREMENTS.bat ပြန်run ပါ |
| `Gemini key မတွေ့` | .env အဆင်သည် စစ်ပါ |
| `FFmpeg မတွေ့` | INSTALL_REQUIREMENTS.bat ပြန်run ပါ |
| `429 quota exceeded` | Key ထပ်ထည့်သွင်းပါ သို့ နောက်နေ့ စမ်းပါ |
| `Edge TTS NoAudioReceived` | Internet connectivity စစ်ပါ |

## 📂 Project Structure

```
movie-recap-myanmar-app/
├── RUN.bat                          # Main Entry Point
├── INSTALL_REQUIREMENTS.bat         # Setup Script
├── .env.example                     # API Keys Template
├── config.json.example              # Configuration Template
├── requirements.txt                 # Python Dependencies
│
├── app/
│   ├── __init__.py
│   ├── main.py                      # Application Entry
│   ├── config_manager.py            # Config Handler
│   ├── job_manager.py               # Job Management
│   ├── models.py                    # Data Models
│   └── ui/
│       ├── __init__.py
│       └── controller.py            # Main UI Controller
│
├── services/
│   ├── __init__.py
│   ├── whisper_service.py           # Speech-to-Text
│   ├── ai_service.py                # Gemini Translation
│   ├── tts_service.py               # Edge TTS
│   └── ffmpeg_service.py            # Video Processing
│
├── pipeline/
│   ├── __init__.py
│   ├── planner_worker.py            # Transcript + Translation
│   └── render_worker.py             # TTS + Sync + Render
│
├── jobs/                            # Output Folder
│   └── <name>_<timestamp>/
│       ├── whisper_transcript.txt
│       ├── timestamp_translations.json
│       ├── smart_sync_plan.json
│       └── edge_tts_smart_sync/
│           └── final_edge_tts_smart_sync.mp4
│
└── tests/
    ├── __init__.py
    ├── test_config.py
    └── test_job.py
```

## 📝 Development Status

✅ Step 1: Project Structure Initialized  
⏳ Step 2: Core Services Implementation  
⏳ Step 3: UI Controller Development  
⏳ Step 4: Pipeline Integration  
⏳ Step 5: Preview & Export Features  
⏳ Step 6: Batch Processing  
⏳ Step 7: Production Ready Release  

## 📄 License

MIT License - See LICENSE for details

## 👨‍💻 Author

Created for Myanmar movie recap automation

---

**🎬 English ရုပ်ရှင်ကို မြန်မာအသံဖြင့် တစ်နည်းနည်းပြန်တည်ဆောက်ပါ။**
