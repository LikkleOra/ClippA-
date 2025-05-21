# clips-tool/backend/transcribe.py
import faster_whisper
import moviepy.editor as mp
import os

def transcribe_audio(video_file):
    """
    Transcribes the audio from a video file using faster-whisper.
    
    Args:
        video_file (str): Path to the video file.
    
    Returns:
        tuple: A tuple containing the full transcript (as plain text) and a list of timestamped segments with text (e.g., start, end, text).
    """
    # Extract audio if needed
    if video_file.endswith(".mp4") or video_file.endswith(".mov"):
        audio_file = "temp_audio.mp3"
        video = mp.VideoFileClip(video_file)
        video.audio.write_audiofile(audio_file)
    else:
        audio_file = video_file
    
    # Use faster-whisper to transcribe it
    model_size = "medium" # Placeholder
    model = faster_whisper.WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(audio_file, beam_size=5)
    transcript = ""
    segments_list = []
    for segment in segments:
        transcript += segment.text
        segments_list.append({"start": segment.start, "end": segment.end, "text": segment.text})
    
    # Clean up temporary audio file
    if video_file.endswith(".mp4") or video_file.endswith(".mov"):
        os.remove(audio_file)

    return transcript, segments_list
