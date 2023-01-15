from flask import Flask,render_template

app = Flask(__name__)

is_logged: bool = True


@app.route('/')
def index():
    global is_logged
    if is_logged:
        mylist = ['RUFUS','TELLOR','DOTNET','QUITO','SALEM']
        return render_template('home.html',task=mylist)
    else:
        return render_template('not_logged.html')

@app.route('/info')
def info():
    return '<h1>Information page</h1>'

@app.route('/user/<name>')
def user(name):
    name_lenght = len(name)
    return f'<h1>Bem vindo {name.upper()} seu nome tem {name_lenght} characteres</h1>'

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()