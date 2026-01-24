# Foodie Vision
Foodie Vision is a web-based application that demonstrates end-to-end web development using a RESTful backend and a lightweight frontend. The application allows users to upload food images and view structured recipe information, including ingredients and preparation steps. The project focuses on clean API design, modular architecture, and frontend–backend integration.

## Technical Overview
The backend is implemented using FastAPI and handles image uploads, request validation, and structured response generation. The frontend is built using HTML, CSS, and JavaScript with an emphasis on responsiveness and clarity. The project follows a simple and maintainable folder structure suitable for academic and learning purposes.

## Features
- Upload food images through a web interface
- Preview uploaded images
- Display recipe information including ingredients and preparation steps
- RESTful backend using FastAPI
- Responsive frontend design
- Clean and modular project structure

## Tech Stack
Backend: Python, FastAPI
Frontend: HTML, CSS, JavaScript
Tools: Git, GitHub, VS Code

## Project Structure
food_recipe_app/
├── main.py              # FastAPI application entry point
├── static/
│   └── css/
│       └── style.css    # Frontend styling
├── templates/
│   └── index.html       # Main UI template
├── uploads/             # Uploaded food images
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

## How It Works
1. The user uploads a food image using the web interface.
2. The frontend sends the image to the FastAPI backend.
3. The backend processes the request and prepares structured recipe data.
4. The frontend displays the uploaded image along with ingredients and cooking steps.

## Deployment Instructions
Clone the repository:
git clone https://github.com/venomy46/foodie-vision.git
cd foodie-vision

Create a virtual environment:
python -m venv venv

Activate the virtual environment (Windows):
venv\Scripts\activate

Activate the virtual environment (Linux / macOS):
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the application:
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000

## Notes
Ensure Python 3.9 or above is installed. Uploaded images are stored locally in the uploads directory. Use CTRL + C to stop the server.

## Project Objective
This project was developed to strengthen practical skills in backend API development, frontend–backend communication, and web application architecture. It serves as an academic and learning-focused project showcasing clean coding practices and full-stack integration.

## Author
Srikanth M
GitHub: https://github.com/venomy46
