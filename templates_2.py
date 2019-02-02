from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'snjl'}
    # return render_template('index.html', title='博客', user=user)
    return render_template('index_2.html', title='博客', user=user)
    # return render_template('index_2.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
