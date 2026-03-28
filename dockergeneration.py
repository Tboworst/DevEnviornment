# Each function returns a Dockerfile as a string for the given backend language.
# Dockerfiles tell Docker how to build and run your app inside a container.

def generate_dockerfile_python(name):
    # python:3.12-slim is a lightweight Python image
    # We copy requirements.txt first so Docker can cache the install step
    return """FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
"""

def generate_dockerfile_go(name):
    # golang:1.21-alpine is a small Go image
    # We compile the binary with go build, then run it directly
    return f"""FROM golang:1.21-alpine

WORKDIR /app

COPY go.mod .
RUN go mod download

COPY . .

RUN go build -o {name} .

CMD ["./{name}"]
"""

def generate_dockerfile_java(name):
    # Maven handles building and packaging the Java project into a jar
    return f"""FROM maven:3.9-eclipse-temurin-21

WORKDIR /app

COPY pom.xml .
RUN mvn dependency:resolve

COPY . .
RUN mvn package -DskipTests

CMD ["java", "-jar", "target/{name}-1.0.jar"]
"""

def generate_dockerfile_ts(name):
    # Node Alpine is a lightweight Node image
    # ts-node runs TypeScript directly without compiling first
    return """FROM node:20-alpine

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

CMD ["npx", "ts-node", "main.ts"]
"""
