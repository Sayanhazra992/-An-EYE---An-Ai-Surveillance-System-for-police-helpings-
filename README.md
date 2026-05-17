<div align="center">

# 👁️ An EYE
### AI-Powered Surveillance & Emergency Response Platform

Transforming traditional CCTV systems into intelligent real-time incident detection infrastructure for police and public safety systems.

<br>

<img src="./big-dot.png" width="180"/>

<br>

<!-- DEMO GIF PLACEHOLDER -->
<img src="./assets/demo.gif" alt="An-EYE Demo" width="100%"/>

> 📹 Replace the GIF above with:
> - Dashboard walkthrough
> - Violence detection demo
> - Live alert animation
> - Incident escalation workflow

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSockets-black?style=for-the-badge&logo=socketdotio&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-AI-red?style=for-the-badge)

</div>

---

# 🚔 Live Police Dashboard

🌐 **Dashboard:**  
https://an-eye-surveillance.vercel.app/

> ⚠️ Backend APIs may sometimes be inactive because the project currently runs on free-tier infrastructure.

---

# 📚 Table of Contents

- [About](#-about)
- [Features](#-features)
- [System Workflow](#-system-workflow)
- [Tech Stack](#-tech-stack)
- [Monorepo Structure](#-monorepo-structure)
- [Installation Guide](#-installation-guide)
- [Environment Variables](#-environment-variables)
- [Running The Project](#-running-the-project)
- [Future Scope](#-future-scope)
- [Contributors](#-contributors)
- [License](#-license)

---

# 🧠 About

**An EYE** is an AI-powered surveillance intelligence platform designed for:

- 🚨 Real-time violence detection
- 👮 Police monitoring systems
- 📹 Smart CCTV analytics
- 🧠 Human pose intelligence
- ⚡ Live incident alerts
- 📍 Smart emergency response

The platform combines:

- Artificial Intelligence
- Computer Vision
- Real-Time Streaming
- Backend APIs
- Live Monitoring Dashboard

to create a modern intelligent surveillance ecosystem.

---

# ✨ Features

<div align="center">

| Feature | Description |
|---|---|
| 🎥 Real-Time CCTV Monitoring | Analyze live camera feeds |
| 🧠 AI Violence Detection | Detect fights & aggressive motion |
| 🕺 Pose Intelligence | Human pose estimation & movement analysis |
| 🚨 Live Incident Alerts | Instant dashboard notifications |
| 🔊 Alert Sound System | Siren/audio notification support |
| 📼 Smart Clip Recording | Automatic evidence clip generation |
| 📍 Incident Location Tracking | Camera & location metadata |
| 🌐 Police Dashboard | Live centralized monitoring |
| ⚡ WebSocket Updates | Realtime alert communication |
| 🧾 Audit Logs | Incident tracking & review history |
| 📡 Multi-Camera Architecture | Scalable monitoring support |
| 🧠 Local AI Inference | AI runs locally on machine/GPU |
| 🔐 Authentication System | Protected operator access |
| 🖥️ Modern UI Dashboard | Responsive React interface |

</div>

---

# ⚙️ System Workflow

```text
CCTV / Camera Feed
        ↓
Motion Detection
        ↓
AI Violence Detection
        ↓
Pose Intelligence Analysis
        ↓
Threat Confirmation
        ↓
Evidence Clip Recording
        ↓
Incident Generation
        ↓
FastAPI Backend
        ↓
WebSocket Alert System
        ↓
Police Dashboard
```

---

# 🛠️ Tech Stack

## 🤖 AI & Computer Vision

- 🐍 Python
- 👁️ OpenCV
- 🧠 YOLO Pose Estimation
- 🔥 TensorFlow / Keras
- ⚡ Local GPU Inference

---

## ⚙️ Backend

- ⚡ FastAPI
- 🗄️ SQLAlchemy
- 🐘 PostgreSQL / SQLite
- 🔌 WebSockets
- 🔐 JWT Authentication

---

## 🌐 Frontend

- ⚛️ React
- ⚡ Vite
- 🎨 CSS / Tailwind-inspired UI
- 📡 Live Dashboard Updates

---

# 🗂️ Monorepo Structure

```bash
An-EYE/
│
├── dashboard/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── websocket/
│   │   └── utils/
│   │
│   ├── package.json
│   └── vite.config.js
│
├── An-EYE-incident-ai/
│   │
│   ├── ai_engine/
│   │   ├── services/
│   │   ├── suspect_db/
│   │   ├── suspect_faces/
│   │   └── suspect_system/
│   │
│   ├── config/
│   │   └── cameras.json
│   │
│   ├── detectors/
│   │   ├── pose_detector.py
│   │   └── violence_detector.py
│   │
│   ├── model/
│   ├── streaming/
│   ├── app_v1.py
│   └── requirements.txt
│
├── storage/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation Guide

<details>
<summary><b>📥 1. Clone Repository</b></summary>

```bash
git clone https://github.com/Sayanhazra992/-An-EYE---An-Ai-Surveillance-System-for-police-helpings-.git

cd -An-EYE---An-Ai-Surveillance-System-for-police-helpings-
```

</details>

---

<details>
<summary><b>🐍 2. Create Python Environment</b></summary>

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

</details>

---

<details>
<summary><b>📦 3. Install Backend & AI Dependencies</b></summary>

```bash
pip install -r requirements.txt
```

Install AI engine dependencies:

```bash
cd An-EYE-incident-ai

pip install -r requirements.txt
```

</details>

---

<details>
<summary><b>🌐 4. Install Dashboard Dependencies</b></summary>

```bash
cd dashboard

npm install
```

</details>

---

# 🔐 Environment Variables

Create `.env` file in backend/dashboard if needed.

Example:

```env
DATABASE_URL=postgresql://user:password@localhost/aneye
SECRET_KEY=your_secret_key
BACKEND_URL=http://localhost:8000
```

---

# ▶️ Running The Project

## 🤖 Start AI Engine

```bash
cd An-EYE-incident-ai

python app_v1.py
```

---

## ⚙️ Start Backend Server

```bash
uvicorn main:app --reload
```

---

## 🌐 Start Dashboard

```bash
cd dashboard

npm run dev
```

---

# 📸 Demo Assets

## Dashboard Showcase

```md
![Dashboard Demo](./assets/dashboard-demo.gif)
```

---

## AI Detection Showcase

```md
![AI Detection Demo](./assets/violence-detection.gif)
```

---

## Live Alerts Showcase

```md
![Live Alerts](./assets/live-alerts.gif)
```

---

# 🧭 Future Scope

- 🔫 Weapon Detection
- ☁️ Cloud Evidence Storage
- 📱 Mobile Police App
- 🌍 Smart City Integration
- 🛰️ Multi-Camera Synchronization
- 🤖 Distributed AI Nodes
- 🚔 Automatic Dispatch Suggestions
- 👥 Crowd Anomaly Detection

---

# 🤝 Contributors

## 👨‍💻 Sayan Hazra
📧 sayanh992@gmail.com

---

## 👨‍💻 Hanumant Pratap
📧 hanumantpratap1234@gmail.com

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

### 👁️ An EYE
#### Intelligent Surveillance For Faster Emergency Response

⭐ Star the repository if you found this project useful.

</div>