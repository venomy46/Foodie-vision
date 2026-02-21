<div align="center">

# 🍽️ Foodie Vision  
### *See Food. Know It. Cook It.*

🚀 A modern, animated food recognition & recipe web application built using **FastAPI**

🌐 **Live Demo**  
👉 https://food-app-recipe-bfst.onrender.com  

<br/>

<img src="https://img.shields.io/badge/FastAPI-Modern-00C7B7?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black"/>

</div>

---

## ✨ About the Project

**Foodie Vision** is a visually rich and interactive food recognition web app.  
Users upload an image of food, and the application instantly identifies the dish and provides:

- Ingredients 🧂  
- Step-by-step cooking instructions 👨‍🍳  
- Voice-assisted cooking steps 🔊  
- Direct YouTube cooking tutorials ▶️  

The UI is designed with **smooth animations**, **floating elements**, **dark mode**, and **PWA support** for a modern user experience.

---

## 🚀 Features

✨ Animated modern UI  
📸 Food image upload & preview  
🍕 Food detection (Pizza, Biryani, Dosa, Burger, Fried Rice, etc.)  
🧂 Ingredients list  
👨‍🍳 Cooking steps  
🔊 Text-to-speech instructions  
🌙 Dark mode toggle  
▶️ YouTube cooking video links  
📱 Progressive Web App (PWA) support  

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Uvicorn
- Python

### Frontend
- HTML (Jinja2 Templates)
- CSS (Gradients, animations, responsive design)
- JavaScript (Fetch API, Speech Synthesis)

### Deployment
- Render

---

## 📁 Project Structure

```text
Foodie-vision/
│
├── main.py                 # FastAPI backend
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Main UI page
│
├── static/
│   ├── css/
│   │   └── style.css       # Styling & animations
│   ├── manifest.json       # PWA configuration
│   └── service-worker.js  # Offline support
│
└── uploads/                # Uploaded food images
