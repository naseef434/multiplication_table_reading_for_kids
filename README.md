# Audio multiplication table for kids
install a pip module<br> 
---------------------------
#pip install pyttsx3  <br><br>
<h5>If you recieve errors such as</h5> No module named win32com.client,<br> No module named win32, <br> No module named win32api, <br>you will need to additionally install <h4>pypiwin32<h4>
<h5>Usage</h5>  
import pyttsx3<br>
engine = pyttsx3.init()<br>
engine.say("I will speak this text")<br>
engine.runAndWait()<br>
