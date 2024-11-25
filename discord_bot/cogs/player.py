import discord
from discord.ext import commands
import youtube_dl

ytdl_format_options = {
    'format': 'bestaudio/best',
    'noplaylist': 'True',
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def play(self, ctx, url):
        """Reproduce una canción desde YouTube."""
        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            return await ctx.send("Debes estar en un canal de voz para reproducir música.")

        voice_client = await voice_channel.connect()
        info = ytdl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
        voice_client.play(source)

async def setup(bot):
    await bot.add_cog(Music(bot))
