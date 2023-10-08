import tkinter as tk
from tkinter import Scrollbar, Text
from gtts import gTTS
import os
import random

response_pack = {
    "greeting": ["Hello!", "Hi there!", "Greetings!"],
    "farewell": ["Goodbye!", "See you later!", "Farewell!"],
    "default": ["I'm not sure what to say.", "Could you please elaborate?", "I don't understand."],
}

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.chat_history = Text(root, bd=1, bg="white", height=8, width=50, font=("Arial", 14))
        self.chat_history.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        self.user_entry = tk.Entry(root, width=50, font=("Arial", 14))
        self.user_entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.send_button = tk.Button(root, text="Send", command=self.get_response, font=("Arial", 14))
        self.send_button.pack(side=tk.LEFT, padx=10, pady=10)

    def animate_text_typing(self, response, index=0):
        if index <= len(response):
            self.chat_history.insert(tk.END, response[index])
            self.root.after(100, self.animate_text_typing, response, index + 1)
        else:
            self.chat_history.insert(tk.END, "\n")
            self.generate_text_to_speech(response)  # Generate text-to-speech after typing animation

    def generate_text_to_speech(self, response):
        tts = gTTS(response, lang='en')
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")  # You can use pygame mixer for better audio control

    def get_response(self):
        user_input = self.user_entry.get()
        self.chat_history.insert(tk.END, "You: " + user_input + "\n")
        response_pack_key = "default"
        if "hello" in user_input.lower():
            response_pack_key = "greeting"
        elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
            response_pack_key = "farewell"
        response = random.choice(response_pack.get(response_pack_key, ["I'm not sure what to say."]))
        self.animate_text_typing("Chatbot: " + response)

        self.user_entry.delete(0, tk.END)  # Clear the input field

# Main driver code
if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()
