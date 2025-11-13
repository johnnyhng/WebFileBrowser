# Flask File Server with Docker, Nginx, and Gunicorn

This project sets up a simple, yet robust, file server using a multi-container Docker application. It uses Flask to handle the application logic, Gunicorn as a production-ready WSGI server, and Nginx as a reverse proxy. The server allows for hierarchical browsing of the `data` directory.

## Architecture

-   **Flask:** A Python web framework used to create the file browsing and download logic.
-   **Gunicorn:** A Python WSGI HTTP Server for UNIX. It's used to serve the Flask application in a production environment.
-   **Nginx:** A high-performance web server, used here as a reverse proxy to forward requests to the Gunicorn server.
-   **Docker & Docker Compose:** Used to containerize the application and orchestrate the multi-container setup.

## Prerequisites

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/johnnyhng/WebFileBrowser.git
    cd WebFileBrowser
    ```

2.  **Add files to the `data` directory:**
    Place any files and directories you want to serve into the `data` directory. You can create any nested structure you like.

3.  **Build and start the file server:**
    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker image for the Flask application and start both the `web` (Flask/Gunicorn) and `nginx` services in detached mode. The file server will be accessible at [http://localhost:8080](http://localhost:8080).

4.  **Stop the file server:**
    ```bash
    docker-compose down
    ```
    This command will stop and remove the containers and any associated networks.

## Configuration

### Changing the Data Directory

By default, the file server serves files from the `./data` directory. If you want to serve files from a different location on your host machine, you can change the volume mapping in the `docker-compose.yml` file.

In `docker-compose.yml`, locate the `web` service and its `volumes` section:

```yaml
services:
  web:
    # ... (other configurations)
    volumes:
      - .:/usr/src/app
      - ./data:/data:ro  # <-- Modify this line
    # ... (other configurations)
```

Change `./data` to the path of the directory you want to serve. For example, to serve a directory named `my_files` located in your home directory, you would change it to:

```yaml
      - ~/my_files:/data:ro
```

After modifying `docker-compose.yml`, rebuild and restart the services for the changes to take effect:

```bash
docker-compose up --build -d
```
