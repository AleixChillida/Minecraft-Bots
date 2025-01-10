import random
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

class AskBot:
    def __init__(self, mc):
        self.mc = mc

    def question_1(self):
        question = "Cual es el bloque mas resistente en Minecraft?"
        answer = "bedrock"
        self.ask_question(question, answer)

    def question_2(self):
        question = "Como se llama el jefe final de Minecraft?"
        answer = "ender dragon"
        self.ask_question(question, answer)

    def question_3(self):
        question = "Cual es el nombre de la dimension que tiene un portal con bloques de obsidiana?"
        answer = "nether"
        self.ask_question(question, answer)

    def ask_question(self, question, correct_answer):
        self.mc.postToChat(question)
        self.mc.postToChat("Escribe tu respuesta en el chat, tienes 15 segundos.")
        
        player_answer = self.wait_for_answer(correct_answer)
        
        if player_answer:
            if player_answer.lower() == correct_answer.lower():
                self.mc.postToChat("Correcto!")
            else:
                self.mc.postToChat(f"Incorrecto. La respuesta correcta es {correct_answer}.")
        else:
            self.mc.postToChat("No se recibio respuesta a tiempo.")

    def wait_for_answer(self, correct_answer, timeout=15):
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            messages = mc.events.pollChatPosts()
            for message in messages:
    
                if message.entityId != -1 and not message.message.startswith("!"):
                    player_answer = message.message
                    return player_answer
            time.sleep(1) 
        
        return None  
    
    def run(self, should_continue):
        while should_continue():
            
            question_methods = [getattr(self, method) for method in dir(self) if method.startswith("question_")]
            
            
            question_method = random.choice(question_methods)
            question_method()  
            
            time.sleep(10)  

ask_bot_instance = AskBot(mc)
