def loadText(ty): #reads files and converts to lists
    x = []
    with open(ty,"r") as file:
        content = file.read()
        words = content.split(",")
        
        for i in words:
            x.append(i)
            print(i)

    return x

def preciseWords(word,precise,txt): # For sorting words to be more precise, IE: football$activity, pizza$food
    pass