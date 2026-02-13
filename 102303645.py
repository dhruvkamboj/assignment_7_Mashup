import sys
import os
import yt_dlp
from pydub import AudioSegment
from moviepy.editor import VideoFileClip


def download_videos(singer, num_videos, download_dir):
    search_query = f"ytsearch{num_videos}:{singer} official song"

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])
    except Exception as e:
        print("Error downloading videos:", e)
        sys.exit(1)


def convert_videos_to_audio(video_dir, audio_dir):
    os.makedirs(audio_dir, exist_ok=True)
    audio_files = []

    for file in os.listdir(video_dir):
        if file.endswith((".mp4", ".mkv", ".webm", ".flv")):
            video_path = os.path.join(video_dir, file)
            audio_name = os.path.splitext(file)[0] + ".mp3"
            audio_path = os.path.join(audio_dir, audio_name)

            try:
                clip = VideoFileClip(video_path)
                clip.audio.write_audiofile(audio_path, logger=None)
                clip.close()
                audio_files.append(audio_path)
            except Exception as e:
                print(f"Error converting {file}:", e)

    return audio_files


def trim_audios(audio_files, duration_sec, trimmed_dir):
    os.makedirs(trimmed_dir, exist_ok=True)
    trimmed_files = []

    for file in audio_files:
        try:
            audio = AudioSegment.from_file(file)
            trimmed = audio[:duration_sec * 1000]

            out_path = os.path.join(trimmed_dir, os.path.basename(file))
            trimmed.export(out_path, format="mp3")
            trimmed_files.append(out_path)

        except Exception as e:
            print(f"Error trimming {file}:", e)

    return trimmed_files


def merge_audios(audio_files, output_file):
    try:
        combined = AudioSegment.empty()

        for file in audio_files:
            audio = AudioSegment.from_file(file)
            combined += audio

        combined.export(output_file, format="mp3")
        print(f"\nMashup created successfully: {output_file}")

    except Exception as e:
        print("Error merging audios:", e)


def main():
    if len(sys.argv) != 5:
        print("Usage:")
        print("python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    base_dir = "temp_mashup"
    video_dir = os.path.join(base_dir, "videos")
    audio_dir = os.path.join(base_dir, "audios")
    trimmed_dir = os.path.join(base_dir, "trimmed")

    os.makedirs(video_dir, exist_ok=True)

    print("Downloading videos...")
    download_videos(singer, num_videos, video_dir)

    print("Converting videos to audio...")
    audio_files = convert_videos_to_audio(video_dir, audio_dir)

    print("Trimming audio files...")
    trimmed_files = trim_audios(audio_files, duration, trimmed_dir)

    print("Merging audio files...")
    merge_audios(trimmed_files, output_file)

    print("Done.")


if __name__ == "__main__":
    main()
