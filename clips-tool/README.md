# clips-tool

A lightweight, personal-use backend for a clipping tool.

## Description

This tool accepts long-form audio or video, transcribes it using OpenAI Whisper (or FasterWhisper if available), finds moments worth clipping based on keyword spotting and optional silence detection, clips those moments using MoviePy or FFmpeg, and exports the clips to an `outputs/` folder.

## Folder Structure

```
clips-tool/
├── backend/
│   ├── main.py # Entrypoint
│   ├── transcribe.py # Whisper functions
│   ├── clipper.py # Clipping logic
│   ├── utils.py # Helper functions
│   ├── config.py # Keyword lists, clip lengths, etc.
├── examples/
├── outputs/
├── README.md
├── requirements.txt
```

## TODO

- [ ] Add argument parsing for input file, keywords, etc.
- [ ] Implement Faster Whisper transcription
- [ ] Add error handling
- [ ] Add language detection
- [ ] Add support for different models
- [ ] Implement keyword spotting logic
- [ ] Implement silence detection
- [ ] Implement logic to expand clips to include surrounding context
- [ ] Implement clipping logic using MoviePy or FFmpeg
- [ ] Add error handling
- [ ] Implement logic to move the clip to the output directory
- [ ] Add error handling
- [ ] Implement logging logic
- [ ] Add timestamps and clip names to the logs
