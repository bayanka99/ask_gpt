import os

import openai
from flask import Flask, request, jsonify
from DAL_Controller import database,QA_DTO,init_db,add_qa_dto



app = Flask(__name__)

init_db(app) ##initiates the database


@app.route('/ask',methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    answer = get_answer_from_openai(question)
    add_qa_dto(question,answer)
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

#test=app.test_client().post('/ask', json={'question': 'how are you?'})