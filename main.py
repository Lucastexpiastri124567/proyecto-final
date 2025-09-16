import discord
import random
import os
import requests
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

estadisticas = [
    "La temperatura promedio global ha aumentado aproximadamente 1.1 °C desde la era preindustrial.",
    "Más del 70% de los glaciares del mundo han perdido masa en las últimas décadas.",
    "Las emisiones de CO₂ de la industria y transporte han aumentado más del 50% desde 1990.",
    "Se estima que el nivel del mar ha subido unos 20 cm en el último siglo.",
    "Los incendios forestales han aumentado en frecuencia e intensidad debido al cambio climático.",
    " La producción agrícola puede disminuir hasta un 25% en algunas regiones si no se toman medidas.",
    "Más de 2.2 mil millones de personas viven en zonas con escasez de agua.",
    "El cambio climático afecta la biodiversidad, con miles de especies en peligro de extinción."
]

retos = [
    "Recicla correctamente al menos 5 materiales diferentes hoy.",
    "Planta una planta o cuida una en tu entorno.",
    "Reutiliza botellas o envases en lugar de tirarlos.",
    "Comparte un consejo con tu familia o amigos.",
    "Apaga el aire acondicionado o calefacción si no es necesario.",
    "Reduce el consumo de agua durante tu ducha y lavado de platos.",
    "Comparte contenido educativo sobre cambio climático en redes sociales.",
    "Recoge basura cuando veas en la calle o en parques.",
    "Comparte transporte escolar o laboral para reducir emisiones."

]

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
    },
     {
        "pregunta": "¿Qué fenómeno ocurre cuando los glaciares se derriten?",
        "opciones": ["A) Sequías", "B) Huracanes", "C) Aumento del nivel del mar", "D) Tornados"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es un efecto directo del calentamiento global?",
        "opciones": ["A) Reducción del CO₂", "B) Derretimiento de glaciares", "C) Menor nivel del mar", "D) Más hielo polar"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué práctica ayuda a reducir la emisión de gases contaminantes?",
        "opciones": ["A) Usar transporte público o bicicleta", "B) Encender más aparatos electrónicos", "C) Usar solo el auto", "D) Tirar basura al río"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Qué es la huella de carbono?",
        "opciones": ["A) Cantidad de basura producida", "B) Gases de efecto invernadero emitidos", "C) Agua consumida", "D) Energía solar utilizada"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Qué tipo de energía contribuye menos al cambio climático?",
        "opciones": ["A) Carbón", "B) Petróleo", "C) Solar", "D) Gas natural"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el acuerdo internacional para limitar el calentamiento global a menos de 2 °C?",
        "opciones": ["A) Protocolo de Kyoto", "B) Acuerdo de París", "C) Convenio de Montreal", "D) Tratado de Kioto"],
        "respuesta": "B"
    }
]


noticias = [
    "https://news.un.org/es/story/2025/09/1540404",
    "https://news.un.org/es/story/2025/09/1540399",
    "https://news.un.org/es/story/2025/09/1540393",
    "https://news.un.org/es/story/2025/08/1540366",
    "https://news.un.org/es/story/2025/08/1540362"
]


def get_weather(city: str)->str:
    base_url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(base_url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Intentalo mas tarde"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hola(ctx):
    await ctx.send(f"👋 ¡Hola!Soy Ambiental bot, un bot creado en Python para hablar sobre uno de los temas más importantes de nuestro tiempo: el cambio climático. 🌍.Proponer retos y trivias para aprender jugando.Darte consejos prácticos para reducir tu huella ecológica.Mostrar datos y curiosidades para que juntos entendamos mejor cómo cuidarlo. A continuacion escribe !comandos para poder ver todos los comandos de este bot y probarlos")


@bot.command()
async def comandos(ctx):
    await ctx.send("""
**Guía de comandos del bot**

**!info** → Explica qué es el cambio climático y sus principales causas.  
**!problematicas** → Muestra los problemas más graves que genera el cambio climático y sugiere recursos visuales.  
**!infografia** → Envía una infografía con información visual.  
**!verificar** → Analiza una imagen con IA e identifica el material presente.  
**!materiales_impacto** → Explica el daño ambiental de distintos materiales y cómo reducirlo.  
**!consejo** → Da un consejo práctico para cuidar el ambiente.  
**!reto** → Propone un reto ecológico para cumplir en el día.  
**!estadistica** → Muestra una estadística real sobre el cambio climático.  
**!video** → Comparte un video educativo sobre el cambio climático.  
**!trivia** → Lanza una pregunta de opción múltiple sobre temas ambientales.  
**!clima <ciudad>** → Devuelve el clima actual en la ciudad indicada.
**!noticia** → Enlace a una noticia reciente sobre cambio climático.
    """)

@bot.command()
async def info(ctx):
    await ctx.send(f"El cambio climático se refiere a las variaciones a largo plazo en los patrones del clima de la Tierra, principalmente causadas por la actividad humana. La quema de combustibles fósiles (como carbón, petróleo y gas) y la deforestación liberan grandes cantidades de gases de efecto invernadero, especialmente dióxido de carbono (CO₂), que atrapan el calor en la atmósfera.")
                   


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
async def verificar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
            await ctx.send(f"si quieres conocer el impacto de cada material que reconezco escribe el comando !materiales_impacto")
    else:
        await ctx.send("Olvidaste subir la imagen :(")    
    
   
@bot.command()
async def materiales_impacto(ctx):
        await ctx.send("Impacto de los materiales en el ambiente:")
        await ctx.send("Plásticos:\nPersisten siglos en el ambiente, contaminan océanos y liberan microplásticos.\nSugerencia: Reducir, reutilizar y reciclar; evitar plásticos de un solo uso.")
        await ctx.send("Metales:\nSu extracción genera contaminación y residuos tóxicos.\nSugerencia: Reciclar metales y elegir productos duraderos.")
        await ctx.send("Químicos:\nPueden contaminar agua y suelos, afectando ecosistemas y salud.\nSugerencia: Usar alternativas seguras y tratar residuos correctamente.")
        await ctx.send("Combustibles fósiles:\nAl quemarse liberan CO₂, agravando el cambio climático.\nSugerencia: Promover energías renovables y eficiencia energética.")
        await ctx.send("Telas (textiles):\nLa industria textil consume agua y químicos; las fibras sintéticas contaminan océanos.\nSugerencia: Comprar menos, elegir fibras sostenibles y reciclar ropa.")
        await ctx.send("Cartón:\nSu producción usa agua y energía, y si no se recicla ocupa espacio en vertederos.\nSugerencia: Reutilizar y reciclar cajas de cartón.")
        await ctx.send("Vidrio:\nSu fabricación consume energía, pero es 100% reciclable.\nSugerencia: Preferir envases retornables y reciclar vidrio.")
        await ctx.send("Papel:\nContribuye a la deforestación si no proviene de fuentes sostenibles.\nSugerencia: Reducir impresiones y usar papel reciclado.")


@bot.command()
async def consejo(ctx):
    consejo_elegido = random.choice(consejos)
    await ctx.send(f"consejo: {consejo_elegido}")


@bot.command()
async def reto(ctx):
    reto = random.choice(retos)
    await ctx.send(f"Tu reto del día: \n{reto}")


@bot.command()
async def estadistica(ctx):
    estadistica = random.choice(estadisticas)
    await ctx.send(f"Estadística: {estadistica}")


@bot.command()
async def video(ctx):
    videos = [
        "https://youtu.be/miEJI0XQiN4",
        "https://youtu.be/LKNVNXHYzS0",
        "https://youtu.be/JQHtjT-_c7U",
        "https://youtu.be/IXQ5_RX5Bgo",
        "https://youtu.be/5kBMHvvWlcs",
        "https://youtu.be/wNQ5wvGmnEk",
        "https://youtu.be/hoD3ghHhqq8",
        "https://youtu.be/gbuIWr-XHsc"
    ]
    video_elegido = random.choice(videos)
    await ctx.send("Mira este video sobre el cambio climático:")
    await ctx.send(video_elegido)



@bot.command()
async def noticia(ctx):
    noticia_elegida = random.choice(noticias)
    await ctx.send(f"Noticia sobre cambio climático:{noticia_elegida}")


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


@bot.command()
async def clima(ctx,*,city: str):
    weather_info = get_weather(city)
    await ctx.send(f"clima en {city}: {weather_info}")

bot.run("")