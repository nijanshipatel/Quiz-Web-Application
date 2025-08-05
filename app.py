# from flask import Flask, request, render_template, redirect, url_for, session
# from werkzeug.security import generate_password_hash, check_password_hash
# import pandas as pd
# import mysql.connector
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.secret_key = "@123nij"

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="quiz_app"
# )
# print("Database connected successfully")
# cur = db.cursor()

# @app.route('/uploads', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and file.filename.endswith('.xlsx'):
#             filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(filepath)
#             df = pd.read_excel(filepath)

#             for _, row in df.iterrows():
#                 cur.execute("""
#                     INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
#                     VALUES (%s, %s, %s, %s, %s, %s)
#                 """, (
#                     row['Question'], row['Option_A'], row['Option_B'], row['Option_C'],
#                     row['Option_D'], row['Correct_Answer']
#                 ))
#             db.commit()
#             return "Upload successful."
#         else:
#             return "Please upload a valid .xlsx file."
#     return render_template('upload.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == "POST":
#         email = request.form['email']
#         password = request.form['password']
#         password_hash = generate_password_hash(password)
#         try:
#             cur.execute("INSERT into users (email, password_hash) VALUES (%s, %s)", (email, password_hash))
#             db.commit()
#             return "REGISTRATION SUCCESSFUL"
#         except:
#             return "USER already registered"
#     return render_template("register.html")

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         cur.execute("SELECT id, password_hash FROM users WHERE email = %s", (email,))
#         user = cur.fetchone()

#         if user and check_password_hash(user[1], password):
#             session['user_id'] = str(user[0])  # Convert to str
#             return redirect('/confirm')
#         else:
#             return "Invalid credentials"
#     return render_template('login.html')

# @app.route('/confirm', methods=['GET', 'POST'])
# def confirm():
#     if request.method == 'POST':
#         return redirect('/quiz')
#     if 'user_id' not in session:
#         return redirect('/login')
#     return render_template('confirm.html')

# @app.route('/quiz', methods=['GET'])
# def quiz():
#     if 'user_id' not in session:
#         return redirect('/login')

#     cur.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM questions")
#     questions = cur.fetchall()

#     session['questions'] = [list(map(str, q)) for q in questions]  # Convert all elements to str
#     session['current'] = 0
#     session['answers'] = {}

#     return redirect('/show_question')

# @app.route('/show_question')
# def show_question():
#     if 'questions' not in session or 'current' not in session:
#         return redirect('/quiz')

#     current = session['current']
#     questions = session['questions']
#     total = len(questions)

#     if 0 <= current < total:
#         q = questions[current]
#         return render_template('quiz.html',
#             question_id=q[0],
#             question=q[1],
#             option_a=q[2], option_b=q[3],
#             option_c=q[4], option_d=q[5],
#             index=current + 1,
#             total=total,
#             is_last=(current == total - 1),
#             is_first=(current == 0)
#         )
#     return "No question found."

# @app.route('/submit_answer', methods=['POST'])
# def submit_answer():
#     answer = request.form.get('answer')
#     qid = str(request.form.get('question_id'))  # Ensure it's a string

#     answers = session.get('answers', {})
#     answers[qid] = answer
#     session['answers'] = answers

#     current = session.get('current', 0)
#     if current == len(session['questions']) - 1:
#         return redirect('/result')
#     else:
#         session['current'] += 1
#         return redirect('/show_question')

# @app.route('/next', methods=['POST'])
# def next_question():
#     answer = request.form.get('answer')
#     qid = str(request.form.get('question_id'))

#     answers = session.get('answers', {})
#     answers[qid] = answer
#     session['answers'] = answers

#     if 'current' in session and session['current'] < len(session['questions']) - 1:
#         session['current'] += 1
#     return redirect('/show_question')

# @app.route('/previous', methods=['POST'])
# def previous_question():
#     if 'current' in session and session['current'] > 0:
#         session['current'] -= 1
#     return redirect('/show_question')

# @app.route('/result')
# def result():
#     questions = session.get('questions', [])
#     user_answers = session.get('answers', {})

#     correct = 0
#     wrong = 0
#     results = []

#     for q in questions:
#         qid = str(q[0])
#         correct_answer = q[6]
#         user_answer = user_answers.get(qid, "No Answer")

#         if user_answer == correct_answer:
#             correct += 1
#         else:
#             wrong += 1

#         results.append({
#             'question': q[1],
#             'your_answer': user_answer,
#             'correct_answer': correct_answer,
#             'is_correct': user_answer == correct_answer
#         })

#     return render_template("result.html", correct=correct, wrong=wrong, total=len(questions), results=results)

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, render_template, redirect, url_for, session, flash
# from werkzeug.security import generate_password_hash, check_password_hash
# import pandas as pd
# import mysql.connector
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.secret_key = "@123nij"

# import mysql.connector

# # Connect to the RDS database
# db = mysql.connector.connect(
#     host="quizdb.cryiywweedxs.eu-north-1.rds.amazonaws.com",  # RDS endpoint
#     user="admin",                                              # RDS username
#     password="Nijanshi23",                                   # RDS password
#     database="quizdb",                                        # Database name
#     port=3306                                                  # Default MySQL port
# )

# print("✅ Database connected successfully.")

# cur = db.cursor()

# # Path to the SQL file (if it's on EC2, update the path accordingly)
# with open("quiz_app.sql", 'r', encoding='utf-8') as f:
#     sql_script = f.read()

# # Split the script into individual commands
# commands = sql_script.strip().split(';')

# # Execute each SQL command
# for command in commands:
#     command = command.strip()
#     if command:
#         try:
#             cur.execute(command)
#         except mysql.connector.Error as err:
#             print(f"⚠️ Error in command: {command[:100]}...\n{err}")

# # Commit the changes
# db.commit()
# print("✅ SQL file imported successfully.")

# # Close the connection
# cur.close()
# db.close()

# @app.route('/')
# def home():
#     return redirect('/register') 

# @app.route('/uploads', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and file.filename.endswith('.xlsx'):
#             filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(filepath)
#             df = pd.read_excel(filepath)

#             for _, row in df.iterrows():
#                 cur.execute("""
#                     INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
#                     VALUES (%s, %s, %s, %s, %s, %s)
#                 """, (
#                     row['Question'], row['Option_A'], row['Option_B'], row['Option_C'],
#                     row['Option_D'], row['Correct_Answer']
#                 ))
#             db.commit()
#             return "Upload successful."
#         else:
#             return "Please upload a valid .xlsx file."
#     return render_template('upload.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == "POST":
#         email = request.form['email']
#         password = request.form['password']
#         password_hash = generate_password_hash(password)
#         try:
#             cur.execute("INSERT into users (email, password_hash) VALUES (%s, %s)", (email, password_hash))
#             db.commit()
#             return "REGISTRATION SUCCESSFUL"
#         except:
#             return "USER already registered"
#     return render_template("register.html")

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         cur.execute("SELECT id, password_hash FROM users WHERE email = %s", (email,))
#         user = cur.fetchone()

#         if user and check_password_hash(user[1], password):
#             session['user_id'] = str(user[0])
#             session['user_email'] = email
#             return redirect('/confirm')
#         else:
#             return "Invalid credentials"
#     return render_template('login.html')

# @app.route('/confirm', methods=['GET', 'POST'])
# def confirm_start():
#     # ✅ Check if user is logged in
#     if 'user_id' not in session:
#         return redirect(url_for('login'))  # redirect to login if not logged in

#     if request.method == 'POST':
#         return redirect(url_for('quiz'))  # redirect to quiz start page

#     return render_template('confirm.html')

# @app.route('/quiz', methods=['GET'])
# def quiz():
#     if 'user_id' not in session:
#         flash("You must be logged in to start the quiz.")
#         return redirect('/login')

#     cur.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM questions")
#     questions = cur.fetchall()

#     session['questions'] = [list(map(str, q)) for q in questions]
#     session['current'] = 0
#     session['answers'] = {}

#     return redirect('/show_question')

# @app.route('/show_question')
# def show_question():
#     if 'user_id' not in session:
#         flash("You must be logged in to continue the quiz.")
#         return redirect('/login')

#     if 'questions' not in session or 'current' not in session:
#         return redirect('/quiz')

#     current = session['current']
#     questions = session['questions']
#     total = len(questions)

#     if 0 <= current < total:
#         q = questions[current]
#         return render_template('quiz.html',
#             question_id=q[0],
#             question=q[1],
#             option_a=q[2], option_b=q[3],
#             option_c=q[4], option_d=q[5],
#             index=current + 1,
#             total=total,
#             is_last=(current == total - 1),
#             is_first=(current == 0)
#         )
#     return "No question found."

# @app.route('/submit_answer', methods=['POST'])
# def submit_answer():
#     if 'user_id' not in session:
#         flash("You must be logged in to submit an answer.")
#         return redirect('/login')

#     answer = request.form.get('answer')
#     qid = str(request.form.get('question_id'))

#     answers = session.get('answers', {})
#     answers[qid] = answer
#     session['answers'] = answers

#     current = session.get('current', 0)
#     if current == len(session['questions']) - 1:
#         return redirect('/result')
#     else:
#         session['current'] += 1
#         return redirect('/show_question')

# @app.route('/next', methods=['POST'])
# def next_question():
#     if 'user_id' not in session:
#         flash("You must be logged in to continue the quiz.")
#         return redirect('/login')

#     answer = request.form.get('answer')
#     qid = str(request.form.get('question_id'))

#     answers = session.get('answers', {})
#     answers[qid] = answer
#     session['answers'] = answers

#     if 'current' in session and session['current'] < len(session['questions']) - 1:
#         session['current'] += 1
#     return redirect('/show_question')

# @app.route('/previous', methods=['POST'])
# def previous_question():
#     if 'user_id' not in session:
#         flash("You must be logged in to continue the quiz.")
#         return redirect('/login')

#     if 'current' in session and session['current'] > 0:
#         session['current'] -= 1
#     return redirect('/show_question')

# @app.route('/result')
# def result():
#     if 'user_id' not in session:
#         flash("You must be logged in to view results.")
#         return redirect('/login')

#     questions = session.get('questions', [])
#     user_answers = session.get('answers', {})

#     correct = 0
#     wrong = 0
#     results = []

#     for q in questions:
#         qid = str(q[0])
#         correct_answer = q[6]
#         user_answer = user_answers.get(qid, "No Answer")

#         if user_answer == correct_answer:
#             correct += 1
#         else:
#             wrong += 1

#         results.append({
#             'question': q[1],
#             'your_answer': user_answer,
#             'correct_answer': correct_answer,
#             'is_correct': user_answer == correct_answer
#         })

#     return render_template("result.html", correct=correct, wrong=wrong, total=len(questions), results=results)

# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("You have been logged out.")
#     return redirect('/login')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import mysql.connector
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.secret_key = "@123nijanshi@#"

DB_CONFIG = {
    "host": "quizdb.cn4468yo6iiq.ap-south-1.rds.amazonaws.com",
    "user": "admin",
    "password": "Nijanshi23",
    "database": "quizdb",
    "port": 3306
}

@app.route('/')
def home():
    return redirect('/register') 

@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            df = pd.read_excel(filepath)

            try:
                db = mysql.connector.connect(**DB_CONFIG)
                cur = db.cursor()

                for _, row in df.iterrows():
                    cur.execute("""
                        INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        row['Question'], row['Option_A'], row['Option_B'], row['Option_C'],
                        row['Option_D'], row['Correct_Answer']
                    ))
                db.commit()
            except mysql.connector.Error as err:
                return f"❌ Database Error: {err}"
            finally:
                cur.close()
                db.close()

            return "Upload successful."
        else:
            return "Please upload a valid .xlsx file."
    return render_template('upload.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cur = db.cursor()
            cur.execute("INSERT into users (email, password_hash) VALUES (%s, %s)", (email, password_hash))
            db.commit()
        except mysql.connector.Error as err:
            return f"❌ Registration failed: {err}"

        finally:
            cur.close()
            db.close()

        return "REGISTRATION SUCCESSFUL"
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cur = db.cursor()
            cur.execute("SELECT id, password_hash FROM users WHERE email = %s", (email,))
            user = cur.fetchone()
        except mysql.connector.Error:
            user = None
        finally:
            cur.close()
            db.close()

        if user and check_password_hash(user[1], password):
            session['user_id'] = str(user[0])
            session['user_email'] = email
            return redirect('/confirm')
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/confirm', methods=['GET', 'POST'])
def confirm_start():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        return redirect(url_for('quiz'))
    return render_template('confirm.html')

@app.route('/quiz', methods=['GET'])
def quiz():
    if 'user_id' not in session:
        flash("You must be logged in to start the quiz.")
        return redirect('/login')

    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cur = db.cursor()
        cur.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM questions")
        questions = cur.fetchall()
    except mysql.connector.Error as err:
        return f"Database error: {err}"
    finally:
        cur.close()
        db.close()

    session['questions'] = [list(map(str, q)) for q in questions]
    session['current'] = 0
    session['answers'] = {}

    return redirect('/show_question')

@app.route('/show_question')
def show_question():
    if 'user_id' not in session:
        flash("You must be logged in to continue the quiz.")
        return redirect('/login')

    if 'questions' not in session or 'current' not in session:
        return redirect('/quiz')

    current = session['current']
    questions = session['questions']
    total = len(questions)

    if 0 <= current < total:
        q = questions[current]
        return render_template('quiz.html',
            question_id=q[0],
            question=q[1],
            option_a=q[2], option_b=q[3],
            option_c=q[4], option_d=q[5],
            index=current + 1,
            total=total,
            is_last=(current == total - 1),
            is_first=(current == 0)
        )
    return "No question found."

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    if 'user_id' not in session:
        flash("You must be logged in to submit an answer.")
        return redirect('/login')

    answer = request.form.get('answer')
    qid = str(request.form.get('question_id'))

    answers = session.get('answers', {})
    answers[qid] = answer
    session['answers'] = answers

    current = session.get('current', 0)
    if current == len(session['questions']) - 1:
        return redirect('/result')
    else:
        session['current'] += 1
        return redirect('/show_question')

@app.route('/next', methods=['POST'])
def next_question():
    if 'user_id' not in session:
        flash("You must be logged in to continue the quiz.")
        return redirect('/login')

    answer = request.form.get('answer')
    qid = str(request.form.get('question_id'))

    answers = session.get('answers', {})
    answers[qid] = answer
    session['answers'] = answers

    if 'current' in session and session['current'] < len(session['questions']) - 1:
        session['current'] += 1
    return redirect('/show_question')

@app.route('/previous', methods=['POST'])
def previous_question():
    if 'user_id' not in session:
        flash("You must be logged in to continue the quiz.")
        return redirect('/login')

    if 'current' in session and session['current'] > 0:
        session['current'] -= 1
    return redirect('/show_question')

@app.route('/result')
def result():
    if 'user_id' not in session:
        flash("You must be logged in to view results.")
        return redirect('/login')

    questions = session.get('questions', [])
    user_answers = session.get('answers', {})

    correct = 0
    wrong = 0
    results = []

    for q in questions:
        qid = str(q[0])
        correct_answer = q[6]
        user_answer = user_answers.get(qid, "No Answer")

        if user_answer == correct_answer:
            correct += 1
        else:
            wrong += 1

        results.append({
            'question': q[1],
            'your_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': user_answer == correct_answer
        })

    return render_template("result.html", correct=correct, wrong=wrong, total=len(questions), results=results)

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect('/login')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

