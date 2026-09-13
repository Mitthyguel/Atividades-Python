import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} supremacy')

@bot.command()
async def hello(ctx):
    await ctx.send(f'oi, sou eu, o HFROG')

@bot.command()
async def ha(ctx, count_heh = 5):
    await ctx.send("HÁ" * count_heh)

@bot.command()
async def face_reveal(ctx):
    with open('images/image.png', 'rb' ) as imagem:
        imagem = discord.File(imagem)

        await ctx.send("quem fez isso?", file=imagem)

@bot.command()
async def kkk(ctx):
    await ctx.send("komorus, kamacurse, komorshin")

@bot.command()
async def fall(ctx):
    await ctx.send("Oh wee wee wee, is that Revan Plaza")


@bot.command()
async def komorus(ctx):
    await ctx.send("EU AMO O KOMORUS. Sinceramente, eu nem sei explicar o quanto, porque parece que qualquer palavra é pequena demais. Esse desgraçado simplesmente alugou um espaço permanente na minha cabeça e aparentemente decidiu nunca mais sair 😭. Eu posso estar fazendo qualquer coisa e do nada penso “KOMORUS”. Ele é simplesmente incrível, perfeito, maravilhoso, ABSURDO. Eu amo tudo sobre ele e provavelmente nunca vou enjoar de falar dele. KOMORUS EU TE AMO PRA CARALHO, VOCÊ É O MAIOR. 🗣️🔥")


@bot.command()
async def pack(ctx):
    pasta = "images"
    arquivos = ["gato.jpg", "trem.jpg", "mine.jpg", "jordan.jpg", "image.png", "clip.jpg", "banheiro.png"]
    imagem = random.choice(arquivos)
    await ctx.send(file=discord.File(f"images/{imagem}"))
bot.run("MTU0MTU4MTI5NjQyODM4ODQ0Mw.GaN3mv.GQp1qfwSn8He21eyWBz1znHDmC1UPb03X9uYeE")

 