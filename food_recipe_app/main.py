from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os, uuid, shutil

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# SIMPLE PREDEFINED RECIPES
RECIPES = {
    "pizza": {
        "ingredients": ["Flour", "Cheese", "Tomato sauce"],
        "steps": ["Prepare dough", "Add toppings", "Bake"],
        "tips": ["Bake at high temperature"]
    },
    "biryani": {
        "ingredients": ["Basmati rice", "Chicken", "Spices"],
        "steps": ["Cook rice", "Prepare masala", "Dum cook"],
        "tips": ["Use long grain rice"]
    },
    "dosa": {
        "ingredients": ["Rice batter", "Urad dal", "Salt"],
        "steps": ["Heat pan", "Spread batter", "Cook till crispy"],
        "tips": ["Use fermented batter"]
    },
    "burger": {
        "ingredients": ["Buns", "Patty", "Lettuce"],
        "steps": ["Grill patty", "Assemble burger"],
        "tips": ["Serve hot"]
    },
    "fried rice": {
        "ingredients": ["Rice", "Vegetables", "Soy sauce"],
        "steps": ["Stir fry vegetables", "Add rice"],
        "tips": ["Use day-old rice"]
    }
}

def detect_food(filename: str):
    name = filename.lower()
    for food in RECIPES:
        if food in name:
            return food
    return "pizza"  # default


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict-food")
async def predict_food(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    food = detect_food(file.filename)
    recipe = RECIPES[food]

    return JSONResponse({
        "predicted_food": food.title(),
        "recipe": recipe,
        "youtube_videos": f"https://www.youtube.com/results?search_query=how+to+make+{food}"
    })
