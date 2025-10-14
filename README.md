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
