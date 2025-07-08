# clip_cleaner.py       # Your existing logic (modularized)

# Clip Cleaner - Step 1–3 Only (No TempSplit)
# Prerequisites: ffmpeg, opencv-python

import os
import shutil
import subprocess
from pathlib import Path
import cv2
import tempfile

# === Configuration ===
INPUT_VIDEO = "input_art_video.mp4"  # Replace with your raw video
CLIP_DURATION = 1  # in seconds

# === Output Folders ===
WORK_DIR = Path("output")
CLEAN_VIDEO_DIR = WORK_DIR / "CleanVideo"
REMOVED_DIR = WORK_DIR / "RemovedClips"

for folder in [CLEAN_VIDEO_DIR, REMOVED_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# === Helper: Detect unwanted clips ===
def analyze_clip(clip_path):
    cap = cv2.VideoCapture(str(clip_path))
    success, prev_frame = cap.read()
    if not success:
        cap.release()
        return "corrupt"

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    frame_diffs = []
    total_brightness = 0
    white_pixel_ratio = 0
    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(gray, prev_gray).mean()
        frame_diffs.append(diff)

        white_pixels = (gray > 240).sum()
        white_pixel_ratio += white_pixels / gray.size

        total_brightness += gray.mean()
        prev_gray = gray
        frame_count += 1

    cap.release()

    if frame_count == 0:
        return "corrupt"

    avg_motion = sum(frame_diffs) / len(frame_diffs) if frame_diffs else 0
    avg_brightness = total_brightness / frame_count
    avg_white_ratio = white_pixel_ratio / frame_count

    if avg_brightness < 10:
        return "black"
    elif avg_motion < 2:
        return "idle"
    elif avg_white_ratio > 0.6:
        return "erase"
    else:
        return "keep"

# === Step 1–3 Combined: Stream and Filter Clips ===
def process_video():
    print("🔄 Processing raw video...")
    temp_dir = tempfile.TemporaryDirectory()
    temp_path = Path(temp_dir.name)

    # Step 1: Split to temp folder
    split_command = [
        "ffmpeg", "-i", INPUT_VIDEO,
        "-c", "copy", "-map", "0",
        "-f", "segment", "-segment_time", str(CLIP_DURATION),
        str(temp_path / "clip_%03d.mp4")
    ]
    subprocess.run(split_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Step 2: Analyze each clip
    good_clips = []
    for i, clip in enumerate(sorted(temp_path.glob("clip_*.mp4"))):
        result = analyze_clip(clip)
        if result == "keep":
            new_path = CLEAN_VIDEO_DIR / clip.name
            shutil.move(str(clip), new_path)
            good_clips.append(new_path)
        else:
            name = f"{result}_{i:03d}.mp4"
            shutil.move(str(clip), REMOVED_DIR / name)

    # Step 3: Merge all good clips
    if good_clips:
        list_file = CLEAN_VIDEO_DIR / "inputs.txt"
        with open(list_file, "w") as f:
            for clip in good_clips:
                f.write(f"file '{clip}'\n")

        subprocess.run([
            "ffmpeg", "-f", "concat", "-safe", "0",
            "-i", str(list_file), "-c", "copy",
            str(CLEAN_VIDEO_DIR / "CleanVideo.mp4")
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(list_file)

    print("✅ Cleaned video and removed clips saved.")
    temp_dir.cleanup()

# === Run ===
if __name__ == "__main__":
    process_video()
