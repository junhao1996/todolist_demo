from flask import app, Flask, render_template

print(__name__)
app = Flask(__name__)


@app.route('/')
def hello():
    todo = ["测试1",
            "测试2", "测试3", "测试4", ]
    return render_template('index.html', todo_list=todo)


if __name__ == "__main__":
    app.run(debug=True)
