


# High Scores
highScores = [
  {"score":60,"Name":"Billy"},
  {"score":40,"Name":"Tommy"},
  {"score":35,"Name":"Ronny"},
  {"score":10,"Name":"Timmy"},
  {"score":45,"Name":"Jimmy"}
]

# high scores variable to sort scores in order
def scoreSort(highScores):
  return highScores["score"]

# sorted highscores
highScores = sorted(highScores, key=scoreSort)

# Quiz Questions & Answers
quizQs = [
  {
    "question": "What year was the Premier League founded?\nA: 1992 B:1985 \n",
    "answer": "A",
    "questionMed": "C: 1993 D: 1999 \n",
    "questionHard": "E: 2005 F:1995\n"
  },
  {
    "question": "Who has won the most Premier League titles?\nA: Chelsea B: Manchester United\n",
    "answer": "b",
    "questionMed": "C: Liverpool D: Manchester City\n",
    "questionHard": "E: Arsenal F:Chelsea\n"
  },
  {
    "question": "Who holds the record for most Premier League hat-tricks?\nA: Alan Shearer B: Wayne Rooney \n",
    "answer": "a",
    "questionMed": "C: Erling Haaland D: Didier Drogba\n",
    "questionHard": "E: Harry Kane F: Thierry Henry\n"
  },
  {
    "question": "Who holds the record for most Premier League wins as a manager?\nA: Jose Mourhinio B: Sir Alex Ferguson\n",
    "answer": "b",
    "questionMed": "C: Pep Guardiola D: Harry Rednapp\n",
    "questionHard": "E: Arsene Wenger F: Jurgen Klopp\n"
  },
  {
    "question": "Who holds the record for most Premier League red cards?\nA: Patrick Vieira B: Roy Keane \n",
    "answer": "a",
    "questionMed": " C: Duncan Ferguson D: Joey Barton\n",
    "questionHard": " E: John Terry F: Vinnie Jones\n"
  },
]

# user difficulty
userDifficulty = "easy"

# Variables for calculating prize money
prizePerCorrectAnswer = 200000

# Welcome Message
print(
  "Welcome to Who Wants to be a Millionaire!" + "\n" +
  "There are 5 questions to answer and each correct answer is worth £200,000." + "\n" + "Good Luck!" + "\n")

# play again status
playAgain = "yes"

# While loop start for the quiz
while playAgain.lower() == "yes":
  userName = input("Please enter your name: " + "\n")
  userDifficulty = input("Please enter your difficulty: Easy, Medium or Hard " + "\n")

  correctAnswers = 0
  

  # for loop to run through the 5 questions
  for i in range(5):

      # easy difficulty loop
    if userDifficulty.lower() == "easy":
      answer = input("\n"+quizQs[i]["question"])

      if answer.lower() == str(quizQs[i]["answer"]).lower():
        print("\n" + "Congratulations that is correct!" + "\n")
        correctAnswers += 10
      else:
        print("\n" + "That is incorrect!" + "\n")

        # Medium difficulty loop
    elif userDifficulty.lower() == "medium":
      answer = input("\n"+quizQs[i]["question"]+ quizQs[i]["questionMed"])

      if answer.lower() == str(quizQs[i]["answer"]).lower():
        print("\n" + "Congratulations that is correct!" + "\n")
        correctAnswers += 10
      else:
        print("\n" + "That is incorrect!" + "\n")

        # Hard difficulty loop
    elif userDifficulty.lower() == "hard":
      answer = input("\n"+quizQs[i]["question"]+ quizQs[i]["questionMed"]+ quizQs[i]["questionHard"])

      if answer.lower() == str(quizQs[i]["answer"]).lower():
        print("\n" + "Congratulations that is correct!" + "\n")
        correctAnswers += 10
      else:
        print("\n" + "That is incorrect!" + "\n")    

  # total score and prize money print statement
  print(
    f"You scored {int(correctAnswers/10)} out of 5. Congratulations!!!! Your total prize money is £{correctAnswers * prizePerCorrectAnswer}. "
  )

  # Update high scores
  if correctAnswers > highScores[0]["score"]:
    highScores[0]["Name"] = userName
    highScores[0]["score"] = correctAnswers
    highScores = sorted(highScores, key=scoreSort)

  # displays updated leaderboard
  print(f"LeaderBoard:\n1st Place = {highScores[-1]['Name']}:\t {highScores[-1]['score']}")
  print(f"2nd Place = {highScores[-2]['Name']}:\t {highScores[-2]['score']}")
  print(f"3rd Place = {highScores[-3]['Name']}:\t {highScores[-3]['score']}")
  print(f"4th Place = {highScores[-4]['Name']}:\t {highScores[-4]['score']}")
  print(f"5th Place = {highScores[-5]['Name']}:\t {highScores[-5]['score']}")
  

  # Question to check if player wants to play again
  playAgain = input("Would you like to play again? (Yes or No): ")

  #Displays a thank you message if the player doesn't want to play again
if playAgain.upper() == "NO":
  print("\n"+"Thank you for Playing!")




