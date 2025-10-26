from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import textwrap

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def divide_text(text, max_chars=7500):
    """Divide un texto largo en varios fragmentos"""
    return textwrap.wrap(text, max_chars)


def convert_text_to_speach(json_path, name: str):
    """Lee un archivo JSON y convierte su texto en múltiples audios si es necesario"""

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        articulo = data.get("texto", "")

    if not articulo:
        raise ValueError("El archivo Json no contiene texto")

    fragments = divide_text(articulo)
    print(f"Texto dividido en {len(fragments)} fragmentos")

    audios = []
    for i, fragments in enumerate(fragments, start=1):
        filename = f"{name}_{i}.mp3"

        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=fragments,
        ) as response:
            response.stream_to_file(filename)

        audios.append(filename)
        print(f"Fragmento {i} guardado como {filename}")

    return audios


path = "./articulos/Lula_se_ofrece_como_mediador_para_aliviar_tensione_b88f5084.json"

try:
    archivo_audio = convert_text_to_speach(path, "el_nacional")
    print(f"Audios generados")
except Exception as e:
    print(f"Error: {e}")
