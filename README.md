
# Generates movie subtitle using Whisper OpenAi model and Gradio Web UI Implementation
This is an experimental repo to generate movie subtitle.
If video file is large, extract audio to mp3 format and upload to avoid unwanted web crashes.

##Hardware requirements
The package uses Whisper (medium) model as default, requirements are as per the model.

## Authors

- [Niranjan Shrestha](https://www.github.com/shniranjan)

  
## About Me
I'm a enthuast AI researcher and coder.

  
# Setting Up

Install ffmpeg and whisper as per the instructions at: https://github.com/openai/whisper

## Installation

Download Program

```bash
  git clone https://github.com/shniranjan/generate_subtitle_with_whisper.git
  cd generate_subtitle_with_whisper 
  pip install -r requirements.txt
```
    

Run Program

```bash
  python app.py

```

