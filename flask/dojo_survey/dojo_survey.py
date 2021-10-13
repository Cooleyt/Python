from flask import Flask , render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/survey')
def survey():
    return render_template('results.html')

@app.route('/')
def index():
    if 'first_name' not in session:
        session['first_name'] = ''
    if 'location' not in session:
        session['dojo_location'] = ''
    if 'language' not in session:
        session['dojo_language'] = ''
    if 'comments' not in session:
        session['comments'] = ''
    return render_template('dojo_survey.html')


@app.route('/requests', methods = ['POST'])
def requests():
    session['first_name'] = request.form['first_name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    return render_template('results.html')

@app.route('/result', methods = ['POST'])
def result():
        return render_template('results.html')

@app.route('/destroy_session')
def destroySession():
    session.clear
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)