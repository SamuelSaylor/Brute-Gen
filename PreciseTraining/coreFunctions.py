def loadText(ty): #reads files and converts to lists
    x = []
    with open(ty,"r") as file:
        content = file.read()
        words = content.split(",")
        
        for i in words:
            x.append(i)
            print(i)

    return x

def write(txt,arr): #updates savefiles
    msg = ""
    for i in arr:
        msg = msg+i+"," #data is stored like this in WordStorage
    
    with open(txt,"w") as file:
        file.write(msg)
