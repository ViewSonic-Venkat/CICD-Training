from flask import Flask
import socket

app = Flask (__name__)

@app.route ('/goodbye')
def goodbye():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f'Goodbye @{ip_address}!!'

@app.route('/hello')
def hello():
    return 'Hello Mark!'

@app.route ('/')
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f'Hello World @{ip_address}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#comment to new checkout branch testing
#My pipeline comments