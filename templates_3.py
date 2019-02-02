from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'snjl'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index_3.html', title='Home', user=user, posts=posts)
    # return render_template('index_3.html', user=user, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
