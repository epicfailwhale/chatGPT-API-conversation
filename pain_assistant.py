import openai
import os
from Chatter import Chatter


pain_assistant = Chatter()
start_sequence = "\nAI: "
restart_sequence = "\nHuman: "


user_input = input(restart_sequence)
respond = pain_assistant.chat(user_input)
print(start_sequence + respond)
