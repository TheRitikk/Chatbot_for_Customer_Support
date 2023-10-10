import tkinter as tk
from tkinter import scrolledtext, StringVar
import threading
from googletrans import Translator

# Create a translator instance
translator = Translator()

# Define a function to interact with the chatbot
def chat_with_bot():
    user_input = input_field.get()
    # Get the selected translation direction
    selected_language = language_choice.get()

    # Translate user input based on the selected language
    if selected_language == "English to Hindi":
        translated_input = translator.translate(user_input, src='en', dest='hi').text
    else:  # Hindi to English
        translated_input = translator.translate(user_input, src='hi', dest='en').text

    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "Chatbot: " + translated_input + "\n")
    chat_log.insert(tk.END, "\n")
    input_field.delete(0, tk.END)

# Function to close the GUI after a set period of inactivity
def close_gui():
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("Language Translator Chatbot")
root.geometry("500x450")

# Create a StringVar to store the selected language choice
language_choice = StringVar()

english_hindi = tk.Radiobutton(root, text="English to Hindi", value="English to Hindi", variable=language_choice)
hindi_english = tk.Radiobutton(root, text="Hindi to English", value="Hindi to English", variable=language_choice)
english_hindi.grid(row=0, column=0)
hindi_english.grid(row=0, column=1)

# Initialize the radio button choice
language_choice.set("English to Hindi")

# Create a scrolled text widget to display the chat log
chat_log = scrolledtext.ScrolledText(root, width=58, height=20)
chat_log.grid(padx=10, pady=10, columnspan=2)
chat_log.insert(tk.END, "Chatbot: Hello! I'm the Language Learning Bot. I can help you learn and practice vocabulary.\n")
chat_log.insert(tk.END, "\n")

# Create an entry field for user input
input_field = tk.Entry(root, width=30)
input_field.grid(padx=10, pady=10, columnspan=2)
input_field.bind('<Return>', lambda event=None: chat_with_bot())  # Bind Enter key to chat_with_bot function

# Create a Send button to send user input
send_button = tk.Button(root, text="Enter", command=chat_with_bot)
send_button.grid(pady=5, columnspan=2)

# Create a timer to close the GUI
close_timer = threading.Timer(5, close_gui)
close_timer.daemon = True

# Start the GUI main loop
root.mainloop()
