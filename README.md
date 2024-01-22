# youtubetranscribe
This Python script uses the OpenAI Whisper library and pytube to convert YouTube audio into text. (This won't work with Python 3.12 yet). I made it because no transcription service did a good job converting technical talks into text.

### Step 1
Install [OpenAI Whisper](https://github.com/openai/whisper) and [pytube](https://github.com/pytube/pytube)

### Step 2
Run from your terminal either:
`python generate-transcript-from-youtube.py <youtube_url>`
or
`python generate-transcript-from-youtube.py <youtube_url> <optional_folder_path>`
