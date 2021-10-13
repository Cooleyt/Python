from flask import Flask , render_template 

app = Flask(__name__)

@app.route('/board')
def board():
    return render_template('checkerboard.html', x = 4)

@app.route('/board/<int:x>/<int:y>')
def board2(x, y):
    return render_template('checkerboard.html', x = x, y = y)

@app.route('/board/<int:x>/<int:y>')
def board3(x, y):
    return render_template('checkerboard.html', x = x, y = y)

if __name__ == "__main__":
    app.run(debug=True)