from flask import Flask
import os
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

# Replace with your full name
FULL_NAME = "Deepanshu Biswas"

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')
    
    # Get 'top' command output (first 10 lines)
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout
    top_output_lines = "\n".join(top_output.split("\n")[:10])
    
    # HTML response
    response = f"""
    <html>
        <head><title>HTOP Endpoint</title></head>
        <body>
            <h1>HTOP Endpoint</h1>
            <p><strong>Name:</strong> {FULL_NAME}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time:</strong> {server_time}</p>
            <h2>Top Output</h2>
            <pre>{top_output_lines}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
