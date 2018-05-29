from flask import app, Flask, render_template

print(__name__)
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
