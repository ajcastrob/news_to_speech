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
        articulo = data.get("resumen", "")

    if not articulo:
        raise ValueError("El archivo Json no contiene texto")

    fragments = divide_text(articulo)
    print(f"Texto dividido en {len(fragments)} fragmentos")

    audios = []
    for i, fragments in enumerate(fragments, start=1):
        # Crear la carpeta audios y guardar ahí las salidas de audio.
        output_folder = "audio"
        os.makedirs(output_folder, exist_ok=True)
        filename = os.path.join(output_folder, f"{name}_{i}.mp3")

        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=fragments,
        ) as response:
            response.stream_to_file(filename)

        audios.append(filename)
        print(f"Fragmento {i} guardado como {filename}")

    return audios


def run_tts_on_articles(article_path: list):
    """Recorre una lista de artículos y los convierte de texto a audio"""

    print(f"Iniciando la conversión de {len(article_path)} artículos a audio.")

    for path in article_path:
        if not path:
            print("Se encontró una ruta vacía. Saltando")
            continue

        try:
            # Extraer un nombre base del archivo JSON para nombrar el audio.
            base_name = os.path.splitext(os.path.basename(path))[0]

            print(f"Convirtiendo audio de {path}")

            generate_audio = convert_text_to_speach(path, name=base_name)
            print(f"Audios generados para {base_name}: {generate_audio}")

        except Exception as e:
            print(f"Errro al convertir audio {e}")

    print("Conversión completada.")
