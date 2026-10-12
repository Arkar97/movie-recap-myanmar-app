from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class JobConfig:
    source_video: str
    job_name: str
    job_dir: str
    voice_name: str = "my-MM-ThihaNeural"
    voice_speed: str = "0%"
    output_ratio: str = "16:9"
    max_video_speed: float = 1.25
    translation_batch_max_items: int = 40


@dataclass
class TranslationResult:
    segment_id: int
    english_text: str
    myanmar_text: str
    start_time: float
    end_time: float
    confidence: float = 1.0


@dataclass
class SyncPlan:
    total_duration: float
    segments: list = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
