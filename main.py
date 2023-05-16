# Import required libraries
from tkinter import *
import threading
import speech_recognition as sr
import openai
import os
import pyttsx3
import sqlite3

# Initialize pyttsx3 for text-to-speech conversion
engine = pyttsx3.init()

# Define a function to handle text-to-speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the ChatGPT model
from pyChatGPT import ChatGPT

# Initialize SpeechRecognition and ChatGPT
r = sr.Recognizer()

API_KEY_FILE = 'hidden_key.txt'

with open(API_KEY_FILE, 'r') as file:
    api_key = file.read().strip()

os.environ['OPENAI_Key'] = api_key
openai.api_key = os.environ['OPENAI_Key']

response_cache = {}

# Define a function to generate responses using ChatGPT
def generate_response(prompt):
    if prompt in response_cache:
        return response_cache[prompt]

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    response_cache[prompt] = message
    return message

# Define a function to capture speech and convert it to text using STT API
def transcribe_speech():
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=10) # Capture speech for 10 seconds
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return None


def start_chat_threaded():
    threading.Thread(target=start_chat).start()

# Define a function to start the chatbot
def start_chat():
# Create a GUI using Tkinter
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("500x570+100+30")
    screen3.title("Chatbot By Prasad")
    screen3.config(bg="Orange")

# Create logo and center frame
    logoPic = PhotoImage(file="pic.png")
    logoPicLabel = Label(screen3, image=logoPic, bg="Orange")
    logoPicLabel.pack()

    centerframe = Frame(screen3)
    centerframe.pack()

# Create chat history textbox and scrollbar
    global Scrollbar
    Scrollbar = Scrollbar(centerframe)
    Scrollbar.pack(side=RIGHT)

# Create a text area to display the chat
    textarea = Text(centerframe, font=('times new roman',15,'bold'), height=15, yscrollcommand=Scrollbar.set)
    textarea.pack(side=LEFT)

    Scrollbar.config(command=textarea.yview)
    
    prompt = ("Krishna: Hi! How can I help you today?\n")
    textarea.insert(END, prompt)
    screen3.update() # Update the GUI to handle events
    speak(prompt) # Speak the prompt
    user_inputs = []
    while True:
        user_input = transcribe_speech()
        if user_input:
            user_inputs.append(user_input)
            prompt = "You: " + user_input + "\n"
            response = generate_response(prompt)
            response_text = "Krishna: " + response + "\n"
            textarea.insert(END, prompt)
            textarea.insert(END, response_text)
            speak(response) # Speak the response
            screen3.update() # Update the GUI to handle events
        if len(user_inputs)>= 100: # Stop capturing inputs after 100 questions
                break
    prompt ="Thank you for using our chatbot. Have a nice day!\n"
    textarea.insert(END, prompt)
    screen3.update() # Update the GUI to handle events  
    Button(screen3, Text="End Chat", width=10, height=10, command=stop_chat())
    Button.pack()

def stop_chat():
    print("Chat stopped.")
    start_chat.exit()  
    

def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END) 

    Label(screen1,text="Registration sucess", fg= "green", font= ("calibri", 11)).pack()

def login_verify():
    
    username1= username_verify.get()
    password1= password_verify.get()
    
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1, "r")
        verify=file1.read().splitlines()
        if password1 in verify:
            start_chat()  
        else:
            print("password_not_recognised")
    else:
        print("User_not_found")           

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password, show='*')
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()

def login():
    global screen2
    screen2= Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter the details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify 
    global password_verify  

    username_verify=StringVar()
    password_verify=StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username * ").pack()
    username_entry1=Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1=Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login",width=10, height=1, command= login_verify).pack()
   
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Chatbot by Prasad")
    Label(text="Your Personal Companion",bg="Orange", width="300", height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

# Start the mainscreen event loop
    screen.mainloop()
main_screen()
