# clips-tool/backend/clipper.py
import moviepy.editor as mp
import os
import re

def find_clippable_moments(segments, keywords):
    """
    Finds moments in the transcript that are worth clipping based on keywords.
    
    Args:
        segments (list): A list of timestamped segments with text (e.g., start, end, text).
        keywords (list): A list of keywords to search for.
    
    Returns:
        list: A list of tuples containing the start and end timestamps of the clippable moments.
    """
    moments = []
    for segment in segments:
        for keyword in keywords:
            if re.search(r"\b" + keyword + r"\b", segment["text"], re.IGNORECASE):
                moments.append((segment["start"], segment["end"]))
                break # Only add the moment once per segment
    return moments

def clip_moments(video_file, moments):
    """
    Clips the video file based on the given moments.
    
    Args:
        video_file (str): Path to the video file.
        moments (list): A list of tuples containing the start and end timestamps of the clippable moments.
    
    Returns:
        list: A list of paths to the created clips.
    """
    clips = []
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True) # Ensure output directory exists
    
    for i, (start, end) in enumerate(moments):
        # Clip 15–60 sec chunks (5–10 sec before, 10–30 sec after)
        clip_start = max(0, start - 5)
        clip_end = min(mp.VideoFileClip(video_file).duration, end + 10)
        
        clip_path = os.path.join(output_dir, f"clip_{i}.mp4")
        
        try:
            video = mp.VideoFileClip(video_file).subclip(clip_start, clip_end)
            video.write_videofile(clip_path, codec="libx264", audio_codec="aac")
            clips.append(clip_path)
        except Exception as e:
            print(f"Error creating clip {i}: {e}")
    
    return clips
