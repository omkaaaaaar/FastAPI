from fastapi import FastAPI
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
