# quizGame.py
#
# Python Bootcamp Day 17 - Quiz Game
# Usage:
#      git@github.com:megler/Day17-Quiz-Game.git
#
# Marceia Egler October 12, 2021

from question_model import Question
from data import question_data
from quiz_brain import Quiz

#Quiz runs until end of questions right or wrong by design

question_bank = []
quiz = Quiz(question_bank)

for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
