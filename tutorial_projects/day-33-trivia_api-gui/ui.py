from tkinter import *

from quiz_brain import QuizBrain
from styles import Styles


class QuizInterface(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        # Non-UI properties
        self.quiz = quiz_brain

        # UI
        self.styles = Styles()
        self.title("Quizzler")
        self.config(**self.styles.window)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # CREATE WIDGETS
        self.score_label = Label(self, **self.styles.score)
        self.question_canvas = Canvas(self, **self.styles.question_canvas_default)
        self.question_text = self.question_canvas.create_text(self.styles.question_canvas_default["width"] / 2,
                                                              self.styles.question_canvas_default["height"] / 2,
                                                              **self.styles.question_text)
        correct_image = PhotoImage(**self.styles.correct_button_image)
        self.correct_button = Button(image=correct_image, **self.styles.correct_button, command=self.correct_button_click)
        wrong_image = PhotoImage(**self.styles.wrong_button_image)
        self.wrong_button = Button(image=wrong_image, **self.styles.wrong_button, command=self.wrong_button_click)

        # ARRANGE WIDGETS
        self.score_label.grid(column=1, row=0)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.correct_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        self.next_question()

        self.mainloop()

    def correct_button_click(self):
        is_correct = self.quiz.check_answer(True)
        self.give_feedback(is_correct)

    def wrong_button_click(self):
        is_correct = self.quiz.check_answer(False)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
        if is_correct:
            self.question_canvas.config(**self.styles.question_canvas_correct_feedback)
        else:
            self.question_canvas.config(**self.styles.question_canvas_wrong_feedback)
        self.after(1500, self.next_question)

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def next_question(self):
        self.question_canvas.config(self.styles.question_canvas_default)
        if self.quiz.still_has_questions():
            self.update_score_label()
            next_question = self.quiz.get_next_question()
            self.question_canvas.itemconfig(self.question_text, text=f"{next_question}")
            self.correct_button.config(state="active")
            self.wrong_button.config(state="active")
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.")
