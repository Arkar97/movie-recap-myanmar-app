from __future__ import annotations

import os
import json
from pathlib import Path


class ConfigManager:
    def __init__(self, base_dir: str | Path):
        self.base_dir = Path(base_dir)
        self.config_path = self.base_dir / "config.json"
        self.default_config = {
            "ffmpeg_path": "",
            "ffprobe_path": "",
            "python_path": "",
            "max_video_speed": 1.25,
            "translation_batch_max_items": 40,
            "atomic_target_duration": 4.2,
            "atomic_max_duration": 5.6,
            "translation_audit": True,
            "title_font_path": r"C:\Windows\Fonts\mmrtext.ttf",
            "overlay_blur_strength": 18,
            "voice_name": "my-MM-ThihaNeural",
            "voice_speed": "0%",
            "gemini_model": "gemini-2.5-flash",
            "output_ratio": "16:9",
        }
        self.config = self._load()

    def _load(self):
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    merged = self.default_config.copy()
                    merged.update(data)
                    return merged
            except Exception:
                pass
        return self.default_config.copy()

    def save(self):
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()
