from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Path to the SQLite database
DATABASE = 'classical_music.db'

def query_db(query, args=(), one=False):
    """Function to query the SQLite database."""
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/query', methods=['POST'])
def run_query():
    """API endpoint to execute a SQL query."""
    query = request.form.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        result = query_db(query)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
