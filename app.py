from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=["get"])

def home():
    with open("score.txt", "r") as my_score:
        scores = []
        for line in my_score:
            scores.append(line)
        return render_template('home.html', scores=scores)


@app.route('/add', methods=["post"])

def add():
    score = request.json
    with open("score.txt", "a") as my_score:
        my_score.write(str(score["score"]))
        my_score.write("/n")
        return make_response("done")

if __name__ == "__main__":
    app.run()