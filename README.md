# mcloud1
master en contenedores


#Conectarse al servidor: 

ssh -i docker.pem azureuser@20.185.177.248

#Crear carpeta

mkdir NOMBRE
cd NOMBRE

# clonar repo
git clone https://github.com/gmacastil/mcloud1.git

# Compilar (omitir)

# Construir la imagen
docker build . -t NOMBRE:TAG

# Subir la imagen
docker tag NOMBRE:TAG DOCKERHUB/NOMBRE:TAG
docker push DOCKERHUB/NOMBRE:TAG


