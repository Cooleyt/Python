from flask import Flask , render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():

    if 'counter1' not in session:
        session['counter1'] = 0
            
    return render_template('counter.html')

# @app.route('/increment', methods=['POST'])
# def increment_counter():    


@app.route('/increment/<int:num>')
def increment_counter(num):

    session[f'counter{num}'] += 1

        # if num ==1:
        #     session['counter1'] += 1
    return redirect('/')

# @app.route('/')
# def index():

#     if 'counter1' not in session:
#         session['counter1'] = 0

#     return redirect('/')



@app.route('/reset')
def reset_counters():

    #method 1  set back to a value
    # session['counter1'] = 0

    # #method2   clears a specific key
    # session.pop('counter1')

    #method3   clears all keys -not the best
    session.clear()
    return redirect('/')

    # if 'key_name' in session:
    # print('key exists!')
# else:
#     print("key 'key_name' does NOT exist")


if __name__ == "__main__":
    app.run(debug=True)