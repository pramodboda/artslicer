# ArtSlicer

art-video-tool

I am essentially building a two-phase intelligent video refinement system specifically for art videos.

Main Project Name: ArtSlicer - A art video processing project

## Project 1 Name: Clip Cleaner

- 1. Accept a long art process video (up to 4K, any duration)
- 2. Then it identifies "beautiful" clips and filters out/ or removed "idle", "fully black", "erasingwith eraser" clips
- 3. Now video should be ready to download with Final Video and RemovedClips/ – idle/erasing with eraser/ unbeautiful clips
- 4. But now again User chooses clip duration (default 1 sec)
- 5. Tool splits video into equal-length clips
- 6. Final outputs:
- 7. CleanClips/ – ordered beautiful clips

🎯 Goal/ Key Pipeline:

1. Accept raw video (up to 4K, any duration)

2. Detect and remove:
   - Idle frames (no brush movement)
   - Fully black/blank screens
   - Erasing activity (eraser detection)
3. Now video should be ready to download and also RemovedClips/ – idle/erasing with eraser/ unbeautiful clips
   📁 Output: Folders of raw Clean Video and Removed Clips

```Edit
CleanVideo/
  ├── CleanVideo.mp4
RemovedClips/
  ├── idle_001.mp4
  ├── erase_001.mp4
```

4. But now again by one button click, now spliting remaining CleanVideo content into fixed-duration clips (default: 1 sec)
   📁 Output: Folders of raw CleanClips

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

🤖 What it does:

- Analyses each clip’s aesthetic quality
- Ranks and selects(but slips should be in order only) clips up to the target total time

📁 Output:

```Edit
BeautifulClips/   ← selected top clips up to time limit
UnselectedClips/ ← leftover clips (not selected)
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
