import discord
from discord.ext import commands

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if any(word in message.content.lower() for word in ['spam', 'malicious']):
            await message.delete()
            await message.channel.send(f"Mensaje de {message.author.name} eliminado por contener palabras inapropiadas.")
        
    @commands.command(name='auto_ban')
    @commands.has_permissions(ban_members=True)
    async def ban_user(self, ctx, member: discord.Member, *, reason=None):
        """Banea a un usuario."""
        await member.ban(reason=reason)
        await ctx.send(f'{member.name} ha sido baneado.')

async def setup(bot):
    await bot.add_cog(Security(bot))
