# from flask import Flask, render_template, request

# import cheater
# import clone


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('input_form.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     letters = request.form['letters']
#     # Here you can use 'letters' to call functions from cheater.py or clone.py
#     return f"You entered: {letters}"

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import cheater
import clone

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    letters = request.form['letters']
    # Here you can use 'letters' to call functions from cheater.py or clone.py
    return f"You entered: {letters}"

if __name__ == '__main__':
    app.run(debug=True)
