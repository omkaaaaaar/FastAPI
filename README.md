# FastAPI

### Topics covered in this repo are in 3 parts

##### Part 1: Fundamentals - (with the help of a project)

##### Part 2: ML Model integrate with FastAPI

##### Part 3: Deployment of ML API (AWS)

---

---

## Part 1:

### Video 1:

#### What is API?

Acc to s/w:
APIs are mechanisms that enable two software components-such as the frontend and the backend of an application-to communicate with each other using a defined set of rules, protocols, and data formats.
Basically a connector between two different software

---

#### Need for APIs

###### Pre API Era

In _Monolithic Architecture_ (application), here in this architecture a file will have everything innit a _Frontend_ Folder(it'll have components, style, utils, etc folders in it) and a _Backend_ Folder(it'll have controllers, models, routes, service, etc folders in it)
sooooo,
_Db <--> Backend <--> Frontend_
All of these 3 can communicate with each other without needing of an API
The Backend and Frontend is _Tightly Coupled_ here, which means if any component goes through a problem/change then affect the whole project
Before APIs websites were developed with the help of _Monolithic Architecture_ only

###### Problem Case for the need of APIs

Ex -> we have the govt. IRTC website and we have a DB which has the info about the trains and the timings
This DB is connected with the Backend and the Frontend
The Backend we have uses the chosen filter, protocolsm rules, data formats, etc. to only show/provide only the specific info to user to secure the confidential data.

Now, the companies like Makemytrip, Yatra, ixigo approached us to share them the data for money behind per search of the train so that the users of their platform can access the timings of the trains and can book their tickets from their websites
But, we can't give them the access to the govt.-confidential data sooo we give them the _access to the Backend_ soo that they can only access the selected data that we decided to show them

But since the Backend we have now is not an independent application and it is tightly coupled with the Frontend and the DB resulting into failure of this giving access to the Backend Technique (we can't share the data of the DB to any other application outside out our Monolithic Architecture)

This results into the loss of profit for the IRCTC Website cause they can't share their DATA to the other companies to earn more money,
This problem is Solved using APIs

###### Solution for the Above problem with API
