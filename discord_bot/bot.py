import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN')

target_user_id = "@elfhelm__", "♛ 𝔒𝔴𝔫𝔢𝔯 ♛ 𝐄𝐥𝐟𝐡𝐞𝐥𝐦", "1227346574603063377"

intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hola" in message.content.lower():
        await message.channel.send(f'¡Hola!\n ¿cómo estás {message.author.name}?')
    elif "quién te creo" in message.content.lower():
        await message.channel.send('Buenas, me creo @_aztharot_ con el objetivo de tener un bot para compartir conocimiento, aprendizaje y sobre todo yo sirva para la seguridad IT y de servidores de Discord')
    elif "nuv" in message.content.lower():
        await message.channel.send(f'¡Hola NUV {message.author.name}')
    elif "aztharot" in message.content.lower():
        await message.channel.send('¡Hola!\n ¿cómo estás? puede ser que mi creador este ocupado mandale DM y en cuánto pueda él personalmente atendera tu mensaje. ¡Ten buen día!')
    elif "pobre" in message.content.lower():
        await message.channel.send("Ma pobre tu madre que anda mendigando en las esquinas de la villa de formas curiosas...")
    
    if any(mention.id == target_user_id for mention in message.mention):
        await message.channel.send(f'¡Hola {message.author.mention}!\n sabias que el Shampoo de Elfh te deja deslumbrante?')

    await bot.process_commands(message)

@bot.command(name="shutdown")
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Apagando el bot...")
    await bot.close()

initial_extensions = ['cogs.general', 'cogs.admin', 'cogs.cybersecurity', 'cogs.interaction', 'cogs.player', 'cogs.server_sec', 'cogs.learning']

async def load_extensions():
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f'Extensión {extension} cargada correctamente.')
        except Exception as e:
            print(f'No se pudo cargar la extensión {extension}.', e)

async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
