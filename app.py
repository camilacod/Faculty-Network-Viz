from flask import Flask, render_template, jsonify
import os
import json
from process_data import process_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Create directories if they don't exist
    os.makedirs('static/data', exist_ok=True)
    
    # Process data if files don't exist
    if not (os.path.exists('static/data/nodes.json') and os.path.exists('static/data/edges.json')):
        process_data()
    
    # Load the processed data
    with open('static/data/nodes.json', 'r') as f:
        nodes = json.load(f)
    
    with open('static/data/edges.json', 'r') as f:
        edges = json.load(f)
    
    return jsonify({
        'nodes': nodes,
        'edges': edges
    })

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('static/data', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Process data
    process_data()
    
    app.run(debug=True)
