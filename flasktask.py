from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', prof=prof)




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
