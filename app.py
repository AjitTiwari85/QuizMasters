from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define the quiz questions and answers
questions = [
    {
        'id': 1,
        'text': 'What is 2 + 2?',
        'choice_1': '3',
        'choice_2': '4',
        'choice_3': '5',
        'correct': '2',
    },
    {
        'id': 2,
        'text': 'What is 3 x 5?',
        'choice_1': '10',
        'choice_2': '15',
        'choice_3': '20',
        'correct': '2',
    },
    {
        'id': 3,
        'text': 'What is 30 - 5?',
        'choice_1': '10',
        'choice_2': '15',
        'choice_3': '25',
        'correct': '3',
    },
    {
        'id': 4,
        'text': 'What is 12 x 5?',
        'choice_1': '10',
        'choice_2': '60',
        'choice_3': '20',
        'correct': '2',
    },
    # Add more questions
]

@app.route('/')
def index():
    return render_template('quiz.html', questions=questions)

@app.route('/', methods=['POST'])
def quiz():
    score = 0
    for question in questions:
        user_answer = request.form['question_' + str(question['id'])]
        if user_answer == question['correct']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
