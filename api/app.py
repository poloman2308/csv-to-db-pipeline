import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from etl.load_data import load_csv_to_db
import os

app = Flask(__name__)

@app.route('/load', methods=['POST'])
def load_csv():
    data = request.get_json()
    csv_path = data.get('csv_path')
    table_name = data.get('table_name')

    if not csv_path or not table_name:
        return jsonify({"error": "csv_path and table_name are required"}), 400

    if not os.path.exists(csv_path):
        return jsonify({"error": f"CSV file not found at {csv_path}"}), 404

    try:
        load_csv_to_db(csv_path, table_name)
        return jsonify({"message": f"Loaded {csv_path} into {table_name}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
