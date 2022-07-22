# Cloud Mask Replacement Task  
This repository is being formed to demonstrate the solution to the Cloud Mask Replacement Task
 - Code can be tested via the following methods described
   - Virtual environment: 
   - Docker Method: 
   - Jupyter environemnt:
     - Via Docker 
     - Local 

## Virtual Environment
 > - ``` python3 -m venv venv``` 
 > - ``` source venv/activate```
 > - ``` ./install.sh ``` # For GDAL 
 > - ``` pip install -r requirements.txt ```
 
If all the steps are successful you can use the virtual environment as your projects default interpreter to test the codebase. 
From the settings menu of your favourite Python IDE change the interpreter to the newly created ```venv``` folder.

## Docker Method
> For the docker method a dedicated ubuntu base image has been used. All the neceassary libraries and virtual environment is being handled via docker image. Required python libraries, necessary local libraries and the virtual environment is being prepared for you within the image. 
> - ```docker-compose -f docker-compose.yml up -d ```
> - ```Change interpreter from virtual environment to docker environment```
> - ![alt text](https://github.com/KenanBolat/cloud_mask_replacement/blob/main/media/docker_compose_interpreter.png)



