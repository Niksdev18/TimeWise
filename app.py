from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# --- Chatbot Logic ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "bored": ["How about learning a new shortcut in VS Code?", "Watch a documentary on Netflix.", "Go for a 10-minute walk."],
        "code": ["Try solving a LeetCode 'Easy' problem.", "Build a To-Do list app today.", "Check out roadmap.sh for guidance."],
        "stress": ["Take a deep breath. Try the 4-7-8 breathing technique.", "Listen to some Lo-Fi beats.", "Drink a glass of water."],
        "hello": ["Hey there! How can I help you utilize your time today?", "Hello! Ready to be productive?"],
        "default": ["That's interesting! Tell me more.", "I can help with Coding, Fitness, or Relaxation advice."]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.form['msg']
    bot_reply = get_bot_response(user_msg)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)