FROM maven:3.8.3-openjdk-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src/ ./src/
RUN mvn package -DskipTests

FROM openjdk:17-alpine
WORKDIR /app
RUN apk update && apk add curl
COPY --from=build /app/target/idrive-0.0.1-SNAPSHOT.jar .
EXPOSE 8080
ADD $PWD/flag.txt /flag.txt

CMD ["java", "-jar", "idrive-0.0.1-SNAPSHOT.jar"]
