import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Expulsa a un miembro del servidor."""
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} ha sido expulsado por {reason}')

    @commands.command(name="ban")
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Banea a un miembro del servidor."""
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} ha sido baneado por {reason}')

    @commands.command(name="borrar_mensajes")
    async def borrar(self, ctx, amount: int = 50):
        """Comando para borrar mensajes."""
        await ctx.channel.purge(limit=amount)

async def setup(bot):
    await bot.add_cog(Admin(bot))
