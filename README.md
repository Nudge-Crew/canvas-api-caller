# Installation Guide
## Virtual Environment
### Linux and MacOS

The venv folder contains all dependencies which are needed to run this project. To enter the venv virtual environment use:

``` source venv/bin/activate ```

If this is the first time running or if anything in the requirements has changed use:

``` virtualenv venv && source venv/bin/activate && pip install -r requirements.txt ```

after installing a new package use: 

``` pip freeze > requirements.txt ```

to update the requirments folder

### Windows
The venv folder contains all dependencies which are needed to run this project. To enter the venv virtual environment use:

``` source venv/bin/activate ```

If this is the first time running or if anything in the requirements has changed use:

``` virtualenv venv && source venv/Scripts/activate && pip install -r requirements.txt ```

after installing a new package use: 

``` pip freeze > requirements.txt ```

to update the requirments folder

#### Important Note
Make sure to have python37 and python37\Scripts added in your environmental path.
Else command such as ```virtualenv venv``` may not work.

Example environmental variables:

![Environmental Variables](https://i.imgur.com/2u3va11.png "Environmental Variables")

## Run Flask
In order to run flask, you just need to execute `flask run`.

# Endpoints
The only endpoint this function has is `/canvas`, here some parameters are expected.

Headers:
* Authorization - Canvas Authorization header / Access Token in Bearer format, as we need access to your Canvas courses.

Parameters;
* Endpoint - Contains the endpoint to the canvas API url after `https://fhict.instructure.com/api/v1/`.
* Canvas related parameters - Parameters expected by canvas itself such as `student_id`.

This should work with most (if not all) canvas endpoints (GET) that use basic parameters.
