from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segredo')
def get_flag():
    with open('segredo.txt', 'r') as f:
        flag_content = f.read()
        print(flag_content) 
    return flag_content

if __name__ == '__main__':
    app.run(debug=True)
