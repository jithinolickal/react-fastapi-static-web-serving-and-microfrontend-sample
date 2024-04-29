"""
This file is a FastAPI application that serves a React app from the dist folder.
The dist folder is the output folder of the React app after building it.
Based ion the mount url, the index.html file will be served from the root path. Baseurl is set in frontend as /frontend (in vite.config.js)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the dist folder containing your built React app
app.mount("/frontend", StaticFiles(directory="../frontend/dist", html=True), name="ReactApp")