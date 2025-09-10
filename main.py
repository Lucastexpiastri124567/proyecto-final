import discord
import random
import os
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


infografias = [
    "inf1.png",
    "inf2.png",
    "inf3.png",
    "inf4.png",
    "inf5.png"
]


consejos = [
    " Usar bombillas LED y apagar luces/electrodomésticos que no estés usando.",
    " Evitar dejar cargadores o aparatos en stand-by (siguen consumiendo energía).",
    " Usa bicicleta o transporte público para disminuir emisiones.",
    " Mejorar el aislamiento de tu casa para necesitar menos calefacción o aire acondicionado.",
    " Ahorrar agua: duchas más cortas, cerrar el grifo al lavarse los dientes.",
    " Si se puede, optar por autos eléctricos o híbridos.",
    " Apostar por productos locales y de temporada (menos transporte = menos emisiones).",
    " Evitar el desperdicio de comida: planificar compras y aprovechar sobras.",
    " Reutilizar bolsas, botellas y envases.",
    " Reciclar papel, vidrio, plásticos y metales.",
    " Comprar menos cosas innecesarias (cada producto tiene una huella de carbono).",
    " Apostar por productos duraderos en lugar de desechables.",
]


preguntas_de_trivia = [
    {
        "pregunta": "¿Cuál es el principal gas responsable del efecto invernadero?",
        "opciones": ["A) Oxígeno", "B) Dióxido de carbono (CO₂)", "C) Nitrógeno", "D) Argón"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué energía renovable proviene del sol?",
        "opciones": ["A) Eólica", "B) Geotérmica", "C) Solar", "D) Hidroeléctrica"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Qué capa de la atmósfera nos protege de los rayos UV?",
        "opciones": ["A) Estratósfera", "B) Ozono", "C) Troposfera", "D) Ionosfera"],
        "respuesta": "B"
    }
]


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hola(ctx):
    await ctx.send(f"👋 ¡Hola!Soy Ambiental bot, un bot creado en Python para hablar sobre uno de los temas más importantes de nuestro tiempo: el cambio climático. 🌍.Proponer retos y trivias para aprender jugando.Darte consejos prácticos para reducir tu huella ecológica.Mostrar datos y curiosidades para que juntos entendamos mejor cómo cuidarlo.")


@bot.command()
async def problematicas(ctx):
    await ctx.send(f'Los problemas del cambio climático incluyen el aumento de la temperatura global, la intensificación de fenómenos meteorológicos extremos como sequías e inundaciones, el aumento del nivel del mar y el deshielo de los polos, la disminución de la biodiversidad, la inseguridad alimentaria, problemas de salud y la pobreza. Estos efectos impactan el medio ambiente, la salud humana y las sociedades, y están vinculados al aumento de los gases de efecto invernadero por la actividad humana. ¿Quieres algun video o infografia que lo explique?, si es asi usa el comando !infografia o !video')

@bot.command()
async def infografia(ctx):
    infografia = random.choice(infografias)
    ruta = os.path.join("images", infografia)
    with open(ruta, 'rb') as f:
        picture = discord.File(f)
        print(os.listdir("images"))
    await ctx.send(file=picture)

    
@bot.command()
async def consejo(ctx):
    consejo_elegido = random.choice(consejos)
    await ctx.send(f"consejo: {consejo_elegido}")

@bot.command()
async def video(ctx):
    videos = [
        "https://youtu.be/miEJI0XQiN4",
        "https://youtu.be/LKNVNXHYzS0",
        "https://youtu.be/JQHtjT-_c7U"
    ]
    video_elegido = random.choice(videos)
    await ctx.send("Mira este video sobre el cambio climático:")
    await ctx.send(video_elegido)


@bot.command(name="trivia")
async def trivia(ctx):
    # Elegir una pregunta aleatoria
    pregunta = random.choice(preguntas_de_trivia)
    opciones_texto = "\n".join(pregunta["opciones"])

    await ctx.send(f"🌍 **Trivia Climática** \n\n{pregunta['pregunta']}\n{opciones_texto}\n\n Responde con la letra (A, B, C o D).")

    # Esperar respuesta del usuario
    respuesta = await bot.wait_for("message")

    if respuesta.content.upper() == pregunta["respuesta"]:
        await ctx.send("✅ ¡Correcto! 🎉")
    else:
        await ctx.send(f"❌ Incorrecto. La respuesta correcta era **{pregunta['respuesta']}**.")



bot.run("")
