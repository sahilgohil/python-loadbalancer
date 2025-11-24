import time
import httpx
from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from itertools import cycle

# --- CONFIGURATION ---
servers = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003"
]

CHAT_SERVER = "http://localhost:5001" 
PAYMENT_SERVER = "http://localhost:5002"

server_cycle = cycle(servers)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- RATE LIMITING DATA ---
visitors = {}
RATE_LIMIT = 5 
TIME_WINDOW = 10 

# --- HELPER FUNCTIONS ---

def check_rate_limit(ip: str):
    current_time = time.time()
    if ip not in visitors:
        visitors[ip] = []
    visitors[ip] = [t for t in visitors[ip] if current_time - t < TIME_WINDOW]
    if len(visitors[ip]) >= RATE_LIMIT:
        return False 
    visitors[ip].append(current_time)
    return True 

async def get_healthy_server(path: str):
    print(path.startswith("chat"))

    if path.startswith("chat"):
        return CHAT_SERVER
    elif path.startswith("payment"):
        return PAYMENT_SERVER
    
    for _ in range(len(servers)):
        server = next(server_cycle)
        try:
            async with httpx.AsyncClient() as client:
                await client.get(server, timeout=1.0)
                return server
        except httpx.RequestError:
            print(f"⚠️ Server {server} is down. Skipping...")
            continue
    return None
# this is the dashboard spacific route
@app.get("/dashboard")
async def dashboard():
    return FileResponse("static/index.html")

# --- MAIN ROUTE (FIXED) ---

# We add TWO decorators. One for paths, one for the homepage.
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
@app.api_route("/", methods=["GET", "POST", "PUT", "DELETE"], include_in_schema=False)
async def proxy(request: Request, path: str = ""):  # Added default path=""
    
    client_ip = request.client.host

    if not check_rate_limit(client_ip):
        print(f"⛔ BLOCKING IP: {client_ip}")
        raise HTTPException(status_code=429, detail="Too Many Requests - Slow Down!")

    target_server = await get_healthy_server(path)
    
    if not target_server:
        raise HTTPException(status_code=503, detail="No available backends!")

    # Construct the URL (Handle the slash carefully)
    url = f"{target_server}/{path}"
    print(f"Forwarding to: {url}") # Added print for debugging

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return Response(content=response.content, status_code=response.status_code)
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Backend failed")

if __name__ == '__main__':
    import uvicorn
    print("🚀 Advanced Load Balancer running on port 8080")
    uvicorn.run(app, host="0.0.0.0", port=8080)