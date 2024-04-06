#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  # Print the string in the console
    return parameter  # Display the string in the web browser

@app.route('/count/<int:parameter>')
def count(parameter):
    """Count up from zero to a given integer, stopping at 9, with numbers on separate lines."""
    result = ""
    for i in range(min(parameter + 1, 10)):  # Stop at count 9
        if len(result) > 0:
            result += "\n"
        result += str(i)
    if parameter >= 9:
        result += "\n"  # Add newline character after 9
    return result



@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    
    if result is not None:
        return str(result)
    else:
        return 'Error: Invalid operation'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
