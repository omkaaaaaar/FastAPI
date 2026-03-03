# FastAPI

### Topics covered in this repo are in 3 parts

##### Part 1: Fundamentals - (with the help of a project)

##### Part 2: ML Model integrate with FastAPI

##### Part 3: Deployment of ML API (AWS)

---

---

## Part 1: What is an API

---

### Video 1:

#### What is API?

Acc to s/w:
APIs are mechanisms that enable two software components-such as the frontend and the backend of an application-to communicate with each other using a defined set of rules, protocols, and data formats.
Basically a connector between two different software

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

_PROBLEM 2_ and its solution
Since user uses Androids, iOS, Windows. All the DBs for these 3 will be different cause different platforms. But with the API we can simply connect the all 3 different frontends of Android, iOS and Windows with the API layer -> Backend -> DB. Soo that their is no need of multiple structures for different platforms.
Most of the MNCs (googlec, facebook) uses this architecture because it is easy!

###### Solution for the Above problem with API

_Steps :-_ _Stop_ Using *Monolithich Archi*tecture / *Decouple App*lication

- Build Frontend alag se, Build Backend alag se
- That means the Backend will be a different application and the Frontend will be a different application
- Add a layer of API after Backend i.e. DB<-->Backend<-->API, here the APIs are basically endpoints they are basically some special type of functions which are publically available to view and access
- Ex. we created a "/Trains" function which is basically a spl function which is availale on the internet soo anyone can access it
- we wrote in the function that if anyone hit on the url of the train function then what we will do bts is --> we'll call the "Fetch Trains" function of the Backend --> this function will thereafter will go to the DB, it'll bring the data and will submit it to the /Trains endpoint (API) soo the User/public can access it
- The companies will hit the /Trains API url and the above flow will take place and the companies will recieve the data
- We can also apply constraints on the API too soo that no malicious info can transfer
- Since our Frontend is an independen App now, it too can acess the DB/Backend with the help of API now
- the data format we use here is _JSON_ since it is a universal data format. i.e. if Makemytrip is built in Python and Yatra is built in Java sooo the API will need to share the data which both languages can understand, which is "JSON"

##### API - ML Perspective

- The DB was imp in the above cases(s/w cases) but in ML/DL the ML Model is the most imp thing
- Everything else is the same
- Ex. ChatGpt, the OpenAI built this model and wanted to share it to the world
- So inorder to share they cant publicly share the model obviously, soo they used the similar struct like previous above structures
- _Previous ML Monolithic Architecture :-_ ML Model <--> Backend <--> Frontend
- _Present ML API Architecture :-_ ML Model <--> Backend <--> API
- For the multiple platform it is same as the DB based we discussed earlier above in the problem case

---

### Video 2: FastAPI Philosophy

#### FastAPI?

FastAPI is a modern, high-performance web framework for building APIs with Python
