Hangman

Juego del ahorcado diseñado para monitores con resolución 1080p. Las ventanas estarán situadas en 700x300 px y mantendrán unas proporciones por defecto de entre 400 y 600 px tanto de alto como de largo.

Los textos están normalizados, por lo que las tildes y los acentos no se tienen en cuenta.

Idiomas

El programa dispone de versiones en español, inglés y francés.

Para cambiar el idioma, hay que modificar el archivo:

Hangman/helpers/lang_config.py


Cambiar el valor de LANGUAGE_CODE según el idioma deseado:

LANGUAGE_CODE = "es"  # Español
LANGUAGE_CODE = "en"  # Inglés
LANGUAGE_CODE = "fr"  # Francés

Linux
1. Instalar Python

Instalar el intérprete de Python desde los repositorios de la distribución.

Arch Linux:

sudo pacman -S python


Ubuntu/Debian:

sudo apt install python3

2. Clonar el repositorio

Navegar hasta la carpeta principal del proyecto:

cd Hangman

3. Configurar el idioma

Modificar Hangman/helpers/lang_config.py y cambiar LANGUAGE_CODE a es, en o fr.

4. Crear el entorno virtual
python3 -m venv venv
source venv/bin/activate

5. Instalar las dependencias
pip install -r requirements.txt
pip install pyinstaller

6. Generar el ejecutable
pyinstaller --noconsole --add-data "assets:assets" main.py


En Linux se utiliza : para separar los recursos en --add-data.

El ejecutable se encontrará dentro de la carpeta dist/.

Windows
1. Instalar Python

Descargar e instalar Python desde el sitio web oficial o desde la Microsoft Store.

Durante la instalación, asegurarse de marcar la opción Add Python to PATH.

2. Clonar el repositorio

Abrir PowerShell o CMD y navegar hasta la carpeta principal:

cd Hangman

3. Configurar el idioma

Modificar Hangman/helpers/lang_config.py y cambiar LANGUAGE_CODE a es, en o fr.

4. Crear el entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

5. Instalar las dependencias
pip install -r requirements.txt
pip install pyinstaller

6. Generar el ejecutable
pyinstaller --noconsole --add-data "assets;assets" main.py


En Windows se utiliza ; para separar los recursos en --add-data.

El ejecutable main.exe se encontrará dentro de la carpeta dist/.
