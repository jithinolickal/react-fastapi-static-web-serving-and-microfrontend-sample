"""
Run: uvicorn main-with-micro-frontend:app --reload
This is an implementation of the micro-frontend architecture, 
    where the frontend app is built as a separate app and served from the backend app. 
    This allows you to build and deploy the frontend and backend apps independently, and combine them at runtime.
    Refer html file under /microfrontend-container folder
    
This file will serve the static files from the dist folder of the frontend app, and the index.html file will be served from the root path. The index.html file will load the JavaScript and CSS files from the dist/assets folder.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/frontend", StaticFiles(directory="../frontend/dist/assets"), name="frontend")
# dist/assets/HomePage-F0tNpdY4.js
# dist/assets/index-BDYb-ORO.js
# dist/assets/index-BPvgi06w.css
# dist/assets/Page1-DTG021ka.js
# dist/assets/Page2-Cyr-aB7O.js
