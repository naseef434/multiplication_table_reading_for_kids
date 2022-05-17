#import pip pyttsx3
import pyttsx3
#get a number
n = input("Enter a number : ")
#dicalred a dictinary for store all values and its string format
dic = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10" : "Ton",
    }
#decalred a empty string
text = ""
mul = 0
#initializing pyttsx3 engine
engine = pyttsx3.init()
#get rate property 
rate = engine.getProperty('rate')   
#set new value                         
engine.setProperty('rate', 150)
#get voicece property  male and female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
                   
for i in range(1,11):
    mul = i * int(n)
    text += str(i)+ " "+ dic[n]+ " are "+ str(mul)+ "\n"
    
engine.say(text)
print(text)
engine.runAndWait()
