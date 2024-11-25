from discord.ext import commands

class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='preguntar')
    async def ask_open_question(self, ctx, *, question):
        """Pregunta algo al canal."""
        await ctx.send(f"{ctx.author.name} pregunta: {question}")
        await ctx.send("Responde en el chat.")
        
    @commands.command(name='encuesta')
    async def poll(self, ctx, *, question):
        """Crea una encuesta simple."""
        poll_message = await ctx.send(f"Encuesta: {question}")
        await poll_message.add_reaction('👍')
        await poll_message.add_reaction('👎')

async def setup(bot):
    await bot.add_cog(Interaction(bot))
