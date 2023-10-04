# Dockerizing a Django Application with Gunicorn

This repository demonstrates how to Dockerize a Django application using Gunicorn as the web server. It provides a solution to the issue reported by user Rohit Gajula on StackOverflow.

## StackOverflow Issue

The user Rohit Gajula encountered an error while trying to use Docker Compose for a Django application. The error message indicated a problem with loading metadata for the Docker image. The StackOverflow question can be found [here](https://stackoverflow.com/questions/77228331/why-is-docker-compose-failing-with-error-internal-load-metadata-for-docker-i).

## Solution Overview

The issue was resolved by updating the Dockerfile to use Gunicorn as the web server to serve the Django application. Here's a brief overview of the solution:

1. **Dockerfile Update**:
   - Gunicorn was installed and configured to run the Django application.
   - The `CMD` instruction was updated to use Gunicorn to serve the application.
   - The Dockerfile was rebuilt to apply these changes.

2. **Project Structure**:
   - The Django project structure was confirmed to match the expected layout, ensuring the correct import paths.

3. **Docker Compose Integration**:
   - Docker Compose was added to streamline the deployment process.
   - The `docker-compose.yaml` file was updated to mount the application code into the Docker container and properly run Gunicorn.

#### How to Use This Repository

1. Clone this repository:
   ```bash
   git clone https://github.com/hugolesta/django-sample.git
   cd django-sample


#### Build the Docker image:

```bash
docker-compose build
```

#### Run the Docker container:

```bash

docker-compose up
```

#### Access the Django application:
Open your web browser and go to http://localhost:8000.


### Contributors
[Hugo Lesta](https://github.com/hugolesta)
