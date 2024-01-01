import openai
import os
import time
import pyttsx3


#this is the key i used to create this bot
engine=pyttsx3.init()
openai.api_key = "OPENAI_API_KEY"

def bot():
    #starting prompt for this bot
    messages = []
    system_msg = "you are a sarcastic guy who makes jokes on everything"
    # system_msg = input("What type of chatbot would you like to create?\n")
    messages.append({"role": "system", "content": system_msg})

    print("\nI'm here for you!.")

    #main function for this bot
    while input != "quit()":
        message = input()
        messages.append({"role": "user", "content": message})




    #function to handle response

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")
        # engine.say(reply)
        # engine.runAndWait()

t=time.strftime("%H")
# strf creates a string 

if (int(t)>17):
    print("good evening sir!")
elif (int(t)<12):
    print("good morning sir!")
else:
    print("good afternoon sir!")
print("Time is",time.strftime("%H:%M:%S"))

def exit():
    a=input("Enter any key to enter BOT: ")
    if (a=="apocalypse"):
        return exit()
    else:
        print("Welcome Ghost!")
exit()
bot()