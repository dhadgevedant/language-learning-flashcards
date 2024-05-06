import tkinter as tk
import csv
import random


class VocabularyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Marathi to English Vocabulary Learning')
        self.root.attributes('-fullscreen', True)  # Set fullscreen mode
        self.root.configure(bg='#f5f5f5')  # Set background color

        # Load vocabulary from CSV
        self.words = self.load_vocabulary('English_to_Marathi.csv')

        # Display words to be learned today
        self.display_learning_words()

    def load_vocabulary(self, file_path):
        words = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                words.append((row[0], row[1]))
        return words

    def display_learning_words(self):
        self.learning_words = random.sample(self.words, 4)  # Store words to be learned

        # Initialize variables
        self.current_index = 0
        self.score = 0

        # Display words to be learned today
        self.learning_frame = tk.Frame(self.root, bg='#f5f5f5')
        self.learning_frame.pack(expand=True, fill = 'both', pady=100, padx = 500)

        learning_label = tk.Label(self.learning_frame, text='आज तुम्ही शिकाल...', font=('Arial', 36, 'bold'), bg='#f5f5f5', fg='#333333')
        learning_label.pack(pady=30)

        for word in self.learning_words:
            word_label = tk.Label(self.learning_frame, text=f'{word[0]} - {word[1]}', font=('Arial', 28), bg='#f5f5f5', fg='#333333')
            word_label.pack()

        start_button = tk.Button(self.learning_frame, text="सुरू करा", font=('Arial', 30, 'bold'), bg='#4CAF50', fg='#ffffff', command=self.start_learning)
        start_button.pack(pady=50)

    def start_learning(self):
        # Destroy the learning words display
        self.learning_frame.destroy()

        # Display question
        self.display_question()

    def display_question(self):
        if self.current_index < 4:  # Limit to 4 questions
            
            global word
            word, correct_translation = self.learning_words[self.current_index]
            
            # Create card-like question frame
            question_frame = tk.Frame(self.root, bg='#f0f0f0')  # Off-white background color
            question_frame.pack(expand=True, fill='both', padx=50, pady=100)

            # Display question
            question_label = tk.Label(question_frame, text=f'"{word}" ला मराठीत काय म्हणतात?', font=('Arial', 36), bg='#f0f0f0', fg='#333333')
            question_label.pack(pady=20)

            

            # Create options frame
            options_frame = tk.Frame(question_frame, bg='#f0f0f0')
            options_frame.pack(expand=True, fill='both', pady=20)

            # Display options
            options = self.get_mcq_options(correct_translation)
            num_options = len(options)
            for i, option in enumerate(options):
                row = i // 2
                col = i % 2
                button = tk.Button(options_frame, text=option, font=('Arial', 24), bg='#4CAF50', fg='#ffffff', padx=20, pady=10, command=lambda selected_option=option: self.check_mcq_answer(selected_option, correct_translation, question_frame))
                button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            options_frame.grid_columnconfigure((0, 1), weight=1)
            options_frame.grid_rowconfigure(tuple(range((num_options + 1) // 2)), weight=1)
        else:
            self.display_score()
        

    def get_mcq_options(self, correct_translation):
        options = [correct_translation]
        while len(options) < 4:
            random_word = random.choice(self.words)[1]
            if random_word not in options:
                options.append(random_word)
        random.shuffle(options)
        return options

    def check_mcq_answer(self, selected_option, correct_translation, question_frame):
        if selected_option == correct_translation:
            self.score += 1
            result_text = "Correct!"
        else:
            result_text = f"Incorrect! The correct answer is: {correct_translation}"

        # Display result
        result_label = tk.Label(question_frame, text=result_text, font=('Arial', 30, 'bold'), bg='#f0f0f0', fg='#333333')
        result_label.pack(pady=30)

        # Destroy question frame after a delay
        self.root.after(0, lambda: question_frame.destroy())

        # Move to the next question
        self.current_index += 1
        self.display_question()
          

    def display_score(self):
        # Destroy previous question frame
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display score
        score_label = tk.Label(self.root, text=f'Your score: {self.score}/{len(self.learning_words)}', font=('Arial', 36, 'bold'), bg='#f5f5f5', fg='#333333')
        score_label.pack(pady=100)

        # Create Try Again button
        try_again_button = tk.Button(self.root, text="Try Again", font=('Arial', 30), bg='#4CAF50', fg='#ffffff', command=self.try_again)
        try_again_button.pack(pady=20)

        # Create Quit button
        quit_button = tk.Button(self.root, text="Quit", font=('Arial', 30), bg='#ff0000', fg='#ffffff', command=self.root.destroy)
        quit_button.pack(pady=20)

    def try_again(self):
        self.current_index = 0
        self.score = 0
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear score and buttons
        self.display_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#f5f5f5')  # Set background color
    app = VocabularyApp(root)
    
    root.mainloop()
