import logging
import discord
from discord.ext import commands
import config

# Configurar el registro (logging)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents)

# Configuración de Embed para el servidor SERVER CCHERO
embed_color = 0x3498db  # Color para los mensajes embed

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} está en línea.")
    await bot.change_presence(activity=discord.Game(name="SERVER CCHERO"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hola" in message.content.lower():
        await message.channel.send(f'¡Hola!\n ¿cómo estás {message.author.name}?')
    elif "ip" in message.content.lower():
        await message.channel.send('La IP del servidor es: 207.231.104.210 \n el Puerto del servidor es: 2578')
    elif "pag" in message.content.lower():
        await message.channel.send(f'¡Hola {message.author.name}, la página web oficial del servidor es: CCHOTE.svhost.net')

    await bot.process_commands(message)

# Cargar módulos y registrar los logs
initial_extensions = ["cogs.moderation", "cogs.security", "cogs.utilities"]
for extension in initial_extensions:
    try:
        bot.load_extension(extension)
        logger.info(f"Extensión {extension} cargada correctamente.")
    except Exception as e:
        logger.error(f"Error al cargar la extensión {extension}: {e}")

bot.run(config.BOT_TOKEN)
