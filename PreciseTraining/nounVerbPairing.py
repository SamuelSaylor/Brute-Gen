import coreFunctions

nounPhrases = ["$person","$job","$place","$obj","$activity"]
verbPhrases = ["$past","$present","$future"]

nounsBef = coreFunctions.loadText(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseNoun.txt')
verbsBef = coreFunctions.loadText(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseVerb.txt')

nouns = coreFunctions.preciseClearing(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseNoun.txt', nounsBef, nounPhrases) #Txt, words, list of phrases to be removed
verbs = coreFunctions.preciseClearing(r'Brute-Gen-main\PreciseTraining\PreciseStorage\PreciseVerb.txt', verbsBef, verbPhrases)
print("Time to pair nouns and verbs. Ensure that noun training and verb training has already went underway!")
