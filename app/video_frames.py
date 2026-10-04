"""Sample still frames from a patient video for the vision model."""

import os
import shutil
import subprocess
import tempfile


def _binary(name):
    found = shutil.which(name)
    if found:
        return found
    for candidate in (f"/opt/homebrew/bin/{name}", f"/usr/local/bin/{name}"):
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    raise ValueError(
        "Video review needs ffmpeg. Install it, then try the consultation again."
    )


def _duration_seconds(ffprobe, video_filepath):
    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            video_filepath,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return 0.0
    try:
        return max(0.0, float((result.stdout or "").strip() or 0))
    except ValueError:
        return 0.0


def extract_video_frame_jpegs(video_filepath, count=3):
    """Return JPEG bytes for a few frames spread across the clip."""
    video_filepath = str(video_filepath)
    if not os.path.isfile(video_filepath):
        raise ValueError("The uploaded video could not be read. Please try another file.")

    ffmpeg = _binary("ffmpeg")
    duration = _duration_seconds(_binary("ffprobe"), video_filepath)
    if duration <= 0.25:
        timestamps = [0.0]
    else:
        timestamps = [
            min(max(duration - 0.05, 0.0), duration * (index + 1) / (count + 1))
            for index in range(count)
        ]

    frames = []
    last_error = "ffmpeg could not read the video"
    with tempfile.TemporaryDirectory(prefix="skin-frames-") as tmp:
        for index, timestamp in enumerate(timestamps):
            out_path = os.path.join(tmp, f"frame_{index}.jpg")
            result = subprocess.run(
                [
                    ffmpeg,
                    "-y",
                    "-ss",
                    f"{timestamp:.3f}",
                    "-i",
                    video_filepath,
                    "-frames:v",
                    "1",
                    "-q:v",
                    "3",
                    out_path,
                ],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0 and os.path.isfile(out_path) and os.path.getsize(out_path) > 0:
                with open(out_path, "rb") as frame_file:
                    frames.append(frame_file.read())
                continue
            detail = (result.stderr or "").strip().splitlines()
            if detail:
                last_error = detail[-1]

    if not frames:
        raise ValueError(f"Could not read frames from the video. {last_error}")
    return frames
