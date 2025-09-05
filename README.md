
# 🚇 Metro Route Expert

A full-stack Delhi Metro navigation system powered by **React** (frontend) and **Flask** (backend), using **Dijkstra’s Algorithm** to compute fare-inclusive optimal routes across 40+ stations with dynamic visual maps.


## 📁 Project Structure

MetroRouteExpert/

├── py-backend/ # Flask backend

│ └── main.py # Entry point for Flask

│
├── metro_fair-master/ # Graph and routing logic (Dijkstra)
│
├── metro_route_expert/

│ └── src/ # React frontend

│ └── (npm start here)
│
├── map_data.csv # Metro station map data

├── links.csv # Station connection data

├── getlinks.ipynb # Preprocessing / analysis notebook

├── Metro Route Xpert_Prj2.pptx

├── MetroRouteXpert_PRJ2.pdf


## 🛠️ Tech Stack

- **Frontend**: React, JavaScript, HTML, CSS
- **Backend**: Flask (Python)
- **Algorithm**: Dijkstra’s Shortest Path
- **Data**: Delhi Metro Stations, Line Transitions
- **Visualization**: Map-based route display


## 🚀 Key Features

- ⚡ Real-time shortest path computation (time & fare)
- 🔀 Handles inter-line transitions intelligently
- 🗺️ Interactive map visualizing routes and stations
- 🔄 Fast communication between frontend and backend via REST API


## 🧠 How It Works

1. React frontend captures user input (source & destination)
2. Sends request to Flask API (`/get_route`)
3. Backend runs Dijkstra’s Algorithm using CSV datasets
4. Returns route, time, fare, and transitions
5. React displays it with dynamic map visualization

---

## 💻 Run Locally

### ▶️ Start Flask Backend

cd py-backend
python main.py
Backend will run at http://localhost:5000/

🌐 Start React Frontend

cd metro_route_expert
npm install
npm start
Frontend will run at http://localhost:3000/

Make sure the frontend sends API requests to http://localhost:5000

📊 Data Files
map_data.csv – Station coordinates and metadata

links.csv – Connections between stations

getlinks.ipynb – Used to process and build graph from raw data

📎 Supporting Material
Metro Route Xpert_Prj2.pptx – Project presentation

MetroRouteXpert_PRJ2.pdf – Project report/documentation

Deployed on RENDER:
https://metroroutexpert.onrender.com/


✨ Developed By
Bhumika
B.Tech, BML Munjal University
🌐 GitHub: @bhumika152

📃 License
MIT License — free to use with attribution.

