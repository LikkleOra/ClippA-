# clips-tool/backend/utils.py
import logging

def export_clip(clip_path, output_dir):
    """
    Exports the clip to the specified output directory.
    
    Args:
        clip_path (str): Path to the clip.
        output_dir (str): Path to the output directory.
    """
    # TODO: Implement logic to move the clip to the output directory
    # TODO: Add error handling
    pass

def log_results(clips):
    """
    Logs the results of the clipping process.
    
    Args:
        clips (list): A list of paths to the created clips.
    """
    # TODO: Implement logging logic
    # TODO: Add timestamps and clip names to the logs
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Created {len(clips)} clips.")
    for clip in clips:
        logging.info(f"Clip: {clip}")
