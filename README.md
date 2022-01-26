Docker build : 

Run the docker build command in the directory containing the Dockerfile. 

docker build -t PythonApp .



Helm Chart:

helm create mypython

Edit the values.yaml file 

Image:
Repository : 
path for the docker image


Deploying to the cluster:

kubectl cluster-info

helm install --name Deploy1 ./mypython/PythonApp
