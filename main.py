from fastapi import FastAPI

app = FastAPI()


@app.get("/places")
async def root():
    return {"message": "Hello, World!"}


@app.get("/places/{id}")
async def get_activity_data(id: int, lang_pref=0):
    return {"id": id}
