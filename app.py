from flask import Flask, render_template, request
from datetime import date as _date, datetime as _datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from database import MessageDB, Base

app = Flask(__name__)
engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

session = Session()
repo = MessageDB(session)

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/add_message_db", methods=['POST'])
def add_message_db():
    data = request.get_json()
    content = data.get('content')
    timestamp = _datetime.now()
    res = repo.add_message(content, timestamp)
    return {"status": "ok"}

@app.route("/view")
def view():
    messages = repo.get_all_messages()
    return render_template('view.html', messages=messages)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=False)

