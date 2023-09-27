import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
import threading
import time

# Define patterns for the chatbot to recognize 
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thanks!', 'I am just a bot, but I am fine. How can I assist you?']),
    (r'what is your name?', ['I am a chatbot.', 'I don\'t have a name.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'what can you do?', ['I can answer questions, provide information, or just chat with you. How can I assist you today?']),
    (r'who created you?', ['I was created by Ritik Singh.']),
    (r'what is the weather like today\??', ['I\'m sorry, I cannot provide real-time weather information.']),
    (r'tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 'Sure, here\'s a joke: Parallel lines have so much in common. It\'s a shame they\'ll never meet.']),
    (r'tell me a fact', ['Did you know that honey never spoils? Archaeologists have even found pots of honey in ancient Egyptian tombs that are over 3,000 years old!']),
    (r'what is your favorite color?', ['I don\'t have a favorite color.']),
    (r'how old are you?', ['I don\'t have an age.']),
    (r'what is the meaning of life?', ['The meaning of life is a philosophical question that has been debated for centuries.']),
    (r'help', ['I\'m here to assist you. You can ask me questions or just chat.']),
    (r'(.*)', ["I'm sorry, I don't understand.", 'Could you please rephrase that?']),
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

# Function to handle sending user input and receiving chatbot responses
def send_message():
    user_input = input_field.get()
    if user_input.lower() == 'quit':
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        chat_log.insert(tk.END, "Chatbot: Goodbye!\n")
        input_field.delete(0, tk.END)
        input_field.config(state=tk.DISABLED)
        close_timer.start()
    else:
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot.respond(user_input)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n")
        input_field.delete(0, tk.END)
        

# Function to close the GUI after a set period of inactivity
def close_gui():
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("Chatbot")

# Create a scrolled text widget to display the chat log
chat_log = scrolledtext.ScrolledText(root, width=40, height=20)
chat_log.pack(padx=10, pady=10)

# Create an entry field for user input
input_field = tk.Entry(root, width=30)
input_field.pack(padx=10, pady=10)
input_field.bind('<Return>', lambda event=None: send_message())  # Bind Enter key to send_message function

# Create a Send button to send user input
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Create a timer to close the GUI 
close_timer = threading.Timer(5, close_gui) 
close_timer.daemon = True

# Start the GUI main loop
root.mainloop()
