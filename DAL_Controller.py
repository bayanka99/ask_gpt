from flask_sqlalchemy import SQLAlchemy

# Initialize the database
database = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@db:5432/ask_gpt'
    database.init_app(app)

class QA_DTO(database.Model): ##this defines the table and it's columns
    id = database.Column(database.Integer, primary_key=True)
    question = database.Column(database.String)
    answer = database.Column(database.String)

def Insert_QA(question, answer):
    qa_dto = QA_DTO(question=question, answer=answer)
    database.session.add(qa_dto)
    database.session.commit()
