from discord.ext import commands
import discord

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info")
    async def info(self, ctx):
        embed = discord.Embed(title="Información de SERVER CCHERO", color=0x3498db)
        embed.add_field(name="Descripción", value="Servidor para comunidades de la UNAM")
        embed.add_field(name="Comunidades", value="CCHs, ENPs y Facultades", inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Utilities(bot))
