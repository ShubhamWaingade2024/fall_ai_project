
# AI Guardian 🚨
## Real-Time Fall Detection & Emergency Response System

---

## 📌 Project Overview

AI Guardian is a real-time AI surveillance system that detects human falls using computer vision and automatically triggers emergency response workflows. The system integrates detection intelligence, verification logic, location services and automated alerts to reduce response time during emergencies.

---

## 🎯 Problem Statement

Falls are a major cause of injury in:
• Elderly care environments  
• Industrial workplaces  
• Public surveillance areas  

Traditional monitoring requires manual supervision.

AI Guardian solves this by:

✅ Detecting falls automatically  
✅ Reducing false positives  
✅ Alerting emergency contacts  
✅ Providing AI first aid recommendations  
✅ Sharing exact incident location  

---

## 🏢 System Architecture

Video Input 🎥  
↓  
YOLOv8 Detection Engine 🤖  
↓  
FastAPI Processing Server ⚙️  
↓  
Event Decision Engine 🧠  

Event Engine triggers:

📩 Telegram Alert System  
📍 Google Maps Location  
🩺 OpenAI First Aid Suggestions  
🖥 Streamlit Monitoring Dashboard  

---

## 🔄 Core Workflow

Detection Pipeline:

Detection → Verification → Classification → Alert Decision

System Logic:

1️⃣ Person fall detected  
2️⃣ Timer verification starts  
3️⃣ Movement check performed  
4️⃣ If movement → Ignore  
5️⃣ If no movement (10 sec) → Alert triggered  
6️⃣ AI generates recommendations (Firstaid)
7️⃣ Location shared  
8️⃣ If no recovery (60 sec) → Hospital escalation  


---

## ✨ Key Features

### AI Features 🤖

• Real-time fall detection  
• YOLOv8 posture classification  
• Confidence score display  
• Bounding box visualization  
• False positive filtering  

### System Features ⚙️

• Incident timer verification  
• Unique incident ID  
• Event decision pipeline  
• Real time processing  

### Integration Features 🔗

• Telegram emergency alerts  
• Google Maps location sharing  
• OpenAI first aid recommendations  
• Nearby hospital identification  

### UI Features 🖥

• Live dashboard  
• Incident display  
• Detection status  
• Alert notifications  

---

## 🛠 Tech Stack

### AI / Vision 🤖

Python  
YOLOv8  
OpenCV  
PyTorch  

### Backend ⚙️

FastAPI  
Uvicorn  
REST API  

### Frontend 🖥

Streamlit  

### APIs 🔗

Telegram Bot API  
Google Maps API  
OpenAI API  

### Engineering Tools 💻

Git  
VS Code  
Virtual Environment  

---

## 📂 Project Structure

fall_ai_project/

backend/
│
├── main.py
├── detector.py
├── services.py
├── telegram_service.py
├── config.py
│
frontend/
│
├── app.py
│
model/
│
├── best.pt
│
uploads/

README.md

requirements.txt

---

## ⚙️ Backend Setup and Execution

### 📥 Clone repository

git clone YOUR_REPO_LINK

cd fall_ai_project

---

### 🐍 Create virtual environment

python -m venv .venv

---

### ▶️ Activate environment

Windows:

.venv\\Scripts\\activate

Linux/Mac:

source .venv/bin/activate

---

### 📦 Install dependencies

cd backend

pip install fastapi uvicorn ultralytics opencv-python torch requests openai python-multipart

---

### 🔑 Environment configuration

Edit:

backend/config.py

Add:

TELEGRAM_TOKEN="YOUR TOKEN"

CHAT_ID="YOUR CHAT ID"

OPENAI_KEY="YOUR KEY"

GOOGLE_KEY="YOUR KEY"

LAT=18.5204

LON=73.8567

---

### 🚀 Run backend

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

---

## 🖥 Frontend Setup and Execution

### Navigate:

cd frontend

---

### Install dependencies:

pip install streamlit requests

---

### Start frontend:

streamlit run app.py

Frontend:

http://localhost:8501

---

## 🔗 API Reference

### Detect Incident 🚨

POST /detect

Detects fall from uploaded video.

Returns:

incident_id  
confidence  
status  
location  
recommendation  

---

### Incident History 📊

GET /incidents

Returns incident logs.

---

### Health Check ❤️

GET /

Server status check.

---

## ⚠ Challenges Faced

Environment conflicts  
API integration failures  
Backend import errors  
Model timing logic  
False detection filtering  

Solved through debugging and modular design.

---

## 📈 Learning Outcomes

Computer Vision deployment  
Backend engineering  
System design thinking  
API integration  
Real-time processing  
Debugging production issues  

---

## 🚀 Future Improvements

• Live webcam detection  
• Multi camera monitoring  
• Incident database  
• Cloud deployment  
• Edge deployment (Jetson Nano)  
• Mobile application  
• SMS alert backup  
• Detection optimization  

---

## 👨‍💻 Author

Shubham Waingade

AI Engineer | Embedded Systems | VLSI
