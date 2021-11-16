import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
#import smtplib
import webbrowser
import math
import time
import pywhatkit as kit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
print(voices[1].id)
engine.setProperty('voices', voices[0].id)
count = 0
"""def engnumtoint():
 dictone = 
{"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"tw
elev":12,"thirteen":13
 ,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
 dicttwo = 
{"twenty":20,"thirty":30,"fourty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
 dictthree = 
{"hundred":100,"thousand":1000,"lack":100000,"crore":10000000,"million":1000000,"billion":10000000
00}
 # taking input from users
 query9 = takecommond().lower() takinginput = query9
 #takinginput = input("please enter the number in english")
 templist = []
 #now splitting the words in number
 splitting = takinginput.split(" ")
 x1 = len(splitting)
 for i in splitting:
 storing_index = (splitting.index(i))
 for i in splitting:
 for j in dictthree.keys():
 if i==j:
 y = splitting.index(j)
 #print(y)
 x = y-2
 #print(splitting[x])
 if splitting[x] in dicttwo.keys():
 z1 = dicttwo[splitting[x]]
 if splitting[x+1] in dictone.keys():
 z2 = dictone[splitting[x+1]]
 #print(z2)
 num1 = z1+z2
 finalnum1 = num1*dictthree[splitting[y]]
 templist.append(finalnum1)
 #print(templist)
 elif splitting[x+1] in dicttwo.keys():
 z1 = dicttwo[splitting[x+1]]
 finalnum3 = z1*dictthree[splitting[y]]
 templist.append(finalnum3)
 #print(z1) elif splitting[x+1] in dictone.keys():
 z3 = dictone[splitting[x + 1]]
 #print(z3)
 num1 = z3
 finalnum1 = num1 * dictthree[splitting[y]]
 templist.append(finalnum1)
 #print(templist)
 #print(splitting[x1-1])
 for i in splitting:
 if splitting[x1-2] in dicttwo.keys():
 y2 = dicttwo[splitting[x1-2]]
 num3 = y2
 #print(splitting[x1-2])
 if splitting[x1-1] in dictone.keys():
 y1 = dictone[splitting[x1-1]]
 #print(splitting[x1-1])
 num2 = y1
 finalnum2 = num3+num2
 templist.append(finalnum2)
 elif splitting[x1-1] in dictone.keys():
 y3 = dictone[splitting[x1-1]]
 #print(splitting[x1-1])
 num4 = y3
 templist.append(num4)
 break
 res = 0
 for i in templist:
 res = int(res+i)
 return int(res)"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#wishme function is here
def wishMe():
    #query11 = takecommond().lower()
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('hello sir good night')
    if hour >= 12 and hour <= 18:
        speak('hello sir Good afternoon')
    if hour > 18 and hour <= 24:
        speak('hello sir Good night')
        speak('I hope your day is going well')
    identity()
# univeral takecommond is here
def takecommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1
        #r.energy_threshold = 4000
        #r.dynamic_energy_threshold = True
        #r.dynamic_energy_adjustment_damping = 0.15
        #r.dynamic_energy_ratio = 1.5
        #r.operation_timeout = 0.15
        audio = r.listen(source)
    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='hn-in')
        print(f"user said :{query}\n")
    except Exception as e:
        print("sorry sir i am not understanding please say it again.....")
        return "None"
    return query
# identity commond is here
def identity():
    speak("Sir please confirm your identity")
    query = takecommond().lower()
    print(query)
    #aman = ["aman","amman","a man","common","man"]
    name = "Hello Sir , I am vision vision it is my honour to serve you.please let me know how may i help you"
    if 'seema' in query:
        speak("Hello mammi, I am Vision It is my honour to serve you. please tell me how i can help you")
    elif "aman" in query:
        speak("Hello aman Sir, I am Vision It is my honour to serve you. please tell me how i can help you")
    elif "vijay" in query:
        speak("Hello vijay Sir, I am Vision It is my honour to serve you. please tell me how i can help you")
    elif "a man" in query:
        speak("Hello aman Sir, I am Vision It is my honour to serve you. please tell me how i can help you")
    elif "amman" in query:
        speak("Hello aman Sir, I am Vision It is my honour to serve you. please tell me how i can help you")
    elif 'beauty' in query:
        speak("Hello beauty Mam, I am Vision It is my honour to serve you. please tell me how i can help you")
 #studybeauty()
    elif 'avdhesh' in query:
        speak("Hello papa, I am jarvis It is my honour to serve you. please tell me how i can help you") # elif 'Ravi' in query:
    #speak("Hello Ravi Sir, I am Vision It is my honour to serve you. please tell me how i can help you")
    #elif 'ashutosh' in query:
    #speak("Hello Ashutosh Sir, I am Visions It is my honour to serve you. please tell me how i can help you")
    else:
        speak("You are not authorised to use me ")
        #speak("Now fuck off You asshole")
        exit()
# math function is here
def math_quadratic_fun():
    speak("what you want to solve in math sir")
    query6 = takecommond().lower()
    if "equation" in query6:
        speak("okay sir please follow the given step to solve it")
        #print("fill in the blanks to get the roots of the equation")
        print("____x^2")
        speak("please tell me the coefficient of x square")
        x1 = takecommond()
        a = int(x1)
        print("____x")
        speak("please tell me the coefficient of x")
        x2 = takecommond()
        b = int(x2)
        speak("please tell me the coefficient of constant term")
        x3 = takecommond()
        c = int(x3)
        print(a,b,c)
        z = ((b * b) - (4 * a * c))
        sq = math.sqrt(int(z))
        w1 = ((-b / 2 * a) + (sq / 2 * a))
        w2 = ((-b / 2 * a) - (sq / 2 * a))
        print("Roots of the given equation are", "\n", w1, w2)
        speak("Roots of the given equation are")
        speak(w1)
        speak(w2)
    elif "table" in query6:
        speak("please tell me the number sir to get table")
        count = 1
        query7 = takecommond().lower()
        x = int(query7)
        #x = int(input("enter the number to get the table"))
        while count <= 10:
            z = x * count
            speak(x)
            if count == 1:
                speak("onezaa")
            elif count == 2:
                speak("twozaa")
            elif count == 3:
                speak("threeza")
            elif count == 4:
                speak("fourzaa")
            elif count == 5:
                speak("fivezaa")
            elif count == 6:
                speak("sixzaa")
            elif count == 7:
                speak("sevenzaa")
            elif count == 8:
                speak("eightzaa")
            elif count == 9:
                speak("ninezaa")
            else:
                speak("tenzaa")
            speak(z)
            count += 1
            time.sleep(0.05)
    elif "simple math" in query6:
        sum = 0
        sub = 0
        mul = 1
        div = 1
        print(
        "please enter \n '+' for addition \n '-' for substraction \n '*' for multiplication \n '/' for dividation")
        speak("sir here you can do all the basic things in math like addition,substraction and other things")
        speak("sir what you want to do, you can exit anytime by saying exit only ")
        user = takecommond().lower()
        while True:
            speak("sir please tell me the next number to add")
            y = takecommond()
            if "add" == user.lower():
                if y == "exit":
                    exit()
                sum = sum + int(y)
                print(sum)
                speak("sum is")
                speak(sum)
            elif "subbstract" == user.lower():
                if y == "exit":
                    exit()
                sub = int(y) - sub
                print(sub)
                speak("sub is")
                speak(sub)
            elif "multiplication" == user.lower():
                if y == "exit":
                    exit()
                mul = int(y) * mul
                print(mul)
                speak("multiplicaton is")
                speak(mul)
            elif "division" == user.lower():
                if y == "exit":
                    exit()
                div = int(y) / div
                print(div)
                speak("division is")
                speak(div)
            else:
                exit()
if __name__ == '__main__':
    wishMe()
    while True:
        if 1:
            query = takecommond().lower()
            if "wikipedia" in query:
                speak("searching wikipedia")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak('according to wikipedia')
                speak(result)
            elif "what can you do " in query:
                speak("Sir I can do whatever you want to do")
                speak('basically I can do baisc things like youtube,wikipedia and open other websites')
            elif "open youtube" in query:
                webbrowser.open('youtube.com')
                speak("opening youtube")
                speak("what you want to watch on youtube sir")
                if(1):
                    query2 = takecommond().lower()
                    kit.playonyt(query2)
                    speak("opening")
                    speak(query2)
            elif "open brazzers videos" in query:
                webbrowser.open("xvideos5.com")
                speak("opening x videos")
                break
            elif "open google" in query:
                webbrowser.open('google.com')
                speak("opening google")
                break
            elif "open up car shop" in query:
                webbrowser.open('apkashop.com')
                speak("opening apkashop")
                speak("sir do you want to open admin pannel of apkashop")
                query2 = takecommond().lower()
                if "yes" in query2:
                    webbrowser.open("apkashop.com/login")
                    break
                else:
                    speak("ok sir you can continue to official site")
                    break
            elif "play music" in query:
                music_dir = 'D:\\videos'
                videos = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, videos[40]))
                break
            elif "math" in query:
                math_quadratic_fun()
            elif "exit" in query:
                speak("I am shutting down my system sir")
                speak("thanks for using me sir")
                exit()
            elif "search" in query:
                kit.search(query[7:])
            elif "solve" in query:
                speak("sir please give me the equation")
                x1 = takecommond()
                x = eval(x1)
                print(x)
                speak(x)
            elif"message" in query:
                speak("sir please tell me the number to send")
                n1 = takecommond()
                n2 = "+91"
                n3 = n2+n1
                speak("sir please tell me message")
                n4 = takecommond()
                hour1 = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute)
                if len(n4)>30:
                    minute = minute+2
                else:
                    minute = minute+1
                    speak("sending messages in")
                    x = kit.sendwhatmsg(n3,n4,hour1,minute)
                    continue
