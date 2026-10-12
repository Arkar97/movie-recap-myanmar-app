# Movie Recap Myanmar App

Professional Windows application to convert English-narrated movie recaps into Myanmar-narrated videos using AI.

## Features

- **Automatic Speech Recognition** (Whisper - local, offline)
- **Smart Translation** (Gemini AI with story context)
- **Myanmar Voice Synthesis** (Microsoft Edge TTS)
- **Intelligent Video Sync** (Smart Sync technology)
- **Batch Processing** (multiple videos)
- **Preview & Edit** (blur, title, logo, zoom, flip)
- **Job Management** (save, resume, continue)
- **Professional Output** (16:9, 9:16, 1:1, Original ratios)

## Quick Start

1. **Clone Repository**
   ```bash
   git clone https://github.com/Arkar97/movie-recap-myanmar-app.git
   cd movie-recap-myanmar-app
   ```

2. **Install Requirements**
   ```bash
   INSTALL_REQUIREMENTS.bat
   ```

3. **Setup API Keys**
   ```bash
   copy .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

4. **Run Application**
   ```bash
   RUN.bat
   ```

## System Requirements

- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.12 (64-bit)
- **FFmpeg**: ffmpeg.exe + ffprobe.exe
- **RAM**: 4GB minimum (8GB+ recommended)
- **GPU**: Optional (NVIDIA CUDA 12 for faster processing)
- **API**: Google Gemini API key (free tier available)
- **Internet**: Required for Gemini and Edge TTS

## Project Structure

```
app/                    # Main application code
├── main.py             # Entry point
├── config_manager.py   # Configuration handler
├── job_manager.py      # Job management
├── models.py           # Data models
└── ui/
    └── controller.py   # UI controller

services/               # Core services
├── whisper_service.py  # Speech-to-text
├── ai_service.py       # Translation
├── tts_service.py      # Voice synthesis
└── ffmpeg_service.py   # Video processing

pipeline/               # Processing pipeline
├── planner_worker.py   # Translation planning
└── render_worker.py    # Video rendering

jobs/                   # Output directory
tests/                  # Unit tests
```

## Usage

### Basic Workflow

1. **Browse Video** - Select English-narrated video
2. **Configure** - Choose voice, speed, output format
3. **Preview** - Review translation and sync
4. **Export** - Generate final Myanmar-narrated video

### Advanced Features

- **Blur Boxes** - Hide sensitive content
- **Title Overlay** - Add Myanmar text
- **Logo Placement** - Add watermark
- **Smart Zoom** - Adjust video scale (1.0-1.25x)
- **Voice Control** - Adjust volume (50-300%)
- **Batch Mode** - Process entire folders

## Configuration

Edit `config.json` to customize:

```json
{
  "max_video_speed": 1.25,
  "translation_batch_max_items": 40,
  "atomic_target_duration": 4.2,
  "voice_name": "my-MM-ThihaNeural",
  "output_ratio": "16:9"
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Python not found | Run INSTALL_REQUIREMENTS.bat again |
| Gemini API error | Check .env file has valid GEMINI_API_KEY |
| FFmpeg not found | Run INSTALL_REQUIREMENTS.bat |
| Rate limit (429) | Add more API keys or wait |
| No audio output | Check internet connection |

## Development

### Run Tests
```bash
python -m pytest tests/
```

### Development Mode
```bash
python app/main.py
```

## API Keys

### Get Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy key to `.env` file

Free tier includes:
- 15 requests per minute
- 1,500 requests per day
- 500,000 input tokens
- 100,000 output tokens

## Notes

- Edge TTS is a Microsoft online service
- Gemini is a Google API
- Respect copyright of source videos
- Follow terms of service for all APIs

## License

MIT License - See LICENSE file

## Support

For issues, questions, or suggestions:
- Open an Issue on GitHub
- Check existing Issues and Discussions

---

**Convert English movie recaps to Myanmar narrated videos with AI-powered technology.**
