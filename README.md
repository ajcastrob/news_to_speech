# News to Speech Pipeline

This README is available in English and Spanish.

---

## English

### Description
A Python project that fetches news articles from a given source, classifies them using the Gemini API, extracts their content, and converts them to audio files using OpenAI's Text-to-Speech API.

### Project Structure
- `import_news.py`: Fetches article URLs from a news website.
- `classify_news.py`: Classifies the news articles using Gemini and saves them to `noticias.json`.
- `news.py`: Downloads the full content of classified articles and saves them as individual JSON files in the `articulos/` directory.
- `text_to_speach.py`: Converts the text from a JSON article file into an MP3 audio file.
- `articulos/`: Directory where the extracted articles are stored.
- `requirements.txt`: Contains the project dependencies.

### Installation
1.  Clone the repository.
2.  Create a virtual environment (recommended).
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root of the project and add your API keys:
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

### Usage
The scripts are currently designed to be run sequentially.

1.  **Fetch and Classify News**:
    Run the `classify_news.py` script to fetch news from the default portal (`elnacional.com`) and classify them. This will create a `noticias.json` file.
    ```bash
    python classify_news.py
    ```
2.  **Extract Article Content**:
    Run the `news.py` script. This will take the first URL from `noticias.json`, download the article, and save it in the `articulos/` directory.
    ```bash
    python news.py
    ```
    *(Note: This script currently only processes the first article)*
3.  **Convert to Speech**:
    Run the `text_to_speach.py` script. You need to manually edit the `path` variable in this script to point to the desired article JSON file.
    ```bash
    python text_to_speach.py
    ```
    *(Note: The file to be converted is hardcoded in the script)*

---

## Español

### Descripción
Un proyecto en Python que obtiene artículos de noticias desde una fuente, los clasifica usando la API de Gemini, extrae su contenido y los convierte a archivos de audio usando la API de Text-to-Speech de OpenAI.

### Estructura del Proyecto
- `import_news.py`: Obtiene las URLs de los artículos de un sitio web de noticias.
- `classify_news.py`: Clasifica los artículos de noticias usando Gemini y los guarda en `noticias.json`.
- `news.py`: Descarga el contenido completo de los artículos clasificados y los guarda como archivos JSON individuales en el directorio `articulos/`.
- `text_to_speach.py`: Convierte el texto de un archivo JSON de un artículo a un archivo de audio MP3.
- `articulos/`: Directorio donde se guardan los artículos extraídos.
- `requirements.txt`: Contiene las dependencias del proyecto.

### Instalación
1.  Clona el repositorio.
2.  Crea un entorno virtual (recomendado).
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Crea un archivo `.env` en la raíz del proyecto y añade tus claves de API:
    ```
    GEMINI_API_KEY="TU_CLAVE_DE_API_DE_GEMINI"
    OPENAI_API_KEY="TU_CLAVE_DE_API_DE_OPENAI"
    ```

### Uso
Actualmente, los scripts están diseñados para ejecutarse en secuencia.

1.  **Obtener y Clasificar Noticias**:
    Ejecuta el script `classify_news.py` para obtener noticias del portal por defecto (`elnacional.com`) y clasificarlas. Esto creará un archivo `noticias.json`.
    ```bash
    python classify_news.py
    ```
2.  **Extraer Contenido del Artículo**:
    Ejecuta el script `news.py`. Este tomará la primera URL de `noticias.json`, descargará el artículo y lo guardará en el directorio `articulos/`.
    ```bash
    python news.py
    ```
    *(Nota: Actualmente, este script solo procesa el primer artículo)*
3.  **Convertir a Audio**:
    Ejecuta el script `text_to_speach.py`. Necesitas editar manualmente la variable `path` en este script para que apunte al archivo JSON del artículo deseado.
    ```bash
    python text_to_speach.py
    ```
    *(Nota: El archivo a convertir está hardcodeado en el script)*
