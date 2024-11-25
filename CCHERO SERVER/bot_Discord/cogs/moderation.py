from discord.ext import commands
import discord
from discord.ui import Select, View

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="admin_menu")
    @commands.has_permissions(administrator=True)
    async def admin_menu(self, ctx):
        # Crear el menú desplegable para opciones de moderación
        select = Select(
            placeholder="Selecciona una opción de moderación...",
            options=[
                discord.SelectOption(label="Ban", value="ban", description="Banear a un usuario"),
                discord.SelectOption(label="Kick", value="kick", description="Expulsar a un usuario"),
                discord.SelectOption(label="Mute", value="mute", description="Silenciar a un usuario"),
                discord.SelectOption(label="Unmute", value="unmute", description="Quitar silencio"),
                discord.SelectOption(label="Warn", value="warn", description="Advertir a un usuario"),
            ]
        )

        # Crear una vista que contenga el menú
        view = View()
        view.add_item(select)

        # Enviar el mensaje con el menú desplegable
        await ctx.send("Menú de moderación:", view=view)

    @commands.Cog.listener()
    async def on_select_option(self, interaction: discord.Interaction):
        # Acciones que suceden dependiendo de la opción seleccionada en el menú
        if interaction.values[0] == "ban":
            await interaction.response.send_message("Banear: Escribe `!ban @usuario` para proceder.")
        elif interaction.values[0] == "kick":
            await interaction.response.send_message("Expulsar: Escribe `!kick @usuario`.")
        elif interaction.values[0] == "mute":
            await interaction.response.send_message("Silenciar: Escribe `!mute @usuario`.")
        elif interaction.values[0] == "unmute":
            await interaction.response.send_message("Quitar silencio: Escribe `!unmute @usuario`.")
        elif interaction.values[0] == "warn":
            await interaction.response.send_message("Advertir: Escribe `!warn @usuario`.")

def setup(bot):
    bot.add_cog(Moderation(bot))
