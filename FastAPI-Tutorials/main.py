from fastapi import FastAPI

app = FastAPI() #object of FastAPI class is created and stored in the variable app

@app.get("/") # Define a GET endpoint at the root URL ("/"), the get signifies that this endpoint will respond to GET requests
#to fetch data from the server get request is used and to send data to the server post request is used
def hello():
    return {'message':'Hello World'} #return a JSON response with a message key and a value of "Hello, World!"

