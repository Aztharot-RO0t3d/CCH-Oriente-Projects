import random
from discord.ext import commands

class Learning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.questions = {
            "¿Qué es una variable en programación?": ["Es un contenedor de datos", "Es un bucle", "Es un condicional"],
            "¿Qué es un for loop?": ["Un bucle", "Un tipo de función", "Un condicional"]
        }

    @commands.command(name='pregunta')
    async def ask_question(self, ctx):
        """Hace una pregunta aleatoria sobre programación."""
        question, answers = random.choice(list(self.questions.items()))
        await ctx.send(f"{question}\nOpciones: {', '.join(answers)}")

async def setup(bot):
    await bot.add_cog(Learning(bot))
