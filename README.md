# News to Speech Pipeline

This README is available in English and Spanish.

---

## English

### Description
A Python project that fetches news articles from a given source, classifies them using the Gemini API, extracts their content, and converts them to audio files using OpenAI's Text-to-Speech API.

### Project Structure
- `main.py`: The main entry point to run the entire news processing pipeline.
- `import_news.py`: Fetches article URLs from a news website.
- `classify_news.py`: A module to classify news articles using the Gemini API.
- `news.py`: A module to download and parse the full content of articles.
- `text_to_speach.py`: A module to convert article text into MP3 audio files.
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
The project is now orchestrated by `main.py`, which automates the entire pipeline.

1.  **Run the main script**:
    ```bash
    python main.py
    ```
2.  **Enter the news portal URL**:
    The script will prompt you to enter the URL of the news portal you want to process (e.g., `https://www.example-news.com`).
3.  **Processing**:
    The script will then automatically:
    *   Fetch and classify the articles.
    *   Extract the content of each article and save it in the `articulos/` directory.
    *   Convert the text of each article into an MP3 audio file.

*(Note: By default, the script is configured to process 2 articles. This can be changed in the `main.py` file.)*

---

## Español

### Descripción
Un proyecto en Python que obtiene artículos de noticias desde una fuente, los clasifica usando la API de Gemini, extrae su contenido y los convierte a archivos de audio usando la API de Text-to-Speech de OpenAI.

### Estructura del Proyecto
- `main.py`: El punto de entrada principal para ejecutar todo el proceso de noticias.
- `import_news.py`: Obtiene las URLs de los artículos de un sitio web de noticias.
- `classify_news.py`: Un módulo para clasificar artículos de noticias usando la API de Gemini.
- `news.py`: Un módulo para descargar y analizar el contenido completo de los artículos.
- `text_to_speach.py`: Un módulo para convertir el texto de los artículos a archivos de audio MP3.
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
El proyecto ahora está orquestado por `main.py`, que automatiza todo el proceso.

1.  **Ejecuta el script principal**:
    ```bash
    python main.py
    ```
2.  **Ingresa la URL del portal de noticias**:
    El script te pedirá que ingreses la URL del portal de noticias que quieres procesar (por ejemplo, `https://www.ejemplo-noticias.com`).
3.  **Procesamiento**:
    El script se encargará automáticamente de:
    *   Obtener y clasificar los artículos.
    *   Extraer el contenido de cada artículo y guardarlo en el directorio `articulos/`.
    *   Convertir el texto de cada artículo a un archivo de audio MP3.

*(Nota: Por defecto, el script está configurado para procesar 2 artículos. Esto se puede cambiar en el archivo `main.py`.)*
