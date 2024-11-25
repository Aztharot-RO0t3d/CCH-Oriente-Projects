import os
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
