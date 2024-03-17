from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('password астронавта', validators=[DataRequired()])
    id_kap = StringField('id капитана', validators=[DataRequired()])
    password_kap = PasswordField('password капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/index/<title>')
@app.route('/<title>')
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


@app.route('/armor', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('armor.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', user_list=[
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тедди Сандерс',
        'Шон Бин'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
