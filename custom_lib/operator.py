import os
import subprocess
import whisper
from whisper.utils import write_vtt

m_choices=["tiny", "base", "small", "medium", "large"]
model = whisper.load_model(m_choices[3])

def video2mp3(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    return f"{filename}.{output_ext}"


def SpeechToText(input_video, opt_select, lang_select):
    if input_video.split('.')[1]=='mp3':
        audio_file = input_video
    else:
        audio_file = video2mp3(input_video)

    if len(lang_select)==0:
        options = dict(beam_size=5, best_of=5)
    else:
        options = dict(language=lang_select, beam_size=5, best_of=5)
    translate_options = dict(task=opt_select, **options)
    result = model.transcribe(audio_file, **translate_options)

    output_dir = 'content/'
    audio_path = audio_file.split(".")[0]
    # subtitle = output_dir+audio_path + ".vtt"
    subtitle = audio_path + ".vtt"

    with open(os.path.join(output_dir, audio_path + ".vtt"), "w") as vtt:
        write_vtt(result["segments"], file=vtt)

    return subtitle, result["text"]
