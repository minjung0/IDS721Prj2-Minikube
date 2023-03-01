## Individual Project #2: Kubernetes based Microservice

- Create a customized Docker container from the current version of Python that deploys a simple python script.
- Push image to DockerHub, or Cloud based Container Registery (ECR)
- Project should deploy automatically to Kubernetes cluster
- Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)  

________

### 1. Microservice to get exchange rates

This service provides the latest exchange rates from your base currency to 161 world currencies using [ExchangeRate-API](https://www.exchangerate-api.com).  
Enter the base currency using a 3-letter abbreviation: e.g. `/USD` or `/EUR`  
You can check all supported currencies and currency codes [here](https://www.exchangerate-api.com/docs/supported-currencies). 

________

### 2. Build and push image to DockerHub

```
docker login -u minjung0
docker build . -t minjung0/ids721_prj2
docker push minjung0/ids721_prj2
```

<img width="831" alt="docker build" src="https://user-images.githubusercontent.com/90014065/222246086-6025bc20-b214-40ab-b8b6-f5c66b4a1283.png">

<img width="804" alt="docker push" src="https://user-images.githubusercontent.com/90014065/222245774-470b8f10-83b2-43cf-976a-cfea32da487c.png">

________

### 3. Deploy with Minikube

1. Start Minikube.

`minikube start`

2. Start a dashboard.

`minikube dashboard --url`

<img width="535" alt="dashboard" src="https://user-images.githubusercontent.com/90014065/222252140-a5664822-7035-43af-be52-5b018834b0f8.png">

3. Create a deployment.

`kubectl create deployment rates --image=registry.hub.docker.com/minjung0/ids721_prj2`

4. View deployments.

`kubectl get deployments`

<img width="690" alt="view deploy" src="https://user-images.githubusercontent.com/90014065/222252418-5e36865d-23dc-4539-b247-dae55be3ac27.png">

5. Create a service and expose it. 

`kubectl expose deployment rates --type=LoadBalancer --port=8080`

6. View services.

`kubectl get service rates`

<img width="532" alt="get service" src="https://user-images.githubusercontent.com/90014065/222252629-b8f63f04-2556-4a0e-8027-bc1efb1fd7e7.png">

7. Check the url of the service.

`minikube service rates --url`

<img width="522" alt="get url" src="https://user-images.githubusercontent.com/90014065/222252930-8d19c645-97d8-471a-b7fb-8ee27a578b10.png">

8. Curl web service.

```
curl http://192.168.49.2:32265
curl http://192.168.49.2:32265/USD
```

<img width="1028" alt="curl1" src="https://user-images.githubusercontent.com/90014065/222253524-27d44425-2905-456b-b19f-ac1fe1bdb044.png">
<img width="572" alt="curl2" src="https://user-images.githubusercontent.com/90014065/222253537-636e16b5-fbe8-48f1-b1fa-7adc0a86fe80.png">

9. Cleanup the service and deployment.

  ```
  kubectl delete service rates
  kubectl delete deployment rates
  minikube stop
  ```
