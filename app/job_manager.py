from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class JobManager:
    def __init__(self, base_dir: str | Path):
        self.base_dir = Path(base_dir)
        self.jobs_dir = self.base_dir / "jobs"
        self.jobs_dir.mkdir(parents=True, exist_ok=True)

    def create_job(self, source_video_path: str):
        source_path = Path(source_video_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        job_name = source_path.stem
        job_dir = self.jobs_dir / f"{job_name}_{timestamp}"
        job_dir.mkdir(parents=True, exist_ok=True)

        metadata = {
            "job_name": job_name,
            "source_video": str(source_path),
            "created_at": datetime.now().isoformat(),
            "status": "queued",
            "output_dir": str(job_dir / "edge_tts_smart_sync"),
        }

        meta_path = job_dir / "job.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        return str(job_dir)

    def list_jobs(self):
        jobs = []
        if self.jobs_dir.exists():
            for job_dir in sorted(self.jobs_dir.iterdir(), key=lambda p: p.name):
                if job_dir.is_dir():
                    jobs.append(job_dir.name)
        return jobs
