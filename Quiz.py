import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['London', 'Berlin', 'Paris', 'Madrid'],
        'correct_answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Earth', 'Jupiter', 'Mars', 'Venus'],
        'correct_answer': 'Mars'
    },
    {
        'question': 'What is the largest mammal?',
        'options': ['Elephant', 'White Shark', 'Giraffe', 'Blue Whale'],
        'correct_answer': 'Blue Whale'
    },
    {
        'question': 'What is the chemical name of water?',
        'options': ['NaO2', 'H2O', 'CaO', 'O2'],
        'correct_answer': 'H2O'
    },
    {
        'question': 'What is the smallest mammal?',
        'options': ['Elephant', 'shrew', 'Giraffe', 'Blue Whale'],
        'correct_answer': 'shrew'
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.quiz = random.sample(quiz_questions, len(quiz_questions))
        self.current_question = 0
        self.user_answers = []
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)

        self.next_question_button = tk.Button(root, text="Next", font=("Arial", 12), state=tk.DISABLED, command=self.next_question)
        self.next_question_button.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12), state=tk.DISABLED, command=self.play_again)
        self.play_again_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.quiz):
            question = self.quiz[self.current_question]
            self.question_label.config(text=question['question'])
            options = question['options']
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.next_question_button.config(state=tk.DISABLED)
        else:
            self.show_results()

    def check_answer(self, choice):
        question = self.quiz[self.current_question]
        selected_option = question['options'][choice]
        if selected_option == question['correct_answer']:
            self.score += 1
        self.user_answers.append(selected_option)
        self.next_question_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.load_question()
        if self.current_question == len(self.quiz):
            self.next_question_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.current_question = 0
        self.user_answers = []
        self.score = 0
        self.load_question()
        self.play_again_button.config(state=tk.DISABLED)

    def show_results(self):
        result_message = f"Your Final Score: {self.score}/{len(self.quiz)}\n\n"
        for i, question in enumerate(self.quiz):
            result_message += f"Question {i + 1}: {question['question']}\n"
            result_message += f"Your Answer: {self.user_answers[i]}\n"
            result_message += f"Correct Answer: {question['correct_answer']}\n\n"
        result_message += "Play Again to retry."
        messagebox.showinfo("Quiz Results", result_message)
        self.next_question_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
