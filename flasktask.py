from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<flag>')
def prof(flag):
    proflist = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                'инженер по терраформированию', 'климатолог',
                'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                'штурман', 'пилот дронов']
    return render_template('proflist.html', flag=flag, proflist=proflist)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {'title': 'АНКЕТА',
            'surname': 'Васильев',
            'name': 'Петя',
            'education': 'высшее',
            'profession': 'Космонавт',
            'sex': 'мужской',
            'motivation': 'всегда меччтал съесть марсианскую еду',
            'ready': 'готов'}

    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
