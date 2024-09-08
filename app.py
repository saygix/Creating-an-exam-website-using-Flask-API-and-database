from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)

def add_sample_questions():
    questions = [
        {
            'question_text': 'What is the main goal of Artificial Intelligence?',
            'option_a': 'To mimic human intelligence',
            'option_b': 'To create better hardware',
            'option_c': 'To improve internet speed',
            'option_d': 'To enhance video quality',
            'correct_answer': 'A'
        },
        {
            'question_text': 'Which of the following is a type of machine learning?',
            'option_a': 'Network Learning',
            'option_b': 'Hardware Learning',
            'option_c': 'Supervised Learning',
            'option_d': 'Manual Learning',
            'correct_answer': 'C'
        },
        {
            'question_text': 'What does NLP stand for in AI?',
            'option_a': 'Neural Learning Programming',
            'option_b': 'Neural Language Programming',
            'option_c': 'Natural Learning Processing',
            'option_d': 'Natural Language Processing',
            'correct_answer': 'D'
        },
        {
            'question_text': 'Which algorithm is commonly used for classification tasks?',
            'option_a': 'Decision Trees',
            'option_b': 'Clustering',
            'option_c': 'Regression',
            'option_d': 'Dimensionality Reduction',
            'correct_answer': 'A'
        },
        {
            'question_text': 'What does the term "overfitting" mean in machine learning?',
            'option_a': 'Model performs well on training data but poorly on new data',
            'option_b': 'Model performs well on new data but poorly on training data',
            'option_c': 'Model performs equally well on both training and new data',
            'option_d': 'Model has low accuracy on all data',
            'correct_answer': 'A'
        },
        {
            'question_text': 'Which of the following is not a deep learning framework?',
            'option_a': 'TensorFlow',
            'option_b': 'Keras',
            'option_c': 'PyTorch',
            'option_d': 'Scikit-learn',
            'correct_answer': 'D'
        },
        {
            'question_text': 'What is the purpose of a neural network?',
            'option_a': 'To store large amounts of data',
            'option_b': 'To perform arithmetic calculations',
            'option_c': 'To learn patterns and make predictions',
            'option_d': 'To improve battery life',
            'correct_answer': 'C'
        },
        {
            'question_text': 'Which AI concept involves creating models that can improve themselves over time?',
            'option_a': 'Data Mining',
            'option_b': 'Machine Learning',
            'option_c': 'Data Analysis',
            'option_d': 'Information Retrieval',
            'correct_answer': 'B'
        },
        {
            'question_text': 'What is the Turing Test used for?',
            'option_a': 'To determine if a machine can exhibit intelligent behavior',
            'option_b': 'To test the speed of computer hardware',
            'option_c': 'To measure network performance',
            'option_d': 'To evaluate user interface design',
            'correct_answer': 'A'
        },
        {
            'question_text': 'What is a common application of AI in the field of healthcare?',
            'option_a': 'Web development',
            'option_b': 'Hardware manufacturing',
            'option_c': 'Telecommunications',
            'option_d': 'Medical image analysis',
            'correct_answer': 'D'
        }
    ]

    for q in questions:
        if not Question.query.filter_by(question_text=q['question_text']).first():
            new_question = Question(
                question_text=q['question_text'],
                option_a=q['option_a'],
                option_b=q['option_b'],
                option_c=q['option_c'],
                option_d=q['option_d'],
                correct_answer=q['correct_answer']
            )
            db.session.add(new_question)
    
    db.session.commit()

def reset_database():
    db.drop_all()
    db.create_all()
    add_sample_questions()

with app.app_context():
    reset_database()

@app.route('/', methods=['GET', 'POST'])
def home():
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    score = 0
    total_questions = Question.query.count()
    
    for question in Question.query.all():
        selected_answer = request.form.get(f'q{question.id}')
        if selected_answer == question.correct_answer:
            score += 1

    session['score'] = score
    session['total_questions'] = total_questions

    if 'highest_score' not in session or score > session['highest_score']:
        session['highest_score'] = score
    
    return redirect(url_for('result'))

@app.route('/result')
def result():
    score = session.get('score', 0)
    total_questions = session.get('total_questions', 1)
    highest_score = session.get('highest_score', 0)
    
    return render_template('result.html', score=score, total_questions=total_questions, highest_score=highest_score)

if __name__ == '__main__':
    app.run(debug=True)
