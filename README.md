Hey there it's Hyroe ! :3

I will explain to you how people in your Tiktok Live can interact with your avatar on VRChat.

Better Reading : https://docs.google.com/document/d/1Q8Hfh12RfJzjGYOhaSmSvGoVqKZTlRy5qdYyMNvEByM/edit?usp=sharing

1 / First Step Link Tiktok Chat and send it to the OSC Server :

→ First Download PyCharm Community by this link: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC

→ Create a New Python Project and create a python file in this folder

→ Copy Paste the code and install all the libraries that you need :
 - In Python packages import "TiktokLive" and install it
 - And import this github : https://github.com/attwad/python-osc
  "Add Package" → "From Version Control" → Copy & Paste and press "OK"

→ Put your Tiktok Name Tag (for me it is @hyroe at line 51) and run the python program when you are live

2 / Link Parameters in your “.Json” file

With the help of the OSC Server, we will be able to send and receive data.
For example, in the code given, if someone sends “boop” in the Tiktok chat, BoopToggle is not equal to 1.

You have now to add this parameter in the text file of your avatar.

→ If you want to understand how the OSC parameters work here is the link from the official webpage of VRChat (Please Read it :3) :
https://docs.vrchat.com/docs/osc-avatar-parameters

→ Copy the Blueprint ID in your Pipeline Manager Component of your avatar in your Unity Project

→ Open this folder : C:\Users\YourName\AppData\LocalLow\VRChat\VRChat\OSC

Search (CTRL+F) by Copy Pasting your ID and open the .json file
And you should have something like that with different parameters :

Now we want to add our new parameter which is ”BoopToggle”.
    {
      "name": "BoopToggle",
      "input": {
        "address": "/avatar/parameters/BoopToggle",
        "type": "Boolean"
      },
      "output": {
        "address": "/avatar/parameters/BoopToggle",
        "type": "Boolean"
      }

Check if your parameter in your unity project is a Boolean, if not change the type.

3 / Test On VRChat :3

→ Enable OSC Server

→ After Starting your Tiktok Live and running your code you should have this in your OSC Debug Panel

→ Sometimes it’s not working for some people in my lives, so if you have an idea let me know ! :3

Have a wonderful day/night

→ Follow me on my socials : 
https://www.tiktok.com/@hyroe
https://x.com/_Hyroe_
https://www.instagram.com/hyroevr/

Boop from Hyroe :3

