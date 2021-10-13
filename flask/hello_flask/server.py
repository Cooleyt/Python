from flask import Flask , render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/another route')
# def another_route():
#     return 'I am another route!'


# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
    
# @app.route('/dojo')
# def success():
#     return 'dojo'

# if __name__ == "__main__":
#     app.run(debug=True)   
    
# app.run(debug=True) should be the very last statement! 

# @app.route('/say/<flask>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(flask):
#     print(flask)
#     return "Hello, " + flask

# if __name__ == "__main__":
#     app.run(debug=True)  

# @app.route('/repeat/<num>/<hello>') # i want this to run hello 35 times
# def repeat (num, hello):
#     return (hello + ' ') * int(num)

# if __name__ == "__main__":
#     app.run(debug=True)  

# @app.route('/multiply/<int:x>/<int:y>')
# def multiply(x, y):
#     return render_template('multiply.html', x = x,
#     y = y, result = x * y)

# if __name__ == "__main__":
#     app.run(debug=True)  
