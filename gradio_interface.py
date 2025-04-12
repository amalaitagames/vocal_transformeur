import time

import gradio as gr
import audioToText as aud

def audio_to_text(audio):
    start = time.time()
    text = aud.writeText(audio)
    end = time.time()
    total = end - start
    return [text, format(total, '.2f')]

def sauver_fichier(text_box, name_box):
    if text_box.__contains__('Ouvre le fichier'):
        aud.open_file_in_editor(text_box)
    else:
        if name_box is None:
            name_box = 'text'
        file_name = name_box + '.txt'
        path = 'downloads/text_exports/'
        file_path = path + file_name
        with open(file_path, 'w') as f:
            f.write(text_box)
            f.close()
        return file_path

def clear_inputs(text_box, name_box, file_box, file_upldr, time_box):
    text_box.clear()
    name_box.clear()
    file_box.clear()
    file_upldr.clear()
    time_box.clear()

def downlaod_file(f_explore):
    return f_explore

def afficher_nom_fichier(fichier):
    return fichier

def ecrire_dans_fichier_existant(file, text_to_append):
    with open(file, 'a') as f:
        f.write('\n' + text_to_append)
        f.close()
        return file

callback = gr.CSVLogger()
demo = gr.Blocks()

with demo:
    with gr.Row():
        with gr.Column():
            with gr.Group():
                audio_file = gr.Audio(sources=["microphone", "upload"],type="filepath")
                with gr.Row():
                    gr.Row()
                    rec_button = gr.Button("Convertir voix en texte", size='lg', min_width=80, variant='huggingface')
                    gr.Row()
            textBox = gr.Textbox(label="Texte trouvé", scale=3)
            timeBox = gr.Textbox(label="Temps de conversion", scale=3)
            nameBox = gr.Textbox(label="Nom du fichier", scale=3)
            file_downloader = gr.File(label="Téléchargement")
        with gr.Column():
            with gr.Row():
                file_uploader = gr.File(label="Upload")
            with gr.Row():
                buttonSubmit = gr.Button("Créer fichier txt", size='lg')
                buttonWrite = gr.Button("Écrire dans le fichier existant", size="lg")
                button_flag = gr.Button("Flag les datas", size='lg')
            clear_button = gr.ClearButton(value="Nouveau", variant="primary", components=[audio_file, textBox, nameBox, file_downloader, file_uploader, timeBox], size='lg')
            with gr.Column():
                timer = gr.Timer(1)
                file_explorer = gr.FileExplorer(root_dir="./downloads", file_count="single", every=timer)
                download_button = gr.DownloadButton("Télécharger un fichier", value=file_explorer.value)

    callback.setup([audio_file, textBox], "flagged_audio")

    buttonSubmit.click(fn=sauver_fichier, inputs=[textBox, nameBox], outputs=[file_downloader])
    buttonWrite.click(fn=ecrire_dans_fichier_existant, inputs=[file_uploader, textBox], outputs=file_downloader)
    button_flag.click(lambda *args: callback.flag(list(args)), [audio_file, textBox], None, preprocess=False)
    rec_button.click(audio_to_text, inputs=audio_file, outputs=[textBox, timeBox])
    download_button.click(fn=downlaod_file, inputs=file_explorer, outputs=download_button)

if __name__ == "__main__":
    demo.launch()
