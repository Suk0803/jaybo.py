import discord
from discord.ext import commands
import random
import settings

logger = settings.logging.getLogger("bot")


class Slapper(commands.Converter):

    def __init__(self, *, use_nicknames) -> None:
        self.use_nicknames = use_nicknames

    async def convert(self, ctx, argument):
        someone = random.choice(ctx.guild.members)
        nickname = ctx.author
        if self.use_nicknames:
            nickname = ctx.author.nick
        return f"{nickname} slaps {someone} with {argument}"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")


@bot.command(
    aliases=['p'],
    help="This is help",
    description="This is description",
    brief=" This is brief",
    enabled=True,
    hidden=True
)
async def ping(ctx):
    """ Answers with pong """
    await ctx.send("pong")


@bot.command()
async def say(ctx, what="WHAT?"):
    await ctx.send(what)


@bot.command()
async def say2(ctx, *what):
    await ctx.send(" ".join(what))


@bot.command()
async def say3(ctx, what="WHAT?", why="WHY?"):
    await ctx.send(what + why)


@bot.command()
async def choices(ctx, *options):
    await ctx.send(random.choice(options))


@bot.command()
async def add(ctx, one: int, two: int):
    await ctx.send(one + two)


@bot.command()
async def joined(ctx, who: discord.Member):
    await ctx.send(who)


@bot.command()
async def joinedat(ctx, who: discord.Member):
    await ctx.send(who.joined_at)


@bot.command()
async def slap(ctx, reason: Slapper(use_nicknames=True)):
    await ctx.send(reason)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("handled error globally")
