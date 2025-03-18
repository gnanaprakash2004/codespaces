from flask import Flask
import getpass
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your actual full name
    full_name = "Gnana Prakash Pragada"
    
    # Get the system username
    system_username = getpass.getuser()
    
    # Get current server time in IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    server_time_ist = datetime.now(ist_timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    # Capture the output of the "top" command (in batch mode, one iteration)
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {e}"
    
    # Construct the HTML response
    html_response = f"""
    <html>
    <head>
        <title>/htop Endpoint</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border: 1px solid #ddd;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
        <h1>/htop Data</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {system_username}</p>
        <p><strong>Server Time in IST:</strong> {server_time_ist}</p>
        <h2>Top Command Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_response

if __name__ == '__main__':
    # Run the app on all interfaces on port 5000
    app.run(host="0.0.0.0", port=5000)

