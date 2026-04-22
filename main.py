from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI() #object of FastAPI class is created and stored in the variable app




class Patient(BaseModel): 

    id: Annotated[str, Field(..., description='ID of the patient', example='P001')]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City of residence of the patient')]
    age: Annotated[int, Field(..., description='Age of the patient', ge=0, le=120)]
    gender: Annotated[Literal['male', 'female', 'Other'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., description='Height of the patient in mtrs', gt=0)]
    weight: Annotated[float, Field(..., description='Weight of the patient in kg', gt=0)]

    @computed_field
    @property
    def bmi(self) -> float: #computed field ka naam hoga bmi, isse self milega aur ye return float karega
        bmi = round(self.weight/(self.height ** 2), 2)
        return bmi
    

    @computed_field   #this field will be computed based on the value of bmi, it will return a string value based on the bmi value. Even if there is no BMI Value rn, if the Body Verdict is called, the verdict will will trigger the BMI Function and the BMI will be calculated and then the verdict will be returned based on the BMI value
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal Weight'
        elif self.bmi < 30:
            return 'Overweight'   
        else:
            return 'Obese'

# Vid 7
# Second Pydantic Model | Patient Update
class PatientUpdate(BaseModel):

    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    # This function can be used to load data from a database or a file
    with open('patients.json', 'r') as f: #r means read mode
        data = json.load(f)

        return data

def save_data(data):
    # This function can be used to save data to a database or a file
    with open('patients.json', 'w') as f: #w means write mode
        json.dump(data, f)


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



# POST Endpoint

@app.post('/create')
def create_patient(patient: Patient): #the json data sent by the client will be stored in the variable called patient, and the Data Type of the patient variable is 'Patient' which is a Pydantic model defined above, so the incoming json data will be validated against the Patient model

    # load existing data
    data = load_data()

    # Check if patient ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient ID already exists')

    # Add new patient to data, merging new data to existing data
    # since the existing data is a dict, and patient is an pydantic model, so we will now add the pydantic model in the existing data
    # step 1: convert the pydantic model to a dict using the .dict() method, this will give us a dictionary representation of the patient data
    data[patient.id] = patient.model_dump(exclude={'id'}) #new patient added to out existing db

    #save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'}) 



@app.put('/edit/{patient_id}') #the patient_id is a path parameter that will be passed in the URL which is a dynamic variable
def update_patient(patient_id: str, patient_update: PatientUpdate): #patient_update is the request body, client will send the new info of patient and we will recieve it here in patient_update variable, which we previously defined as a pydantic model above
    
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    existing_patient_info = data[patient_id] #took the existing patient data of the patient_id provide  by user and stored it in the variable existing_patient_info

    update_patient_info = patient_update.model_dump(exclude_unset=True) #this will give us a dict of only those fields which are being updated, the fields which are not being updated will not be included in the dict
    #exclude_unset=True is used to exclude the fields which are not being updated, so that we only get the fields which are being updated in the update_patient_info dict

    #now we have 2 dict, 1st existing_patient_info dict which has the existing patient data, and 2nd update_patient_info dict which has the new patient data which is being updated by the user, now we have to merge these 2 dict, so that we get the updated patient data

    for key, value in update_patient_info.items():
        existing_patient_info[key] = value #this will update the existing patient info with the new values
    # here we performed loop in Update Dict but we are changing in the existing dict

    #after this above loop we will have the updated patient data in the existing_patient_info dict, now we have to put the updated patient data back to our main data where the patient_id is the key and the updated patient data is the value, so that our main data will also get updated with the new patient data
    #it is simple, but for us, we'll have to update the BMI and the verdict!

    #we will now convert the updated patient data (existing_patient_info) to a new pydantic model, because of this conversion the computed fields will automically get calculated 
    # existing_patient_info -> pydantic object -> updated bmi + verdict  
    existing_patient_info['id'] = patient_id #since the id is not a part of the update_patient_info dict, we have to add it manually to the existing_patient_info dict, so that when we convert it to a pydantic model, it will have the id field as well, which is required in the Patient model otherwise we would get an error
    patient_pydantic_obj = Patient(**existing_patient_info) #this will convert the existing_patient_info dict to a pydantic model
    # -> pydantic object -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id') #this will convert the pydantic model back to a dict, but we will exclude the id field because we don't want to update the id field, we only want to update the other fields, and the id field will remain the same

    #add this dict to data
    data[patient_id] = existing_patient_info

    #save the data
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient updated'})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient deleted'})