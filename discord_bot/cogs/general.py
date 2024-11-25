import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Responde con 'Pong!' y el tiempo de latencia."""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! {latency}ms')

    @commands.command(name="hola")
    async def hello(self, ctx):
        """Responde con un saludo."""
        await ctx.send(f'Hola, {ctx.author.name}!')

    @commands.command(name="borrar", aliases=['clear', 'purge'])  
    @commands.has_permissions(manage_messages=True)
    async def borrar(self, ctx, amount: int = 50):
        """Borra una cantidad de mensajes recientes en el canal (máximo 14 días de antigüedad)."""
        try:
            deleted = await ctx.channel.purge(limit=amount, check=lambda msg: (discord.utils.utcnow() - msg.created_at).days < 14)
            await ctx.send(f'Se han borrado {len(deleted)} mensajes.', delete_after=5)
        except discord.Forbidden:
            await ctx.send("No tengo permisos para borrar mensajes.", delete_after=5)
        except discord.HTTPException:
            await ctx.send("Ocurrió un error al intentar borrar los mensajes.", delete_after=5)

async def setup(bot):
    await bot.add_cog(General(bot))
