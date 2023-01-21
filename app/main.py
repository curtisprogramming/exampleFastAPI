from fastapi import FastAPI
from .routers import posts, users, auth, vote
from . import oauth2, utils, models
from fastapi.middleware.cors import CORSMiddleware

#initialzes database tables
#from .database import engine
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#adds routes to app
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello Bigger Applications!"} 