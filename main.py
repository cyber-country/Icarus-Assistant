import brain
#my main program which take user input/output
#Intro
print("\tThis is Icarus base model\t")
print("currently coded instruction with no algorithms")
while True:
    command=input("waiting for command..")
    result=""
    #command cleaning
    for i in command:
        if i.isalpha() or i==" ":
            result+=i
        else:
            continue
    command=result
    command=command.lower()
    if command=="exit":
        break
    output=brain.reciver(command)
    print(output)