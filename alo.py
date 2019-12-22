from tkinter import *
from PIL import Image, ImageTk
 
root = Tk()
root.title("Voice Assistant")
root.geometry("900x540")
root.configure(background="black")
def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
def onclick():
    import pyttsx3 
    import speech_recognition as sr 
    import datetime
    import wikipedia 
    import webbrowser
    import os
    import smtplib
    import random
    import pyautogui
    import time

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am Stark Sir. Please tell me how may I help you")       

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Tell what can I do fo you?")
            print("Listening...")
            r.pause_threshold = 1    
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print("User said: {}\n".format(query))

        except Exception as e:
            print(e)    
            speak("Say that again please...")  
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('agulabk4444@gmail.com', 'anirudh4444@kumar')
        server.sendmail('agulabk4444@gmail.com', to, content)
        server.close()


    if __name__ == "__main__":
        wishMe()
        
        while True:
            #if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'tell me about' in query:
                speak('Searching Wikipedia...')
                query = query.replace("tell me about", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")      
                print(results)
                speak(results)
            elif 'wikipedia' in query:
                
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)    

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("opening youtube")

            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("opening Google")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                speak("stackoverflow.com")
                speak("opening stackflow")
            elif 'play music' in query:
                speak("playing music")
                webbrowser.open("https://gaana.com/playlist/gaana-dj-bollywood-top-50-1")
                jk=time.sleep(10)
                n=pyautogui.press("tab")
                ol=pyautogui.press("tab")
                fg=pyautogui.press("space")     
            elif 'play' in query:
                l=pyautogui.press("playpause")
            elif 'now' in query:
                n=pyautogui.press("tab")
                ol=pyautogui.press("tab")
                fg=pyautogui.press("space")            
            elif 'love' in query:
                print("Well.I am already married to your laptop!")
                speak("Well!!!!!!!!!!!!I am already married to your laptop!")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak("Sir, the time is {}".format(strTime))
            elif 'email' in query:
                speak("Email to ruhi")
                try:
                    speak("What should I send?")
                    content = takeCommand()
                    to = "1606246@kiit.ac.in"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email") 
            elif 'song' in query:
                mus= 'C:\\Users\\nEW u\\Music\\iTunes\\Album Artwork\\Download'
                songs = os.listdir(mus)
                print(songs)  
                
                i=random.randint(0,(len(songs)-1))
                c=os.startfile(os.path.join(mus, songs[i]))
            elif 'open chrome' in query:
                codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)
            elif 'open firefox' in query:
                codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
                os.startfile(codePath)            
            elif 'coding' in query:
                codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
                os.startfile(codePath)  
            elif 'diary' in query:
                from datetime import datetime,date
                ab="C:\\Windows\\notepad.exe"   
                os.startfile(ab)                    
                time.sleep(2)
                speak("Start writing diary after I say start")
                
                pyautogui.typewrite("Dear Diary,")
                pyautogui.press("enter")
                time.sleep(1)
                speak("Start")
                sr.Microphone(device_index=1)
                a=sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening")
                    a.pause_threshold = 2
                    audio=a.listen(source)
                    try:
                        qu = a.recognize_google(audio, language='en-in')
                        print("User said: {}\n".format(qu))
                        pyautogui.typewrite(qu,interval=0.10)
                        zx=str(datetime.now().date())
                        pyautogui.hotkey('ctrl','s')
                        time.sleep(1)
                        pyautogui.typewrite(zx)
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.hotkey('alt','f4')
                    
                    except:
                        speak("Can't recognise")                    
            
            
            elif 'joke' in query:

                hj=["Difference between a beautiful night and a horror night.Beautiful night is,When you hug your teddy bear and sleep.Horror night is,When your teddy bear hugs you BACK.","Once all the engineering professors were sitting in one plane.Before the takeoff, one announcement came“This plane is made by your students”Then all the professors stood up, ran and went outside.But the principal was sitting.One guy came and asked, “are you not afraid”?Then the principal replied“I trust my students very well and I am sure the plane won’t even start”.","A man inserted an ‘ad’ in the classifieds: “Wife wanted.” Next day he received a hundred letters. They all said the same thing: “You can have mine.”","Two police officers crash their car into a tree. After a moment of silence, one of them says, “Wow, that’s got to be the fastest we ever got to the accident site.”","A man asks a farmer near a field, “Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.”The farmer says, “Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.”","An Engineer Having No Child, No Money, No Home, Blind Mother, Prays To God.God Says He Will Grant Him One Wish.Engineer: “I Want My Mother To See My Wife Putting Diamond Bangles On My Child’s Hands In Our New Bungalow.”God: “Damn! I Still Have A Lot To Learn From These Engineers.”Engineers Always Rock.","The Englishman responds, ‘I’d like to hear “God Save The Queen” just one more time to remind me of the auld country, played by the London All Boys Choir. With Morris Dancers Dancing to the tune.’"]            
                i=random.randint(0,(len(hj)-1))
                speak(hj[i]+"!hahahahahahaha")
                #speak(" Catch her by her waist!!!!! Bring her home!!!!! Keep ur hand on her neck!!!! Put ur lips on her lips!!!! & have a Nice Drink ?COCA COLA? Buurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr ;-)")
                
            elif 'google' in query:
                speak("What do you want to search?")
                sr.Microphone(device_index=1)
                a=sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening")
                    audio=a.listen(source)
                    try:
                        qu = a.recognize_google(audio, language='en-in')
                        print("User said: {}\n".format(qu))
                        speak("Searching")
                        print("Searching")
                        webbrowser.open('https://www.google.com/search?q='+ qu)
                    except:
                        speak("Can't recognise")
            elif 'search youtube' in query:

                speak("What do you want to search?")
                sr.Microphone(device_index=1)
                a=sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening")
                    audio=a.listen(source)
                    try:
                        qu = a.recognize_google(audio, language='en-in')
                        print("User said: {}\n".format(qu))
                        speak("Searching")
                        print("Searching")
                        webbrowser.open('https://www.youtube.com/results?search_query='+ qu)
                    except:
                        speak("Can't recognise")
                        

            elif 'search music' in query:
                speak("What do you want to search?")
                sr.Microphone(device_index=1)
                a=sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening")
                    audio=a.listen(source)
                    try:
                        qu = a.recognize_google(audio, language='en-in')
                        print(f"User said: {qu}\n")
                        speak("do you want to search ")
                        webbrowser.open('https://gaana.com/search/'+qu)
                        time.sleep(5)
                       
                        speak("Searching")
                        print("Searching")                          
                    except:
                        speak("Can't recognise")
                                                                          
            elif 'pause music' in query:
                pyautogui.press('space')

            elif 'bye' in query:
                speak("Good Bye sir!!Hope to meet you soon...")
                break
            elif 'sleep' in query:
                speak("Meet you after five minutes")

                v=time.sleep(300)

                speak("I am back sir..")
                continue
 
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
 
        self.image = Image.open("ANIR.png")
        self.img_copy= self.image.copy()
 
        self.background_image = ImageTk.PhotoImage(self.image)
 
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
 
        mi_but1=PhotoImage(file="micro1.png")
        button2 = Button(self.background, text='button2',image=mi_but1,command=onclick,highlightthickness = 0, bd = 0)
        button2.image=mi_but1
        button2.pack()
        button2.place(relx=0.5, rely=0.5, anchor=CENTER)

 
    def _resize_image(self,event):
 
        new_width = event.width
        new_height = event.height
 
        self.image = self.img_copy.resize((new_width, new_height))
 
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
 
e = Example(root)
e.pack(fill=BOTH, expand=YES)
root.mainloop()
