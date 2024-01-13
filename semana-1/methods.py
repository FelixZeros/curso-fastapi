from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
async def get_students():
    return "Este es el mensaje de un estudiante"

@app.get("/students/{id}")
async def get_students_id(id: int):
    return id

@app.post("/create_students")
async def create_students(id: int, name: str, last_name: str, status: bool):
    return True

@app.put("/students/{id}")
async def edit_student(id: int, name: str, last_name: str, status: bool):
    return id

@app.delete("/students/{id}")
async def delete_student(id: int):
    return id