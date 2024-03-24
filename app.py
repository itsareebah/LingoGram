# index.py
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from src import lingua

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/commands/lingua', methods=['POST'])
def lingua_command():
    data = request.json
    tone = data['tone']
    text = data['text']
    
    try:
        generated_text = lingua.execute(tone, text)
        tone_options = ["formal", "informal", "optimistic", "worried", "friendly", "curious", "assertive", "encouraging", "suprised", "cooperative"]
        return jsonify({'generated_text': generated_text, 'tone_options': tone_options}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
