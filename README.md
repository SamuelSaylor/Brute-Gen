# Brute-Gen
Started work 11/18/2024

Brute Gen is a small project of mine designed to generate simple sentences from words fed to it by users. As the title suggests, everything is bruteforced in.

Keep in mind this was made by a high schooler, bugs and errors might be prevalent.

# How to use:

# # Establishing words and their uses
1. Put in phrases, words, gibberish, basically whatever you want into Insertion.txt
2. Run training.py
3. Answer the questions regarding every unfamiliar word. Just answer "c" for conjugates, "n" for nouns, and so on.

Keep in mind that unanswered questions will just be ignored.

# # Additional training
Inside of the PreciseTraining folder, a couple programs can be used to do some more precise tasks. (Such as determining if a noun is a person, place, or a thing.)

Begin by filling in more information in **/PreciseTraining/nounstraining.py** and **/PreciseTraining/verbtraining.py** to be more precise on the functions of words. For example, in nounstraining.py you can choose if a noun is a person, place, activty, etc.

Head on over to **/PreciseTraining/nounVerbPairing.py** and choose which nouns would logically make sense in a sentence with verbs.
For example, you would _shoot_ a basketball, as that makes sense, but it's illogical to say you'd _kill_ a basketball. (Unless, of course, your basketball for some reason has life and is personified through your work.)
