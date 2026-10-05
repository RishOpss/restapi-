import os
from fastapi import FastAPI , Body, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

Client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))


@app.get("/employees")
def get_employees():
    response = Client.table("employees").select("*").execute()
    return response.data

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    response = Client.table("employees").select("*").eq("employeeid", employee_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Employee not found")
    return response.data[0]

@app.post("/employees", status_code=201)
def add_employee(employee: dict = Body(openapi_examples={"example": {"value": {"employeeid" : "1", "firstname": "John", "lastname": "Doe", "email": "john@email.com"}}})):
    response = Client.table("employees").insert(employee).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to create employee")
    return response.data[0]

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: dict = Body(openapi_examples={"example": {"value": {"firstname": "Jane", "lastname": "Doe", "email": "jane@email.com"}}})):
    response = Client.table("employees").update(employee).eq("employeeid", employee_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Employee not found")
    return response.data[0]

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    response = Client.table("employees").delete().eq("employeeid", employee_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Employee not found")
    return response.data[0]