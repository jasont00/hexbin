# hexbin.py
import os

# import statements for discord
import discord
from discord.ext import commands
from dotenv import load_dotenv

# loads info from .env file: discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# sets intents for bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Use python hexbin.py in console to launch bot

@bot.command(name='bin_dec', help='Converts binary (unsigned) to decimal. Takes a string and outputs a string.')
async def bin_dec(ctx, binary):
    int_temp = 0
    i = 0
    sum = 0
    out = ""

    for bit in reversed(binary):
        int_temp = int(bit)
        sum += int_temp * pow(2, i)
        i += 1
    out = out + " " + str(sum)

    await ctx.send(out)

@bot.command(name='dec_bin', help='Converts unsigned decimal to binary. Take a string and outputs a string. Outputs the converted number'
                                  'without any leading 0s.')
async def dec_bin(ctx, decimal):
    i = int(decimal)
    output = []
    out = ""

    if int(decimal) <= 0:
        out = "0"
        await ctx.send(out)

    while i > 0:
        output.append(i % 2)
        i = i // 2

    output.reverse()

    for digit in output:
        out = out + str(digit)

    await ctx.send(out)

bot.run(TOKEN)
