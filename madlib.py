print("""
      
Mad Libs Summer Trip Story (Funny)
By Scr1pt.gg
 
 """)

# Ask users for nouns
NOUN = input("Please enter an noun: ")
NOUN1 = input("Please enter your second noun: ")
NOUN2 = input("Please enter your third noun: ")
NOUN3 = input("Please enter your fourth noun: ")
NOUN4 = input("Please enter your final noun: ")

# Ask users for adjectives
ADJECTIVE = input("Please enter an adjective: ")
ADJECTIVE1 = input("Please enter a 2nd adjective: ")

# Ask users for verbs ending in -ing
INGVERB1 = input("Please enter your first ING-verb: ")
INGVERB2 = input("Please enter your second ING-verb: ")
INGVERB3 = input("Please enter your third ING-verb: ")
INGVERB4 = input("Please enter your final ING-verb: ")

# Ask users for a random plant
PLANT = input("Please enter a random plant: ")

# Ask users for random part of body
PARTOFBODY = input("Please enter a random part of the body: ")

# Ask users for favorite place
PLACE1 = input("Please enter your favorite place: ")

# Ask users for random number make sure it does not throw error 
# if they enter a float by converting to an integer
NUMBER1 = input(int("Please enter a random number: "))

# Ask users for plural nouns
PLURALNOUN = input("Please enter your first plural noun: ")
PLURALNOUN1 = input("Please enter your second plural noun: ")
PLURALNOUN2 = input("Please enter your third and final plural noun: ")

# Prints Mad Lib
print(f"A vacation is when you take a trip to some {NOUN} with your {ADJECTIVE} family.")
print(f" Usually you go to some place that is near a/an {NOUN1} or up on a/an {NOUN2}.")
print(f" A good vacation place is one where you can ride (a) {PLURALNOUN}.\n I like to spend my time {INGVERB1} or {INGVERB2}")
print(f" When parents go on a vacation, they spend their time eating three {PLURALNOUN1} \n a day, and fathers play {NOUN3}.")
print(f" Mothers sit around {INGVERB3}. Last summer, my little brother fell in a/an {NOUN4}\n and got poison {PLANT} all over his {PARTOFBODY}.")
print(f" My family is going to go to (the) {PLACE1}, and I will practice {INGVERB4}.")
print(f"Parents need vacations more than kids because parents are always very {ADJECTIVE1},\n and because they have to work {NUMBER1} hours every day all year making enough\n {PLURALNOUN2} to pay for the vacation.")