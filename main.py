import threading
import mcpi.minecraft as minecraft
import time
from bots.tntbot import tntbot_run
from bots.insultbot import InsultBot
from bots.askbot import AskBot  

mc = minecraft.Minecraft.create()

# Estados de los bots
bots_state = {
    "tntbot": False,
    "insultbot": False,
    "askbot": False,  
}

insult_bot_instance = InsultBot(mc) 
ask_bot_instance = AskBot(mc)  

# Función para ejecutar un bot en un hilo separado
def start_bot(bot_name, bot_function):
    def bot_wrapper():
        bot_function(lambda: bots_state[bot_name])  

    bot_thread = threading.Thread(target=bot_wrapper, daemon=True)
    bot_thread.start()

# Monitor de comandos del chat
def monitor_chat():
    last_message = ""
    while True:
        messages = mc.events.pollChatPosts()
        for message in messages:
            if message.message != last_message:
                last_message = message.message
                handle_command(last_message)

# Manejo de comandos del chat
def handle_command(message):
    global bots_state
    command = message.lower()

    # Asegurarse de que el mensaje es un comando, es decir, comienza con "!"
    if message.startswith("!"):
        if command == "!start tntbot":
            if not bots_state["tntbot"]:
                bots_state["tntbot"] = True
                start_bot("tntbot", tntbot_run)
            else:
                mc.postToChat("TNTBot ya está activado.")

        elif command == "!stop tntbot":
            if bots_state["tntbot"]:
                bots_state["tntbot"] = False
            else:
                mc.postToChat("TNTBot ya está desactivado.")

        elif command == "!start insultbot":
            if not bots_state["insultbot"]:
                bots_state["insultbot"] = True
                start_bot("insultbot", insult_bot_instance.run) 

            else:
                mc.postToChat("InsultBot ya está activado.")

        elif command == "!stop insultbot":
            if bots_state["insultbot"]:
                bots_state["insultbot"] = False
            else:
                mc.postToChat("InsultBot ya está desactivado.")

        elif command == "!start askbot":  
            if not bots_state["askbot"]:
                bots_state["askbot"] = True
                start_bot("askbot", ask_bot_instance.run) 
            else:
                mc.postToChat("AskBot ya está activado.")

        elif command == "!stop askbot": 
            if bots_state["askbot"]:
                bots_state["askbot"] = False
            else:
                mc.postToChat("AskBot ya está desactivado.")

        else:
            mc.postToChat(f"Comando desconocido: {message}")

# Main function
if __name__ == "__main__":
    mc.postToChat("Sistema de gestion de bots iniciado. Escribe comandos como !start tntbot o !stop insultbot en el chat.")
    chat_thread = threading.Thread(target=monitor_chat, daemon=True)
    chat_thread.start()

    while True:
        time.sleep(1) 
