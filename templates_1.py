from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'snjl'}
    return '''
<html>
    <head>
        <title>Home Page - Home</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''


if __name__ == '__main__':
    app.run(debug=True)
