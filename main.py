from colorama import init, Fore, Style
import discord
from discord.ext import commands
import os

# Inicializar colorama
init()

# Función para colorear el texto con un degradado
def gradient_text(text, color=None):
    gradient = [
        Fore.BLUE, Fore.CYAN, Fore.WHITE
    ]
    if color is None:
        color = Fore.WHITE
    colored_text = ""
    for i, char in enumerate(text):
        colored_text += f"{color}{char}{Style.RESET_ALL}"
    return colored_text

# ASCII Art y encabezado
ascii_art = """
  ___|   \  |__ __|  _ \   _ \  |    
\___ \    \ |   |   |   | |   | |    
      | |\  |   |   |   | |   | |    
_____/ _| \_|  _|  \___/ \___/ _____|
                                     
"""

# Solicitar el token del bot
token = input("Por favor, ingrese el token del bot de Discord: ")

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot de Discord
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(gradient_text("developed by snt", Fore.BLUE))
    print(gradient_text(ascii_art))
    print(gradient_text("v1.0"))
    print(f"{gradient_text('Logged in as:', Fore.WHITE)} {gradient_text(bot.user.name, Fore.BLUE)}\n")
    print(gradient_text("Tokens loaded:", Fore.WHITE))
    print(gradient_text("Discord RPC:", Fore.WHITE))
    print(gradient_text("Proxyless:", Fore.WHITE) + "\n")

    # Centrar el "Page 1/4"
    print(" " * 15 + "Page 1/4\n")

    # Opciones dispuestas en tres columnas
    options = [
        "01. Server leaver", "02. Mass server leaver", "03. Chat spammer",
        "04. Mass chat spammer", "05. Thread creator", "06. Server joiner",
        "07. Mass typing", "08. Nickname changer", "09. Mass Hypesquad",
        "10. Group creator", "11. DM spammer", "12. Token checker"
    ]

    for i in range(0, 4):
        column_text = ""
        for j in range(i, len(options), 4):
            column_text += gradient_text(options[j].ljust(22))
        print(column_text)

    print("\nSelect a feature ~/>")

# Ejecutar el bot
bot.run(token)
