from flask import Flask, render_template, request, jsonify, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'insecure-secret-key-for-demo'

# Simulated user database
users_db = {
    'alice': {'password': 'alice123', 'balance': 5000, 'account': '1234-5678'},
    'bob': {'password': 'bob456', 'balance': 3000, 'account': '8765-4321'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Vulnerable: credentials sent over HTTP
    if username in users_db and users_db[username]['password'] == password:
        session['username'] = username
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'user': username,
            'balance': users_db[username]['balance'],
            'account': users_db[username]['account']
        })
    
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/transfer', methods=['POST'])
def transfer():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.get_json()
    amount = float(data.get('amount', 0))
    to_account = data.get('to_account')
    
    username = session['username']
    
    if users_db[username]['balance'] >= amount:
        users_db[username]['balance'] -= amount
        return jsonify({
            'success': True,
            'message': f'Transferred ${amount} to {to_account}',
            'new_balance': users_db[username]['balance']
        })
    
    return jsonify({'success': False, 'message': 'Insufficient funds'}), 400

@app.route('/balance')
def balance():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    username = session['username']
    return jsonify({
        'username': username,
        'balance': users_db[username]['balance'],
        'account': users_db[username]['account']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
