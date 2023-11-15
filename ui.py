from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_txt = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=right_img, highlightthickness=0)
        self.right.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_img, highlightthickness=0)
        self.wrong.grid(row=2, column=1)

        # scoreboard
        self.score_label = Label(text="Score: 0", foreground="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_questions()

        self.window.mainloop()

    def get_next_questions(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_txt, text=q_text)
