from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI() #object of FastAPI class is created and stored in the variable app

def load_data():
    # This function can be used to load data from a database or a file
    with open('patients.json', 'r') as f: #r means read mode
        data = json.load(f)

        return data


@app.get("/") # Define a GET endpoint at the root URL ("/"), the get signifies that this endpoint will respond to GET requests
#to fetch data from the server get request is used and to send data to the server post request is used
def hello():
    return {'message':'Patient Management System API'} #return a JSON response with a message key and a value of "Hello, World!"


@app.get("/about") # Define another GET endpoint at the URL "/about"
def about():
    return {'message': 'Fully functional API to manage your patient records'} #return a JSON response with a message key and a value of "Hello, I am Omkar"


@app.get('/view')
def view():
    data = load_data() # Call the load_data function to get the data

    return data # Return the data as a JSON response

#Path Parameters:
@app.get('/patient/{patient_id}') # the patient_id is a path parameter that will be passed in the URL which is a dynamic variable
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')): # the patient_id is defined as a string, 
#the Path() fn is called here, the ... signifies that the path param is required, it will be shown in the doc
    data = load_data() #to get the data

    if patient_id in data: # Check if the patient_id exists in the data
        return data[patient_id] #if it exists, then the json data will be returned
    raise HTTPException(status_code = 404, detail='Patient not found')


#Query Parameters:
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='Sort in asc or desc oreder')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Ivaild field, select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order, select between asc and desc')
    
    data = load_data()

    sort_order= True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data