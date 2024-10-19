
from gtts import gTTS
import os
text_to_convert = input("Entrez le texte que vous souhaitez convertir en fichier audio : ")
language = 'fr'
tts = gTTS(text=text_to_convert, lang=language, slow=False)
audio_file = "output.mp3"
tts.save(audio_file)
os.system(f"start {audio_file}")

print(f"Le fichier audio a été créé avec succès : {audio_file}")
