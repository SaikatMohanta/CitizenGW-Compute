from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory log storage
LOGS = []

# Landing page with basic instructions
@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CitizenGW-Compute Server</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { background: white; padding: 20px; border-radius: 12px; 
                         box-shadow: 0 4px 10px rgba(0,0,0,0.1); max-width: 800px; margin: auto; }
            h1 { color: #2c3e50; }
            a { color: #2980b9; text-decoration: none; }
            a:hover { text-decoration: underline; }
            pre { background: #eee; padding: 10px; border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CitizenGW-Compute Server</h1>
            <p>Welcome! This server collects logs from clients running <b>CitizenGW-Compute</b>.</p>

            <h2>Available Endpoints</h2>
            <ul>
                <li><a href="/logs">/logs</a> — view collected logs (JSON)</li>
                <li><code>/upload</code> — POST endpoint where clients send logs</li>
            </ul>

            <h2>How to Test</h2>
            <p>From your client machine, run:</p>
            <pre>
python client.py --server http://127.0.0.1:5000/upload
            </pre>
            <p>Then check <a href="/logs">/logs</a> to see incoming data.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)


@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    if data:
        LOGS.append(data)
        return jsonify({"status": "ok", "received": data}), 200
    return jsonify({"status": "error", "message": "No JSON received"}), 400


@app.route("/logs", methods=["GET"])
def logs():
    return jsonify(LOGS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
