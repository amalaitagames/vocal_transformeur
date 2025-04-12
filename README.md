# PROJET IA GÉNÉRATIVE 

## Programme de transcription d'audio en texte

Ce programme permet de retranscrire un fichier audio ou un enregistrement audio live en format texte.
Par la suite il est possible d'enregistrer la transcription en dans un fichier .txt et à la suite d'un fichier .txt déjà existant.
Enfin ce programme permet également sous Linux avec un bureau Gnome et le gestionnaire de package Flatpak, de lancer des applications en commande vocale.

## INSTALLATION
Pour installer ce programme il faudra installer les librairies python suviantes :
- Gradio,
- Whisper.
Vous pouvez les installer via la commande suivante : 
- pip install gradio
- pip install git+https://github.com/openai/whisper.git 

Il vous faudra ensuite pour le fonctionnement de l'application installer la ligne de commande ffmpeg:
- Linux : sudo apt update && sudo apt install ffmpeg
- Windows : choco install ffmpeg
- Mac : brew install ffmpeg

Plus d'information supplémentaires sur le github de Whisper : https://github.com/openai/whisper
