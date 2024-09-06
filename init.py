from flask import Flask, render_template
import random

app = Flask(__name__)

# Simulasi status server atau aplikasi
def get_status():
    status_list = ['Online', 'Offline', 'Maintenance', 'Degraded']
    return random.choice(status_list)

@app.route('/')
def dashboard():
    server_status = get_status()
    return render_template('index.html', status=server_status)

if __name__ == '__main__':
    app.run(debug=True)
