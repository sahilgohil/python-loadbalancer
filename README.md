# Custom Load Balancer in Python

A custom-built **Layer 7 Load Balancer** that distributes HTTP traffic across backend servers using a **Round-Robin** algorithm. It includes active fault tolerance to detect and bypass failed backend nodes.

## 🚀 Features
- **Round Robin Scheduling** – Distributes requests sequentially across available servers.  
- **Fault Tolerance** – Automatically detects connection errors and reroutes traffic to healthy servers.  
- **Scalability** – Can handle dynamic server lists (simulated via config).  

## 🛠️ Architecture
```
[ Client ]
     ↓
[ Load Balancer (Port 8080) ]
     ↳ [ Server 1 (5001) ]
     ↳ [ Server 2 (5002) ]
     ↳ [ Server 3 (5003) ]
```

## 💻 How to Run

### 1. Setup
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Start the Backend Fleet  
Open **3 separate terminals** and run:

```bash
# Terminal 1
python server.py 5001

# Terminal 2
python server.py 5002

# Terminal 3
python server.py 5003
```

### 3. Start the Load Balancer  
Open a **4th terminal**:

```bash
python load_balancer.py
```

### 4. Test  
Visit: **http://localhost:8080**

- Refresh to see load distribution.
- Kill one backend server (`Ctrl+C`) → Load Balancer automatically skips it.

---

## 🧠 What I Learned
- **Network Socket Programming** – Ports, TCP connections, HTTP.  
- **Algorithms** – Round Robin using Python iterators.  
- **System Design** – Basics of fault-tolerant distributed systems.  

---