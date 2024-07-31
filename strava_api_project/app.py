from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    python_code = '''
def greet(name):
    return f"Hello, {name}!"

greeting = greet("World")
    '''
    result = eval(python_code.splitlines()[-2])  # Be cautious with eval()
    return render_template('projects.html', python_code=python_code, result=result)

if __name__ == '__main__':
    app.run(debug=True)
