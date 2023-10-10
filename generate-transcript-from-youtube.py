import whisper
from pytube import YouTube
import os


def generate_transcript(youtube_url, folder_path=None):
    if folder_path is None:
        # use current directory
        folder_path = os.path.dirname(os.path.realpath(__file__))

    print('Downloading audio from YouTube', youtube_url)
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(mime_type='audio/webm').first()
    file_path = audio_stream.download(output_path=folder_path)

    print('Generating transcript...')
    model = whisper.load_model("base.en")
    result = model.transcribe(file_path)

    transcript_file_name = f'{yt.title}.txt'
    with open(f'{folder_path}/{transcript_file_name}', 'w') as f:
        f.write(result["text"])

    print('Success: Audio file and transcript saved to', folder_path)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        youtube_url = sys.argv[1]
        try:
            generate_transcript(youtube_url)
        except Exception as e:
            print(e)
            exit(0)

    elif len(sys.argv) == 3:
        youtube_url = sys.argv[1]
        folder_path = sys.argv[2]
        try:
            generate_transcript(youtube_url, folder_path)
        except Exception as e:
            print(e)
            exit(0)
    else:
        print('usage: python generate-transcript-from-youtube.py <youtube_url> <optional_folder_path>')
        exit(0)