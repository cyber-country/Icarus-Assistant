import os
def edge():
    os.startfile("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
def valorant():
    os.startfile("C:/Riot Games/VALORANT/live/VALORANT.exe")
def notepad():
    os.startfile("C:/Program Files/WindowsApps/Microsoft.WindowsNotepad_11.2501.31.0_x64__8wekyb3d8bbwe/Notepad/Notepad.exe")
def reciver(command):
    book={"edge":edge,"valorant":valorant,"notepad":notepad}
    current_action=""
    target=[]
    if "open" in command:
        current_action="open"
    com=command.split(" ")
    for i in com:
        if i in book:
            target.append(i)
    for j in target:
        if current_action=="open":
            book[j]()