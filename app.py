# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ACEest_Fitness!"

@app.route('/api/members')
def get_members():
    members = [
        {"id": 1, "name": "John Doe", "membership_level": "gold"},
        {"id": 2, "name": "Jane Smith", "membership_level": "silver"}
    ]
    return jsonify(members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)