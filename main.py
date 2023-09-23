import os
import speech_recognition as sr
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import subprocess
import pyautogui
from pywinauto import Application, findwindows
import openai
import pyttsx3
import urllib.parse
import re
import pywhatkit

openai.api_key = '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'
engine = pyttsx3.init()

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1;
        audio = r.listen(source)
        try:
            print("Recognizing Kashish ...Wait")
            query = r.recognize_google(audio , language="en-in")
            print(f"Kashish said : {query}")
            return query
        except Exception as e:
            return "Some Error"

def write_and_save_text(text):
    time.sleep(2)
    pyautogui.typewrite(text)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl","s")
    time.sleep(1)
    save_as_dialog = None
    timeout = time.time()+10
    while not save_as_dialog and time.time() <timeout:
        save_as_dialog = findwindows.find_elements(title='Save As' , class_name='#32770')
    if save_as_dialog:
        save_as_dialog.set_focus()
        app = Application().connect(handle=save_as_dialog.handle)
        save_as_dialog = app.window(handle=save_as_dialog.handle)
        save_as_dialog.Save.click()
        time.sleep(1)
    else:
        say("I am Really Sorry")
def open_notebook():
    subprocess.Popen('notepad.exe')
    say("say context:")
    content = takeCommand()
    #content = generate_answer(query)
    say("please wait while we are saving your data ")
    write_and_save_text(content)


def login_to_instagram(username,password):
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com")
        time.sleep(2)
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[0])
        say("loooggggged in to your  instagram successfully")
    except Exception as e:
        say("we are sorry , some error occureed" , str(e))


def login_to_username():
    say("Maam , Please input the Instagram Username")
    ig_username=input("Kashish Please input the Instagram Username : ")
    say("Maam , Please input the Instagram Password")
    ig_password =input("Maam ,  Please say the Password : ")
    say("Please Wait while we are redirecting to the instagram")
    login_to_instagram(ig_username , ig_password)

def generate_answer(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )
    answer = response.choices[0].text.strip()
    return answer

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def ai_mail():
    #say("Using artificial intelligence...")
    say("you can ask me anything")
    query = takeCommand()
    if query:
        answer = generate_answer(query)
        print("Question:",query)
        say(answer)
        print("Answer:", answer)

def code_write_notepad():
    say("whats the problem statement")
    query = takeCommand()
    if query:
        answer = generate_answer(query)
        #code = urllib.parse.quote(answer)
        say("please wait while we are redirecting to notepad")
        write_code_to_notepad(answer)


def write_code_to_notepad(code):
    file_name = "code.txt"  # Specify the name of the file
    with open(file_name, "w") as file:
        file.write(code)
    say("your Code written to Notepad.")
    subprocess.Popen(["notepad.exe", file_name])
def write_and_save_text(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def extract_subject_from_body(body):
    pattern = r"Subject:\s*(.*)"

    match = re.search(pattern, body, re.IGNORECASE)

    if match:
        subject = match.group(1).strip()
        return subject

    return "No Subject"

def write_and_open_email():
    #recipient = input("Enter recipient's email address: ")
    print("Ma'am , please speak the subject on which you wanna write mail")
    say("Ma'am , please speak the subject on which you wanna write mail")
    query = takeCommand()

    body = generate_answer(query)

    subject = extract_subject_from_body(body)
    os.startfile("mailto:")

    encoded_subject = urllib.parse.quote(subject)
    encoded_body = urllib.parse.quote(body)

    email_url = f"mailto:?subject={encoded_subject}&body={encoded_body}"

    # Open the email URL in the default web browser
    webbrowser.open(email_url)
    say("Your Mail is Written Successfully")

if __name__ == '__main__':
    print('PyCharm')
    say("hey i am Your Assistant kashish .........How may i help you?")
    while True:
        print("listening.....")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"] , ["wikipedia","https://www.wikipedia.com"] , ["google","https://www.google.com"] , ["instagram","https://www.instagram.com"] , ["leetcode","https://www.leetcode.com"] , ["codechef","www.codechef.com"],["pramp","https://pramp.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"opening {site[0]} sir")

        if "login instagram" in query.lower():
            login_to_username()

        if "open notebook" in query.lower():
            open_notebook()

        if query:
            if "audio solution".lower() in query.lower():
                ai_mail()
        if query:
            if "send mail".lower() in query.lower():
                write_and_open_email()

        if "depressed" in query.lower():
            say( "I'm really sorry to hear that you're feeling depressed. Remember that you're not alone, and there are people who care about you. If you need someone to talk to, consider reaching out to a friend, family member, or mental health professional. Take care of yourself.")

        if "sad" in query.lower():
            say( "I'm sorry to hear that you're feeling sad. It's important to acknowledge and express your emotions. If you need someone to talk to or support, don't hesitate to reach out to a trusted person in your life. You're not alone.")

        if "suicide" in query.lower():
            say("I'm really concerned about what you're going through. If you want to talk about it, I'm here to listen.")

        if "generate code" in query.lower():
            code_write_notepad()

        if "quit".lower() in query.lower():
            exit()

        if "set up".lower() in query.lower():
            say("please wait while am setting up your pc for you")
            webbrowser.open("https://www.leetcode.com")
            webbrowser.open("https://web.whatsapp.com")
            webbrowser.open("https://www.youtube.com")
            webbrowser.open("https://chat.openai.com/")
            webbrowser.open("https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems")
            say("Completed Ma'am")

        if "reset chat".lower() in query.lower():
            chatStr = ""

        if "text".lower() in query.lower():
            contact_name = "+91 8955269344"
            message = takeCommand()
            time_hour = 4
            time_second = 4
            contacts = {
                "sia": "+91 8955269344",
                "dad": "+91 9460203787",
                "mom": "+91 9783903787",
                "papa": "+919460203787",
                "akshu":"+918905977246",
                "adrika":"+919971957205"

                # Add more contact names and phone numbers here
            }
            if contact_name in contacts:
                contact_number = contacts[contact_name]
                pywhatkit.sendwhatmsg(contact_number, message)
            else:
                print("Contact not found!")
            #pywhatkit.sendwhatmsg_instantly(contact, message)

















