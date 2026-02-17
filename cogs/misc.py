from discord.ext import commands
from random import choice, randint
import discord
import asyncio
import json

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Bot = bot
        self.random_messages = json.load(open("data/random_messages.json", "r"))
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.bot.user.id == ctx.author.id:
            return
        if randint(0,512)==268:
            await ctx.channel.send(choice(self.random_messages))
        
    @commands.Cog.listener()
    async def on_ready(self):
        wiiu_games = json.load(open("data/wiiu_games.json", "r"))
        while True:
            await self.bot.change_presence(activity=discord.Game(choice(wiiu_games)))
            await asyncio.sleep(300)

    @commands.slash_command(description="Returns the bot's latency in milliseconds")
    async def ping(self, ctx):
        latency = self.bot.latency * 1000
        await ctx.respond(f"Pong! `{latency:.2f} ms` 🏓")

def setup(bot):
    bot.add_cog(Miscellaneous(bot))
