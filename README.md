# ArtSlicer

art-video-tool

I am essentially building a two-phase intelligent video refinement system specifically for art videos.

Main Project Name: ArtSlicer - A art video processing project

## Project 1 Name: Clip Cleaner

🎯 Goal/ Key Pipeline:

1. Accept raw video (up to 4K, any duration)

2. Detect and remove:
   - Idle frames (no brush movement)
   - Fully black/blank screens
   - Erasing activity (eraser detection)
3. Now video should be ready to download and also RemovedClips/ – idle/erasing with eraser/ unbeautiful clips
   📁 Output: Folders of raw Clean Video and Removed Clips

```Edit
Clip Cleaner/
├── input_art_video.mp4
├── output/
│   ├── CleanVideo/
│   │   ├── clip_000.mp4 (good)
│   │   ├── clip_001.mp4 (good)
│   │   ├── CleanVideo.mp4 (merged good clips)
│   └── RemovedClips/
│       ├── idle_001.mp4
│       ├── erase_002.mp4
```

4. But now again by one button click, now spliting remaining CleanVideo content into fixed-duration clips (default: 1 sec)

📁 Output: Folders of raw CleanClips – ordered beautiful clips

```Edit
CleanClips/
  ├── clip_001.mp4
  ├── clip_002.mp4
```

> Will do this steps UI

Optional: Auto-download/export ZIP for download

## Project 2 Name: BeaClip - Tool selects Beautiful Clips, Beauty Filter (Time-Based Smart Selector)

> Selects only beautiful clips from CleanClips/ folder and picks as many as needed to fit target total
> duration (like 30 sec or 1 hour).

🎯 Goal:

📥 Input: Folder of clean clips

⌛ User provides: Desired total length (e.g., 60 sec)

### 🤖 What It Does

1. Reads all clips in original order.

2. Calculates a beauty score for each clip:

3. Can use CLIP (OpenAI), NIMA (Google), or a custom model.

4. Selects the top-ranking clips (in order) until total time limit is reached.

5. Moves files into:

- ✅ BeautifulClips/ – top clips selected by score

- ❌ UnselectedClips/ – leftover clips not selected

📁 Output:

```Edit
BeautifulClips/ ← selected top clips up to time limit
  ├── clip_003.mp4
  ├── clip_005.mp4

UnselectedClips/ ← leftover clips (not selected)
  ├── clip_001.mp4
  ├── clip_002.mp4
  ├── clip_004.mp4
```

✅ NO merging into one video file. Just sorted folders with clips in order.

## ✅ Is This Doable for Free?

Absolutely. You can build both tools for free using:

| Part                              | Tool                     | Cost    |
| --------------------------------- | ------------------------ | ------- |
| Clip cutting                      | FFmpeg                   | ✅ Free |
| Frame analysis / motion detection | OpenCV                   | ✅ Free |
| Beauty scoring CLIP               | CLIP / NIMA / custom CNN | ✅ Free |
| Sorting & filtering               | Python                   | ✅ Free |
| Storage Local                     | HDD                      | ✅ Free |
| UI (optional) React               | Vite                     | ✅ Free |

## Run Frontend Project

- `cd client`
- `npm run dev`
