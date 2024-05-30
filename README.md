
# 🔴 How People Can Interact With My Avatar In Live ? 👥

![Group 564](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/fc085160-6bb6-41eb-a3e1-0c737d851392)

# Hey there it's Hyroe ! :3

I will explain to you how people in your Tiktok Live can interact with your avatar on VRChat.

## 1 / First Step Link Tiktok Chat and send it to the OSC Server :

→ First Download PyCharm Community by this link: [Download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)

→ Create a New Python Project and create a python file in this folder

![Capture d'écran 2024-05-28 033232](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/983f4efb-e8aa-4b4a-a22f-8c6d1c4c356b) ![Capture d'écran 2024-05-28 033254](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/e8fccf90-bea9-4789-bfa1-5dd68f568ac3)


→ Copy Paste the code and install all the libraries that you need :
 - In Python packages import "TiktokLive" and install it

![Capture d'écran 2024-05-28 032950](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/4597f5a0-6f6a-447b-8261-60fee8fabf33)
![Capture d'écran 2024-05-28 033156](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/70d99656-a8be-43d9-b0ac-42cd85861908)

 - And import this github : https://github.com/attwad/python-osc
  "Add Package" → "From Version Control" → Copy & Paste and press "OK"

![Capture d'écran 2024-05-28 033015](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/c7d4fa9b-0182-4f69-a528-291f2a9bcf48)
![Capture d'écran 2024-05-28 033050](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/3a1c149f-da94-4813-a915-6bd088551d52)


→ Put your Tiktok Name Tag (for me it is @hyroe at line 51) and run the python program when you are live

![Capture d'écran 2024-05-28 033221](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/100a0e86-8733-46ae-927f-052b550b4581)

## 2 / Link Parameters in your “.Json” file

With the help of the OSC Server, we will be able to send and receive data.
For example, in the code given, if someone sends “boop” in the Tiktok chat, BoopToggle is not equal to 1.

### You have now to add this parameter in the text file of your avatar.

→ If you want to understand how the OSC parameters work here is the link from the official webpage of VRChat (Please Read it :3) :
https://docs.vrchat.com/docs/osc-avatar-parameters

→ Copy the Blueprint ID in your Pipeline Manager Component of your avatar in your Unity Project

![Group 561](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/24a76fe5-8c09-4d54-9ab6-4e35a7a5a23b)

→ Open this folder : C:\Users\YourName\AppData\LocalLow\VRChat\VRChat\OSC

Search (CTRL+F) by Copy Pasting your ID and open the .json file
And you should have something like that with different parameters :

![Group 562](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/aeea7185-e6a8-48ce-b9f0-ce510e7440cb)

Now we want to add our new parameter which is ”BoopToggle”.
```
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
```
> Check if your parameter in your unity project is a Boolean, if not change the type.

## 3 / Test On VRChat :3

→ Enable OSC Server

![Capture d'écran 2024-05-28 035221](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/3411ea1b-76cd-4bc1-b9fe-a91c14ae7df7)
![Capture d'écran 2024-05-28 035255](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/78359d0e-7062-4bb9-b16a-b3816f448580)

→ After Starting your Tiktok Live and running your code you should have this in your OSC Debug Panel

![Capture d'écran 2024-05-28 035448](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/5b4cf95a-1ff3-4b30-a78a-72b157a58a08)
![Capture d'écran 2024-05-28 035417](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/9524090b-ffe9-4c01-90c9-57908f367a52)

> Sometimes it’s not working for some people in my lives, so if you have an idea let me know ! :3

Have a wonderful day/night

→ Follow me on my socials : 

https://www.tiktok.com/@hyroe

https://x.com/_Hyroe_

https://www.instagram.com/hyroevr/

Boop from Hyroe :3

