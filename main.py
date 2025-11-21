from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cloud Run test setup working!"}
