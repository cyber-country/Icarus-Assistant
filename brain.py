from file_handler import model
def temperature():
    return "The current temperature is 40 degree celcius"

def greet():
    return "Hello sir"

def time():
    return "the time is now 3:40 pm sir"

def reciver(n):
    output = []
    
    book = {
        "hello": greet,
        "time": time,
        "temperature": temperature
    }
    
    for i in book:
        if i in n:
            output.append(book[i]())  # call function here
    if "open" in n:
        model.reciver(n)
    return ", ".join(output)