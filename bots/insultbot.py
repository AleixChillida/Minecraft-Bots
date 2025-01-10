import mcpi.minecraft as minecraft
import random
import time

mc = minecraft.Minecraft.create()

class InsultBot:

    INSULTS = [
        "Eres malisimo",
        "Aprende a construir",
        "No sabes pelear",
        "Construyes como un noob.",
        "Así es como juegas Minecraft? Vergonzoso.",
    ]

    def __init__(self, mc):
        self.mc = mc

    def insult_random(self):
        insult = random.choice(self.INSULTS)
        self.mc.postToChat(insult)

    def insult_personalized(self, player_name="Jugador"):  
        insult = f"{player_name}, {random.choice(self.INSULTS)}"
        self.mc.postToChat(insult)

    def insult_funny(self):
        self.mc.postToChat("Un bebe juega mejor que tu")

    def run(self, should_continue):
        while should_continue():
            methods = [method for method in dir(self) if method.startswith("insult_")]
            chosen_method = random.choice(methods)
            getattr(self, chosen_method)()
            time.sleep(random.randint(5, 15))
