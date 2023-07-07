# High Scores
highScores = [
  {"score":19,"Name":"Billy"},
  {"score":40,"Name":"Tommy"},
  {"score":11,"Name":"Ronny"},
  {"score":29,"Name":"Timmy"},
  {"score":2,"Name":"Jimmy"}
]

# high scores variable to sort scores in order
def scoreSort(highScores):
  return highScores["score"]

# sorted highscores
highScores = sorted(highScores, key=scoreSort)

# Quiz Questions & Answers
quizQs = [
  {
    "question": "What year was the Premier League founded? ",
    "answer": "1992"
  },
  {
    "question": "Who has won the most Premier League titles? ",
    "answer": "Manchester United"
  },
  {
    "question": "Who holds the record for most Premier League hat-tricks? ",
    "answer": "Alan Shearer"
  },
  {
    "question": "Who holds the record for most Premier League wins as a manager? ",
    "answer": "Sir Alex Ferguson"
  },
  {
    "question": "Who holds the record for most Premier League red cards? ",
    "answer": "Patrick Vieira"
  },
]

# Variables for calculating prize money
prizePerCorrectAnswer = 200000

# Welcome Message
print(
  "Welcome to Who Wants to be a Millionaire!" + "\n" +
  "There are 5 questions to answer and each correct answer is worth £200,000."
  + "\n" + "Good Luck!" + "\n")


playAgain = "yes"

# While loop start for the quiz
while playAgain.lower() == "yes":
  userName = input("Please enter your name: " + "\n")
  correctAnswers = 0

  # for loop to run through the 5 questions
  for i in range(5):
    answer = input("\n"+quizQs[i]["question"])
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




