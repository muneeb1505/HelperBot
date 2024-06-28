import google.generativeai as genai
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "AIzaSyAHBYS-5JvEuvKLvGlAvZ3gmRCbZYYl3zo"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

responses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')
        if not question.strip():
            response = "Please give Prompt !!"
        else:
            response = chat.send_message(question).text
        responses.insert(0, {'response': response})
    return render_template('genai.html',responses=responses)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/about')
def about():
    return render_template('genAbout.html')

@app.route('/services')
def services():
    return render_template('genServices.html')

@app.route('/contactus')
def contact():
    return render_template('YTContact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
