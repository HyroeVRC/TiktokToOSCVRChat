# 🔴 How People Can Interact With My Avatar In Live? 👥

![Group 564](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/fc085160-6bb6-41eb-a3e1-0c737d851392)

# Hey there, it's Hyroe ! :3

Welcome! I'll guide you through how your audience on TikTok Live can interact with your avatar on VRChat.

## 1. Link TikTok Chat and Send it to the OSC Server

### Step 1 : Download PyCharm Community

→ Download PyCharm Community from this link : [Download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)

### Step 2 : Set Up a New Python Project

→ Create a new Python project and a Python file within the project folder.

![New Project](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/983f4efb-e8aa-4b4a-a22f-8c6d1c4c356b)
![Create Python File](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/e8fccf90-bea9-4789-bfa1-5dd68f568ac3)

### Step 3 : Install Necessary Libraries

→ Copy and paste the provided code and install the required libraries:

- Install the `TiktokLive` package :
  ![Install TiktokLive](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/4597f5a0-6f6a-447b-8261-60fee8fabf33)

- Import the `python-osc` package from GitHub :
  ![Import python-osc](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/c7d4fa9b-0182-4f69-a528-291f2a9bcf48)

### Step 4 : Configure Your TikTok Name Tag

→ Set your TikTok name tag (e.g., `@hyroe`) at line 51 in the code and run the Python program when you go live.

![Set TikTok Name](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/100a0e86-8733-46ae-927f-052b550b4581)

## 2. Link Parameters in Your `.Json` File

With the OSC server, you can send and receive data. For example, if someone types "boop" in the TikTok chat, the `BoopToggle` parameter will be set.

### Step 1 : Understand OSC Parameters

→ Read the official VRChat documentation on OSC parameters: [OSC Avatar Parameters](https://docs.vrchat.com/docs/osc-avatar-parameters)

### Step 2 : Copy Your Avatar's Blueprint ID

→ Copy the Blueprint ID from the Pipeline Manager component of your avatar in Unity.

![Blueprint ID](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/24a76fe5-8c09-4d54-9ab6-4e35a7a5a23b)

### Step 3 : Modify the `.json` File

→ Navigate to `C:\Users\YourName\AppData\LocalLow\VRChat\VRChat\OSC`, search for your Blueprint ID, and open the corresponding `.json` file.

![Open JSON File](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/aeea7185-e6a8-48ce-b9f0-ce510e7440cb)

→ Add the new parameter `BoopToggle`:

```json
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
}
```

### Step 4 : Check Parameter Type

→ Ensure the `BoopToggle` parameter in your Unity project is set as a Boolean. If not, change the type accordingly.

## 3. Test On VRChat :3

### Step 1 : Enable OSC Server

→ Enable the OSC server in VRChat.

![Enable OSC](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/3411ea1b-76cd-4bc1-b9fe-a91c14ae7df7)
![OSC Server](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/78359d0e-7062-4bb9-b16a-b3816f448580)

### Step 2 : Run Your Code

→ Start your TikTok Live and run your Python program. You should see interactions reflected in your OSC Debug Panel.

![OSC Debug Panel](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/5b4cf95a-1ff3-4b30-a78a-72b157a58a08)
![Debug Panel](https://github.com/HyroeVRC/TiktokToOSC/assets/170990155/9524090b-ffe9-4c01-90c9-57908f367a52)

> Note : If it doesn't work for some people during your live, feel free to reach out for assistance!

Have a wonderful day/night !

→ Follow me on my socials:

- [TikTok](https://www.tiktok.com/@hyroe)
- [X](https://x.com/_Hyroe_)
- [Instagram](https://www.instagram.com/hyroevr/)

Boop from Hyroe :3
