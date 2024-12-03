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
      
def updateTxt(txt,arr): # Write but different
    msg = ""
    for i in arr:
        msg = msg+i+","
        
    with open(txt,"a") as file:
        file.write(","+msg)
    
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
        return fart
                    
def antiduplicates(oldArr,upd):
    trash = []
    updArr = upd
    
    for i in updArr: #gets rid of words that are already stored
        chk = False
        for x in oldArr:
            if i == x:
                chk = True
        if chk == True:
            trash.append(i)
  
    for i in trash:
        for x in updArr:
            if i == x:
                updArr.remove(x)
    
    return updArr
