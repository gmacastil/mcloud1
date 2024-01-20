FROM openjdk:17-alpine
COPY target/*.jar micro.jar
CMD [ "java","-jar","micro.jar" ]