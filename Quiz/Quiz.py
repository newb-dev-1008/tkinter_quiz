from tkinter import *

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Correct Answer!")
            right += 1
        else:
            label = Label(view, text="Wrong Answer.")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + "\n questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions_1 = ["What are enzymes made of?",
             "What is an active site?",
             "Why are enzymes known as biological catalysts?",
             "Cell Membrane is primarily constructed of what type of molecule?",
             "Which of the statements is not true for mitochondria?"]

options = [["Sugar", "Globular Protein", "Amino Acids", "Carbohydrates"],
           ["It produces sugar", "It's a part of the enzyme that the substrate binds to", "It is a part of the enzyme that slows down the reaction", "The active site produces oxygen"],
           ["They increase the rate of the chemical reaction", "They decrease the rate of the chemical reaction", "They do not affect the rate of the chemical reaction", "They may either increase or decrease the rate, depending on temperature"],
           ["Cytoplasm", "Phosphoric Acid", "Phospholipids", "Cells"],
           ["They can't replicate", "They contain DNA", "They can live freely outside the cell", "They can produce their own protein"]]

correct_answers = ["C", "B", "A", "C", "C"]

questions = []
for i in range(len(questions_1)):
    questionString = questions_1[i]
    answers = []
    for j in range(4):
        answers.append(options[i][j])
    correctLetter = correct_answers[i]
    questions.append(Question(questionString, answers, correctLetter))
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()

window.title("Quiz Window")
window.geometry("500x500")
window.config(background = "#ffffff")
window.resizable(0,0)

label_heading = Label(
    window,
    text = "QUIZ",
    font = ("Times New Roman", 24, "bold"),
    background = "#ffffff"
    )
label_heading.pack()

Label(window, text="Enter your username:", font = ("Times New Roman", 18, "bold"), background = "#ffffff").pack(padx = 10, pady = 50)

Text(window, height = 1, width = 30).pack(padx = 10, pady = 5)

button = Button(
    window,
    text = "Start Quiz",
    font = ("Times New Roman", 16),
    relief = FLAT,
    border = 0,
    command = askQuestion
    )
button.pack(padx = 10, pady = 50)
window.mainloop()
