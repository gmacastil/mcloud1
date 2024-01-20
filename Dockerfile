FROM openjdk:17.0.20-slim
COPY target/*.jar micro.jar
CMD [ "java","-jar","micro.jar" ]