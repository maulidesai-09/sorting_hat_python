import time
import random
import fontstyle

### list of houses in string format
houses = [fontstyle.apply("GRYFFINDOR", "red/ bold"), 
          fontstyle.apply("SLYTHERIN", "green/ bold"), 
          fontstyle.apply("HUFFLEPUFF", "yellow/ bold"), 
          fontstyle.apply("RAVENCLAW", "blue/ bold")]


### list #1 of expressions to print to show sorting hat is processing
expressions_1 = [fontstyle.apply("\"interesting...\"", "italic"), 
               fontstyle.apply("\"slightly tricky...\"", "italic")]

### list #1 of expressions to print to show sorting hat is processing
expressions_2 = [fontstyle.apply("\"let's see... not a bad mind either...\"", "italic"),
                 fontstyle.apply("\"let's see... there's also talent...\"", "italic"),
                 fontstyle.apply("\"let's see... not a bad choice of instrument either\"",                   "italic")]


### variables to track score of each house
gryffindor = 0
slytherin = 0
hufflepuff = 0
ravenclaw = 0



def welcome():
  """ Prints welcome note """
  
  welcome = [
    "WELCOME TO HOGWARTS!", 
    " ",
    "The start-of-term banquet will begin shortly, but before you take your seats in the",       "Great Hall, you will be sorted into your houses. The Sorting is a very important",
    "ceremony because, while you are here, your house will be something like your",
    "family within Hogwarts.",
    "",
    f"The four houses are called {houses[0]}, {houses[1]}, {houses[2]} and {houses[3]}.", 
    "",
    "Each house has its own noble history and each has produced outstanding witches and",
    "wizards."
    ]
  for greetings in welcome:
    print(greetings)
    time.sleep(1)
  
  print()



def instructions():
  """ Prints welcome instructions """
  
  instructions = [
    "Like most things, we have had to make the Sorting Hat ceremony virtual to keep up",
    "with the times! ;) So, instead of wearing the Magical Hat, take the following quiz",
    "to help the Sorting Hat sort you into your house.", 
    " ",
    "Each question will have 4 options - 'A', 'B', 'C' and 'D'. Pick the option you",           "resonate with the most and the Hat will do the rest!",
    " ", 
  "In the original words of the Sorting Hat:",
  fontstyle.apply("\"There’s nothing hidden in your head", "italic"),
  fontstyle.apply(" The Sorting Hat can’t see,", "italic"),
  fontstyle.apply(" So try me on and I will tell you", "italic"),
  fontstyle.apply(" Where you ought to be.\"", "italic")
  ]
  for lines in instructions:
    print(lines)
    time.sleep(1)
  
  print()



def increase_gryffindor():
  """ increments score for gryffindor """
  global gryffindor
  gryffindor += 1

def increase_slytherin():
  """ increments score for slytherin """
  global slytherin
  slytherin += 1

def increase_hufflepuff():
  """ increments score for hufflepuff """
  global hufflepuff
  hufflepuff += 1

def increase_ravenclaw():
  """ increments score for ravenclaw  """
  global ravenclaw
  ravenclaw  += 1



### list of questions in string format
questions = [
 "If you could have any power, which would you choose? \n (A) The power of invisibility  \n (B) The power to change your appearance at will  \n (C) The power to speak to animals  \n (D) The power to read minds",
  
 "Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you, it would smell of:  \n (A) The sea  \n (B) Home  \n (C) Fresh parchment  \n (D) A crackling log fire",
  
 "Out of the following, which musical instrument would you pick?  \n (A) Trumpet  \n (B) Piano  \n (C) Drums  \n (D) Violin",
  
 "Which one of the following elements is most appealing to you?  \n (A) Air  \n (B) Fire  \n (C) Water  \n (D) Earth",
  
 "How do your friends describe you? \n (A) Patient \n (B) Brave and Reckless \n (C) Witty \n (D) Mysterious"
]


### list of options for each of the 5 questions - Separate dictionaries created to save options for each question and the dictionaries are then saved in a list. 
options = [
{"A": increase_gryffindor, "B": increase_slytherin, "C": increase_hufflepuff, "D": increase_ravenclaw},
{"A": increase_slytherin, "B": increase_hufflepuff, "C": increase_ravenclaw, "D": increase_gryffindor},
{"A": increase_hufflepuff, "B": increase_ravenclaw, "C": increase_gryffindor, "D": increase_slytherin},
{"A": increase_ravenclaw, "B": increase_gryffindor, "C": increase_slytherin, "D": increase_hufflepuff},
{"A": increase_hufflepuff, "B": increase_gryffindor, "C": increase_ravenclaw, "D": increase_slytherin}
]



def ask_questions():
  """ prints questions, asks for user input and verifies input """
  
  for i, question in enumerate(questions):
    print(question)
    print()
    while True:
      answer = input("> ")
      answer = answer.upper()
      if answer == "A" or answer == "B" or answer == "C" or answer == "D":
        break
      else:
        print("Please enter a valid input")
    options[i][answer]()
    print()



def processing_expressions():
  """ prints expressions to show sorting hat is processing """
  
  time.sleep(1)
  print("The Sorting Hat is processing: ")
  print()
  time.sleep(1)
  print(fontstyle.apply("\"hmmmm....\"", "italic"))
  print()
  time.sleep(2)
  print(fontstyle.apply("\"where should I place you...\"", "italic"))
  print()
  time.sleep(2)
  print(random.choice(expressions_1))
  print()
  time.sleep(2)
  print(random.choice(expressions_2))
  print()
  time.sleep(3)



def calculate_score():
  """ calculates final score and determines winner """
  
  scores = [gryffindor, slytherin, hufflepuff, ravenclaw]
  winner_score = max(scores)
  winner_index = scores.index(winner_score)
  winner = (houses[winner_index])
  processing_expressions()
  print("The Sorting Hat has spoken!")
  print (f"Congratulations! You have been sorted into {winner}!")
  print (f"Hope you have a magical time at Hogwarts as a {winner}! ")
  return winner



def play_quiz():
  """ starts game play"""
  
  welcome()
  print()
  instructions()
  print()
  start = input("Whenever you are ready, press RETURN to commence the Sorting Ceremony! ")
  print()
  ask_questions()
  calculate_score()

play_quiz()