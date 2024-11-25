from discord.ext import commands
import discord

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Aquí podrías implementar la lógica antiraid
        await member.send("¡Bienvenido a SERVER CCHERO! Respeta las reglas y disfruta.")

    @commands.command(name="set_antiraid")
    @commands.has_permissions(administrator=True)
    async def set_antiraid(self, ctx, threshold: int):
        # Configura el umbral para activar el antiraid
        await ctx.send(f"Antiraid configurado con umbral: {threshold}")

def setup(bot):
    bot.add_cog(Security(bot))
