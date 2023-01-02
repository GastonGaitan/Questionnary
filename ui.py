THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

from tkinter import *

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg="#B1DDC6")
        self.window.resizable(False, False)
        # Question display
        self.canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
        self.background = PhotoImage(file="images\\background.png")
        self.question_background = self.canvas.create_image(400, 263, image=self.background)
        self.score = 0
        self.canvas_score = self.canvas.create_text(680, 50, text=f"Score: {self.score}", font=('arial',20, 'bold'))
        self.canvas_question_text = self.canvas.create_text(400, 263, text="", font=('arial',20,'bold'), width=450)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.feedback = self.canvas.create_text(200, 50, text='', font=('arial', 20, 'bold'))
        # Buttons
        true_button_image = PhotoImage(file="images\\true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=lambda:self.give_feedback('True'))
        # lambda:self.quiz.check_answer('True')
        self.true_button.grid(column=0, row=1)
        wrong_button_image = PhotoImage(file="images\\false.png")
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=lambda:self.give_feedback('False'))
        # lambda:self.quiz.check_answer('False')
        self.wrong_button.grid(column=1,row=1)
        # Get question
        self.get_next_question()
        # Mainloop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.feedback, text="")
        self.true_button.config(state=NORMAL)
        self.wrong_button.config(state=NORMAL)
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question_text, text=q_text)
        except IndexError:
            self.canvas.itemconfig(self.feedback, text = "Questionary finished!")
            self.canvas.itemconfig(self.canvas_question_text, text = "")
            self.true_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)
    def give_feedback(self, *args):
        if len(args) > 0:
            user_answer = args[0]
            correct = self.quiz.check_answer(user_answer)
            if correct:
                print("That was right")
                self.canvas.itemconfig(self.feedback, text="Correct!")
                self.quiz.score += 1
                self.canvas.itemconfig(self.canvas_score, text=f"Score: {self.quiz.score}")
            else:
                self.canvas.itemconfig(self.feedback, text="Wrong")
        # Espero un tiempo y cambio la funcion
        self.true_button.config(state=DISABLED)
        self.wrong_button.config(state=DISABLED)
        self.window.after(1000, self.get_next_question)
        