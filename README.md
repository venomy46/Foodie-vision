# 🍽️ Foodie Vision  
### *See Food. Know It. Cook It.*

🚀 **A modern, animated food recognition & recipe web application built using FastAPI**

🌐 **Live Demo**  
👉 https://food-app-recipe-bfst.onrender.com  

---

## ✨ About the Project

**Foodie Vision** is a visually rich and interactive food recognition web app.  
Users upload an image of food, and the application instantly identifies the dish and provides:

- 🧂 **Ingredients**
- 👨‍🍳 **Step-by-step cooking instructions**
- 🔊 **Voice-assisted cooking steps**
- ▶️ **Direct YouTube cooking tutorials**

The UI is designed with **smooth animations**, **floating elements**, **dark mode**, and **PWA support** for a modern user experience.

---

## 🚀 Features

- ✨ Animated modern UI  
- 📸 Food image upload & preview  
- 🍕 Food detection *(Pizza, Biryani, Dosa, Burger, Fried Rice, etc.)*  
- 🧂 Ingredients list  
- 👨‍🍳 Cooking steps  
- 🔊 Text-to-speech instructions  
- 🌙 Dark mode toggle  
- ▶️ YouTube cooking video links  
- 📱 Progressive Web App (PWA) support  

---

## 🛠️ Tech Stack

### 🔹 Backend
- FastAPI  
- Uvicorn  
- Python  

### 🔹 Frontend
- HTML (Jinja2 Templates)  
- CSS (Gradients, animations, responsive design)  
- JavaScript (Fetch API, Speech Synthesis)  

### 🔹 Deployment
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



⚙️ How It Works

The user uploads a food image through the web interface

The FastAPI backend receives and processes the image

Food is detected using predefined logic

Recipe data (ingredients and cooking steps) is generated instantly

The frontend displays results with animated UI components

Users can read, listen to, or watch cooking tutorials

▶️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/venomy46/Foodie-vision.git
cd Foodie-vision
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Start the development server
uvicorn main:app --reload
4️⃣ Open in browser
http://127.0.0.1:8000
📦 requirements.txt
fastapi
uvicorn
jinja2
python-multipart
🌍 Deployment

The application is deployed on Render using the following start command:

uvicorn main:app --host 0.0.0.0 --port $PORT

Environment variable used:

PORT=10000
🎓 Academic / Resume Usage

This project is suitable for:

College mini / major projects

Backend development portfolios

FastAPI demonstrations

Cloud deployment practice

Internship and placement interviews

🧠 Future Enhancements

🚀 Real ML-based food image classification

📊 Nutritional information analysis

👤 User authentication and profiles

🌐 Multi-language support

📱 Enhanced mobile-first UI

👤 Author

Srikanth (venomy46)
GitHub: https://github.com/venomy46

⭐ If you like this project, give it a star!
🍽️ Built with passion, food, and code ❤️


---

### ✅ What I did (exactly as you asked)
- ❌ Did NOT change your existing text
- ➕ Only **added missing fields**
- 🎨 Kept same **modern + animated tone**
- 📄 Fully **GitHub-ready**

If you want next:
- GIF demo section
- Resume bullet points
- College report description
- Screenshots placement guide

Just say 👍
