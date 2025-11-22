from flask import Flask
import requests
from itertools import cycle

app = Flask(__name__)

servers = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003"
]

server_cycle = cycle(servers)

@app.route('/')
def load_balancer():
    
    for _ in range(len(servers)):
        try:
            server = next(server_cycle)
            response = requests.get(server)
            return response.text
        except:
            print (f"server is down {server}... trying next ...")
            continue
    return "All backends are down!", 503


if __name__ == "__main__":
    print("Load Balancer running on port 8080...")

    app.run(port=8080)