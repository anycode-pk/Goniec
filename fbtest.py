from Interfaces.FacebookInterface import FacebookInterface
import json

fb = FacebookInterface()

text = "Z ostatniej chwili: przed uzyciem nalezy skonsultowac sie z lekarzem lub farmaceuta gdyz kazdy lek niewlasciwie stosowany zagraza twojemu zyciu lub zdrowiu"

x = {
        "author": "Przykładowy user",
        "channel": "Przykładowy kanał",
        "content": text
        }

fb.send_privmessage(x, "6442179169244412")

fb.broadcast_message(x)
