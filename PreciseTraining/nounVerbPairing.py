import coreFunctions

#junk below
allFill = coreFunctions.loadText(r'Brute-Gen-main\PreciseTraining\PreciseStorage\NounVerbPairs.txt') # words that been paired already
nonFill = coreFunctions.loadText(r'Brute-Gen-main\PreciseTraining\PreciseStorage\NounVerbNonPairs.txt')
fill = allFill+nonFill

Pairtxt = (r'Brute-Gen-main\PreciseTraining\PreciseStorage\NounVerbPairs.txt')
Nonpairtxt = (r'Brute-Gen-main\PreciseTraining\PreciseStorage\NounVerbNonPairs.txt')

nounPhrases = ["$person","$job","$place","$obj","$activity"]
verbPhrases = ["$past","$present","$future"]

nounsBef = coreFunctions.loadText(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseNoun.txt')
verbsBef = coreFunctions.loadText(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseVerb.txt')

nouns = coreFunctions.preciseClearing(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseNoun.txt', nounsBef, nounPhrases) #Txt, words, list of phrases to be removed
verbs = coreFunctions.preciseClearing(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseVerb.txt', verbsBef, verbPhrases)
print("Time to pair nouns and verbs. Ensure that noun training and verb training has already went underway!")

pairs = []
nonpairs = []

for noun in nouns:
    for verb in verbs:
        chk = False
        temp = noun+"$"+verb
        for i in fill:
            if i == temp:
                chk = True
                
        if chk == False:
            print("---------------------------------------------------------------------")
            print("Does the noun \""+noun+"\" pairing with the verb \""+verb+"\" make grammatical sense?")
            print("y/n")
            print("---------------------------------------------------------------------")
            
            ans = input()
            if ans == "y":
                pairs.append(noun+"$"+verb)
            if ans == "n":
                nonpairs.append(noun+"$"+verb)

coreFunctions.updateTxt(Pairtxt,pairs)
coreFunctions.updateTxt(Nonpairtxt,nonpairs)

print("Pairing complete.")
