# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
import os

import openai
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/ask_gpt'


# Initialize the database
database = SQLAlchemy(app)

class QA_DTO(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    question = database.Column(database.String)
    answer = database.Column(database.String)



@app.route('/ask',methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    answer = get_answer_from_openai(question)
    qa_dto = QA_DTO(question=question, answer=answer)
    database.session.add(qa_dto)
    database.session.commit()
    return jsonify({'question': question, 'answer': answer})

def get_answer_from_openai(question):

    openai.api_key = os.getenv('OPENAI_API_KEY')
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return completion.choices[0].message.content
