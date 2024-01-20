# mcloud1
master en contenedores


#Conectarse al servidor: 

ssh -i docker.pem azureuser@20.185.177.248

#Crear carpeta

mkdir NOMBRE
cd NOMBRE

# clonar repo
git clone https://github.com/gmacastil/mcloud1.git

# actualizar repo
git pull (en la carpeta)

# Compilar (omitir)

# Construir la imagen
docker build . -t NOMBRE:TAG

# Tagging la imagen con el registry
docker tag NOMBRE:TAG DOCKERHUB/NOMBRE:TAG

# Subir la imagen
docker push DOCKERHUB/NOMBRE:TAG

# Taggin de la imagen en otro registry

docker tag NOMBRE:TAG sabadodev.azurecr.io/NOMBRE:TAG

# Subir la imagen

``````
docker login sabadodev.azurecr.io
user: sabadodev
pwd: 2QBtwiiwWjBt6FZFi+bWFS3RWSWhi+hZEtcqHmYIPd+ACRD+gwcA &nbsp;
docker push sabadodev.azurecr.io/NOMBRE:TAG
``````

