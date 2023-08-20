import cv2
import os
import argparse

def extract_frames(video_path, output_directory, frame_interval, image_prefix):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    # Read frames from the video and save selected frames as images
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as an image only if it's the desired frame
        if frame_count % frame_interval == 0:
            image_path = os.path.join(output_directory, f"{image_prefix}_{frame_count:04d}.png")
            cv2.imwrite(image_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Extracted {frame_count // frame_interval} frames.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video")
    parser.add_argument("--video_path", required=True, help="Path to the input video file")
    parser.add_argument("--output_directory", required=True, help="Directory to save the output images")
    parser.add_argument("--frame_interval", type=int, required=True, help="Frame interval for extraction")
    parser.add_argument("--image_prefix", required=True, help="Prefix for the output image filenames")
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_directory, args.frame_interval, args.image_prefix)
