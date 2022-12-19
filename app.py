#!/home/niranjan/anaconda3/envs/huggingface/bin/python
import gradio as gr
from custom_lib.loadcsvlist import loadArr
from custom_lib.operator import model, video2mp3, SpeechToText

if __name__=='__main__':
    # Initialize
    title = 'OpenAI Whisper implementation on Gradio Web UI'
    languages=loadArr('languages.csv')
    languages[1].sort()

    block = gr.Blocks()

    with block:
        with gr.Group():
            with gr.Box():
                with gr.Row().style():
                    inp_video = gr.Video(
                        label="Input Video",
                        # type="filepath",
                        mirror_webcam = False
                    )
                    with gr.Column(scale=0.25):
                        op_video = gr.File(
                            # type="file"
                        )
                        op_checks = gr.Radio(
                            ["transcribe","translate"],
                            value="translate",
                            label="Select option to translate or transcribe?")
                        op_options = gr.Dropdown(languages[1],
                            label="Select language in the audio (optional)")
                        btn = gr.Button("Generate Subtitle Video")
                op_text = gr.Textbox()

            btn.click(SpeechToText, inputs=[inp_video,op_checks, op_options], outputs=[op_video,op_text])

            gr.HTML('''
            <div class="footer">
                        <p>Testing wishper for movie subtitle</p>
            </div>
            ''')

    block.launch(debug = True)
