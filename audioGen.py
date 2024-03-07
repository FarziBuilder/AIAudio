from pytube import YouTube
from moviepy.editor import *
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.environ["OPENAI_API_KEY"]
)

def download_video(url, path):
    """
    Download a video from a YouTube URL and save it to the given path.
    """
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=path)
    return out_file
def convert_to_mp3(video_file, output_file):
    """
    Convert the downloaded video file to MP3 format.
    """
    video_clip = AudioFileClip(video_file)
    video_clip.write_audiofile(output_file)
    video_clip.close()
def audio_to_text(path_to_audio):
    #gives me the subtitles
    audio_file = open(path_to_audio, "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text",
    prompt="This is a video about quadcopter PID controller and PID tuning"
    )
    with open('transcription.txt', 'w') as text_file:
        text_file.write(transcription)
    print(transcription)
    


if __name__ == "__main__":
    # url = "https://www.youtube.com/watch?v=JBvnB0279-Q&list=PL0K4VDicBzsibZqfa42DVxC8CGCMB7G2G&index=6"
    # path = r"C:\Users\faraa\Desktop\MyWorks\WhisperTry1"
    # video_file = download_video(url, path)
    # output_file = video_file.replace(".mp4", ".mp3")  # Assuming the downloaded file is in mp4 format
    # convert_to_mp3(video_file, output_file)
    # print(f"Downloaded and converted video to MP3: {output_file}")
    audio_to_text(r"audio.mp3")