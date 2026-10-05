import os 
from fastapi import FastAPI , Body
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

Client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))


@app.get("/employees")
def get_employees():    
    response = Client.table("employees").select("*").execute()
    return response.data

@app.post("/employees")
def add_employee(employee: dict = Body(openapi_examples={"example": {"value": {"employeeid" : "1", "firstname": "John", "lastname": "Doe", "email": "john@email.com"}}})):
    response = Client.table("employees").insert(employee).execute()
    return response.data

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: dict = Body(openapi_examples={"example": {"value": {"firstname": "Jane", "lastname": "Doe", "email": "jane@email.com"}}})):
    response = Client.table("employees").update(employee).eq("employeeid", employee_id).execute()
    return response.data

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    response = Client.table("employees").delete().eq("employeeid", employee_id).execute()
    return response.data