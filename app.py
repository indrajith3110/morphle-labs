from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Indrajith Somaiah r m"   
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"   
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")
    
    try:
        top_output = subprocess.getoutput("top -b -n 1")   
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <h2>Name: {full_name}</h2>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <h2>TOP output:</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)