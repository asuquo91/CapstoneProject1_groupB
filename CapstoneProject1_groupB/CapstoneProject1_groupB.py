
# High Scores
highScores = [
  {"score":180,"Name":"Billy"},
  {"score":90,"Name":"Tommy"},
  {"score":150,"Name":"Ronny"},
  {"score":60,"Name":"Timmy"},
  {"score":80,"Name":"Jimmy"}
]

# high scores variable to sort scores in order
def scoreSort(highScores):
  return highScores["score"]

# sorted highscores
highScores = sorted(highScores, key=scoreSort)

# Quiz Questions & Answers
quizQs = [
  # Question 1
  {
    "question": "What year was the Premier League founded?\nA: 1992 B:1985 \n",
    "answer": "A",
    "questionMed": "What year was the Premier League founded?\nA: 1999 B:1985 \nC: 1993 D: 1992 \n",
    "answerMed": "D",
    "questionHard": "What year was the Premier League founded?\nA: 1999 B:1985 \nC: 1993 D: 2000 \nE: 2005 F:1992\n",
    "answerHard": "F"
  },
    # Question 2
  {
    "question": "Who has won the most Premier League titles?\nA: Chelsea B: Manchester United\n",
    "answer": "b",
    "questionMed": "Who has won the most Premier League titles?\nA: Chelsea B: Manchester City\nC: Liverpool D: Manchester United\n",
    "answerMed": "D",
    "questionHard": "Who has won the most Premier League titles?\nA: Chelsea B: Manchester City\nC: Liverpool D: Manchester United\nE: Arsenal F:Chelsea\n",
    "answerHard": "D"
  },
    # Question 3
  {
    "question": "Who holds the record for most Premier League hat-tricks?\nA: Alan Shearer B: Wayne Rooney \n",
    "answer": "a",
    "questionMed": "Who holds the record for most Premier League hat-tricks?\nA: Erling Haaland B: Wayne Rooney \nC: Alan Shearer D: Didier Drogba\n",
    "answerMed": "C",
    "questionHard": "Who holds the record for most Premier League hat-tricks?\nA: Erling Haaland B: Alan Shearer \nC: Wayne Rooney D: Didier Drogba\nE: Harry Kane F: Thierry Henry\n",
    "answerHard": "B"
  },
    # Question 4
  {
    "question": "Who holds the record for most Premier League wins as a manager?\nA: Jose Mourhinio B: Sir Alex Ferguson\n",
    "answer": "b",
    "questionMed": "Who holds the record for most Premier League wins as a manager?\nA: Jose Mourhinio B: Harry Rednapp\nC: Pep Guardiola D: Sir Alex Ferguson\n",
    "answerMed": "D",
    "questionHard": "Who holds the record for most Premier League wins as a manager?\nA: Jose Mourhinio B: Harry Rednapp\nC: Pep Guardiola D: Arsene Wenger \nE: Sir Alex Ferguson F: Jurgen Klopp\n",
    "answerHard": "E"
  },
    # Question 5
  {
    "question": "Who holds the record for most Premier League red cards?\nA: Patrick Vieira B: Roy Keane \n",
    "answer": "a",
    "questionMed": "Who holds the record for most Premier League red cards?\nA: Patrick Vieira B: Roy Keane \nC: Duncan Ferguson D: Joey Barton\n",
    "answerMed": "a",
    "questionHard": "Who holds the record for most Premier League red cards?\nA: Joey Barton  B: Roy Keane \nC: Duncan Ferguson D: Patrick Vieira\nE: John Terry F: Vinnie Jones\n",
    "answerHard": "D"
  },
    # Question 6
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 7
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 8
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 9
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 10
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 11
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 12
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 13
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 14
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 15
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 16
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 17
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 18
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 19
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
    # Question 20
  {
    "question": "?\nA:  B:  \n",
    "answer": "a",
    "questionMed": "?\nA:  B:  \nC:  D: \n",
    "answerMed": "C",
    "questionHard": "?\nA:  B:  \nC:  D: \nE:  F: \n",
    "answerHard": "F"
  },
]

# user difficulty
userDifficulty = "easy"

# Welcome Message
print("Welcome to Capstone Quiz Master, the ultimate quiz game that will test your knowledge!\nWith 20 questions of varying difficulty, this game is designed for players of all backgrounds.\n")
print("There are three difficulty ratings: Easy, Medium, and Hard. Each question has a point value: Easy (5 points), Medium (8 points), and Hard (10 points).\n")
print("To answer a question please type the Letter next to the answer. E.g. if the answer was C: 200 then type 'C'.\n")
print("Think you can conquer Capstone Quiz Master? Gather your friends, family, or fellow trivia enthusiasts and let the challenge begin!\nShow off your knowledge, aim for high scores, and become the ultimate quiz master!\n")


# play again status
playAgain = "yes"

# While loop start for the quiz
while playAgain.lower() == "yes":
  userName = input("Please enter your name: " + "\n")
  userDifficulty = input("Please enter your difficulty: Easy, Medium or Hard " + "\n")

  correctAnswers = 0
  playerScore = 0
  

  # for loop to run through the 20 questions
  for i in range(20):

      # easy difficulty loop
    if userDifficulty.lower() == "easy":
      answer = input("\n"+quizQs[i]["question"])

      if answer.lower() == str(quizQs[i]["answer"]).lower():
        print("\n" + "Congratulations that is correct!" + "\n")
        correctAnswers += 1
        playerScore += 5
      else:
        print("\n" + "That is incorrect!" + "\n")

        # Medium difficulty loop
    elif userDifficulty.lower() == "medium":
      answer = input("\n"+quizQs[i]["questionMed"])

      if answer.lower() == str(quizQs[i]["answerMed"]).lower():
        print("\n" + "Congratulations that is correct!" + "\n")
        correctAnswers += 1
        playerScore += 8
      else:
        print("\n" + "That is incorrect!" + "\n")

        # Hard difficulty loop
    elif userDifficulty.lower() == "hard":
      answer = input("\n"+quizQs[i]["questionHard"])

      if answer.lower() == str(quizQs[i]["answerHard"]).lower():
        print("\n" + "Congratulations that is correct!" + "\n")
        correctAnswers += 1
        playerScore += 10
      else:
        print("\n" + "That is incorrect!" + "\n")    

  # total score and prize money print statement
  print(f"You scored {correctAnswers} out of 20.\n")
  

  # Update high scores
  if playerScore > highScores[0]["score"]:
    print("Congratulations you made it onto the Leaderboard!\n")
    highScores[0]["Name"] = userName
    highScores[0]["score"] = playerScore
    highScores = sorted(highScores, key=scoreSort)

  # displays updated leaderboard
  print(f"LeaderBoard:\n1st Place = {highScores[-1]['Name']}:\t {highScores[-1]['score']}")
  print(f"2nd Place = {highScores[-2]['Name']}:\t {highScores[-2]['score']}")
  print(f"3rd Place = {highScores[-3]['Name']}:\t {highScores[-3]['score']}")
  print(f"4th Place = {highScores[-4]['Name']}:\t {highScores[-4]['score']}")
  print(f"5th Place = {highScores[-5]['Name']}:\t {highScores[-5]['score']}")
  

  # Question to check if player wants to play again
  playAgain = input("\nWould you like to play again? (Yes or No): ")

  #Displays a thank you message if the player doesn't want to play again
if playAgain.upper() == "NO":
  print("\n"+"Thank you for Playing!")  




