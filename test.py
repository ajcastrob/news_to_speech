from gtts import gTTS
import json

path = "./articulos/Última_hora_de_la_visita_de_Trump_a_Asia_acuerdo_d_27e63d51.json"

with open(path, "r") as file:
    data = json.load(file)
    articulo = data["texto"]


tts = gTTS(articulo.strip(), lang="es", tld="us", slow=False)
tts.save("Noticia.mp3")
