# File Server with Docker and Nginx

This project sets up a simple file server using Docker and Nginx. It serves the contents of the `data` directory and allows for directory browsing.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/johnnyhng/WebFileBrowser.git
    cd WebFileBrowser
    ```

2.  **Add files to the `data` directory:**
    Place any files you want to serve into the `data` directory.

3.  **Build and start the file server:**
    ```bash
    docker-compose up -d --build
    ```
    This command will build the Docker image and start the container in detached mode. The file server will be accessible at [http://localhost:8080](http://localhost:8080).

4.  **Stop the file server:**
    ```bash
    docker-compose down
    ```
    This command will stop and remove the container and any associated networks.
