# Use a lightweight Node.js image
FROM node:14

# Create and set the working directory
WORKDIR /app

# Copy static files to the container
COPY index.html /app

# Install a basic web server (like serve)
RUN npm install -g serve

# Expose the frontend on port 3000
EXPOSE 3000

# Start the static website
CMD ["serve", "-s", "."]
