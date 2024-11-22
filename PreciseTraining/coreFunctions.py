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
        
def preciseClearing(txt,arr,precisePhrases): # get precise data set up Nandiaondiownadioawndw
    precThrowaway = []
    x = []
    
    with open(txt,"r") as file:
        fart = file.read()

        for i in precisePhrases:
            fart = fart.replace(i,"")
        
        fart = fart.split(",")

        for i in fart:
            for x in arr:
                if x == i:
                    precThrowaway.append(i)
        
        for i in precThrowaway:
            for x in arr:
                if x == i:
                    arr.remove(x)
