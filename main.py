# Work with Python 3.6
import discord
from discord.ext import commands
import json

DEBUG = True
bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")


@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def welcome(ctx):
    await ctx.send('Welcome to the Hinman Discord Server!\n'
                + 'Please enter the following command in chat:\n\n'
                + '**$setup "Your Name" "Your Building"**\n\n'
                + 'This will get everything ready for you so you can enjoy the groupchat!')


# Where the bot actually runs
def main():
    token = ''
    with open('config.txt') as config_txt:
        data = json.load(config_txt)
        token = data['token'][0]

    bot.run(token)

main()
