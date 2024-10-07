import os

import openai
from flask import Flask, request, jsonify
from src.DAL_Controller import init_db,Insert_QA



app = Flask(__name__)

init_db(app) ##initiates the database


@app.route('/ask',methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    if question is None or question=="":
        return jsonify({'error': 'No question provided'}),400
    answer = get_answer_from_openai(question)
    Insert_QA(question,answer)
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
