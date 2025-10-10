# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the local 'data' directory to the Nginx HTML directory in the container
COPY ./data /usr/share/nginx/html

# Copy the new Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the outside world
EXPOSE 80

# Command to run Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
