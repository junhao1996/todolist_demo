from flask import app, Flask, render_template

from todo.db import TodoDB

print(__name__)
app = Flask(__name__)


@app.route('/')
def hello():
    db = TodoDB()

    todo = db.read_all()
    return render_template('index.html', todo_list=todo)


if __name__ == "__main__":
    app.run(debug=True)
