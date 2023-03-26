import os
import openai


class Chatter:
    def __init__(self):
        # Give AI instructions, and user / assistant examples
        
        openai.api_key = os.getenv("OPENAI_API_KEY") #insert your API key here        
        
        self.messages = [
            {"role": "system", "content": "You are an empathetic pain assistant who gives answers to the user"},
            {"role":"user","content":"I have sharp back pain"},
            {"role":"assistant","content":"Sharp back pain may have several causes. Are you experiencing any numbness, tingling or weakness in your legs?"}
        ]


    def chat(self, message):
        # Adds new conversation to model

        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        
        return response.choices[0].message.content
    

