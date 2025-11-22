# importing required modules
from flask import Flask
import sys

# starting the application
app = Flask(__name__)

@app.route('/')
def hello():

    return f'Hello from server running from {port}'

if __name__ == '__main__':
    # check if the user has provided a port number
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    # get the port number from commandline
    port = int(sys.argv[1])

    # start the server
    print(f'Starting server on port {port}...')

    app.run(port=port)