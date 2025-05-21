# clips-tool/backend/main.py
import transcribe
import clipper
import utils
import config
import argparse

DEFAULT_KEYWORDS = ["you need to", "the secret is", "remember this", "top 3", "nobody talks about"]

def main():
    """
    Main function to orchestrate the transcription, clipping, and exporting process.
    """
    parser = argparse.ArgumentParser(description="Clip moments from a video based on keywords.")
    parser.add_argument("video_file", help="Path to the video file")
    parser.add_argument("-k", "--keywords", nargs="+", default=DEFAULT_KEYWORDS, help="List of keywords to search for")
    args = parser.parse_args()
    
    input_file = args.video_file
    keywords = args.keywords
    
    # Transcribe the audio
    transcript, segments = transcribe.transcribe_audio(input_file)
    
    # Find moments worth clipping
    moments = clipper.find_clippable_moments(segments, keywords)
    
    # Clip those moments
    clips = clipper.clip_moments(input_file, moments)
    
    # Print out the paths to saved clips
    print("Created clips:")
    for clip in clips:
        print(clip)

if __name__ == "__main__":
    main()
