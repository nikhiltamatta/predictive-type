from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample dictionary of words
dictionary = ["apple", "banana", "orange", "pineapple", "grape", "kiwi", "strawberry", "blueberry", "mango", "watermelon"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prefix = data['prefix'].lower()
    suggestions = [word for word in dictionary if word.startswith(prefix)]
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
