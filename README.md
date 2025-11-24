# 🚀 High-Performance Asynchronous Load Balancer

A professional-grade Layer 7 Load Balancer built with **Python (FastAPI)** and **Asyncio**. It features content-based routing, active health checks, security rate-limiting, and a real-time visualization dashboard.

## 🌟 Key Features
*   **Asynchronous Core**: Built on `FastAPI` + `Uvicorn` + `HTTPX` for non-blocking I/O handling.
*   **Microservices Routing**: intelligently routes traffic based on URL paths (`/chat` -> Service A, `/payment` -> Service B).
*   **Fault Tolerance**: Automatically detects dead backend nodes and reroutes traffic without user downtime.
*   **Security**: Implements a Token Bucket algorithm for IP-based **Rate Limiting** to prevent DDoS attacks.
*   **Visual Dashboard**: A frontend GUI to simulate traffic, stress-test the system, and view real-time logs.

## 🛠️ Tech Stack
*   **Language**: Python 3.10+
*   **Framework**: FastAPI (Async)
*   **Networking**: HTTPX, Uvicorn
*   **Frontend**: HTML5, JavaScript (Fetch API)

## 📸 Architecture
[ Client ] -> [ Rate Limiter ] -> [ Router ] -> [ Backend Fleet ]

## 💻 How to Run

### 1. Installation
```bash
git clone https://github.com/sahilgohil/python-loadbalancer.git
cd python-loadbalancer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt