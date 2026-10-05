# REST API Employee Management

A simple REST API for managing employee records built with FastAPI and Supabase.

## Overview

This project implements a CRUD (Create, Read, Update, Delete) API for managing employee data using:
- **FastAPI** - Modern, fast web framework for building APIs with Python
- **Supabase** - Open source Firebase alternative for backend services
- **Python-dotenv** - For managing environment variables

## Features

- Get all employees (`GET /employees`)
- Add a new employee (`POST /employees`)
- Update an existing employee (`PUT /employees/{employee_id}`)
- Delete an employee (`DELETE /employees/{employee_id}`)

## Project Structure

```
rest-api-from-scratch/
├── main.py          # Main application file with API endpoints
├── .env             # Environment variables (SUPABASE_URL, SUPABASE_KEY)
├── restscract/      # Additional project files
│   ├── bin/         # Binary files
│   └── lib/         # Library files
└── README.md        # This file
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rest-api-from-scratch
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi supabase python-dotenv uvicorn
   ```

3. **Configure environment variables**
   Create a `.env` file in the root directory with:
   ```
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

   You can find these values in your Supabase project settings under API.

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`

## API Endpoints

### Get All Employees
```http
GET /employees
```
Returns a list of all employees in the database.

### Add New Employee
```http
POST /employees
```
Request body:
```json
{
  "employeeid": "string",
  "firstname": "string",
  "lastname": "string",
  "email": "string"
}
```
Returns the created employee record.

### Update Employee
```http
PUT /employees/{employee_id}
```
Request body:
```json
{
  "firstname": "string",
  "lastname": "string",
  "email": "string"
}
```
Returns the updated employee record.

### Delete Employee
```http
DELETE /employees/{employee_id}
```
Returns the deleted employee record.

## Environment Variables

- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase anonymous/public API key

## Example Usage

Using curl:
```bash
# Get all employees
curl http://localhost:8000/employees

# Add new employee
curl -X POST http://localhost:8000/employees \
  -H "Content-Type: application/json" \
  -d '{"employeeid": "1", "firstname": "John", "lastname": "Doe", "email": "john@email.com"}'

# Update employee
curl -X PUT http://localhost:8000/employees/1 \
  -H "Content-Type: application/json" \
  -d '{"firstname": "Jane", "lastname": "Doe", "email": "jane@email.com"}'

# Delete employee
curl -X DELETE http://localhost:8000/employees/1
```

## Notes

- This API uses the Supabase `employees` table which should have columns matching the employee model
- The API automatically reloads on code changes when run with `--reload`
- For production use, consider removing `--reload` and using a proper ASGI server

## License

This project is open source and available under the MIT License.