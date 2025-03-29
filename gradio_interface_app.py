import gradio as gr
import audioToText as aud


def voice_to_text(audio):
    text_rec = aud.writeText(audio)
    return text_rec


audio_input = gr.Audio(
    sources=["microphone"],
    type="filepath",
)

demo = gr.Interface(fn=voice_to_text,
                    inputs=audio_input,
                    outputs=gr.Textbox(),
                    title="Voix vers Texte",
                    description="Cliquez sur le bouton rec pour commencer à enregistrer puis envoyez l'audio afin qu'il soit retranscrit")

if __name__ == "__main__":
    demo.launch()