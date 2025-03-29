import gradio as gr
import audioToText as aud

def audio_to_text(audio, progress=gr.Progress()):
    progress(0, desc="Starting process...")
    text = aud.writeText(audio)
    return text

demo = gr.Blocks()

with demo:
    with gr.Group():
        audio_file = gr.Audio(sources=["microphone", "upload"],type="filepath")
        with gr.Row():
            gr.Row(scale=2)
            rec_button = gr.Button("Convert Voice to Text", size='lg', min_width=80, variant='huggingface')
            gr.Row(scale=2)
    text = gr.Textbox(scale=3, submit_btn="Valider le texte", stop_btn="Texte Faux")

    event = text.stop_btn


    rec_button.click(audio_to_text, inputs=audio_file, outputs=text)

if __name__ == "__main__":
    demo.launch()
