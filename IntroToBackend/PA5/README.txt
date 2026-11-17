Name: Avi Sharma
NetID: as4632

Challenges Attempted (Tier I/II/III): None
Working Endpoint: GET /api/courses/ (http://localhost:8000/api/courses/)
Your Docker Hub Repository Link: https://hub.docker.com/r/av1sharma/pa5-cms

Questions:
Explain the concept of containerization in your own words.
Containerization packages an application with its dependencies and runtime so
it can run consistently on different machines. Containers isolate the app's
processes and filesystem while sharing the host's kernel instead of needing
a complete guest operating system for every app.

What is the difference between a Docker image and a Docker container?
An image is a read-only template containing the application's files, runtime,
dependencies, and startup configuration. A container is an instance created
from that image, with its own writable layer, that can be started and stopped.

What is the command to list all Docker images?
docker image ls -a

What is the command to list all Docker containers?
docker container ls -a
The -a flag includes stopped containers.

What is a Docker tag and what is it used for?
A tag is a named reference to an image, such as latest or v1. It lets us identify
and select a version when building, pushing, or pulling an image. Tags can be
updated to refer to a newer image; they are not immutable version guarantees.

What is Docker Hub and what is it used for?
Docker Hub is a hosted registry for storing and sharing container images.
Developers push images to repositories, and other machines pull those images
to run the packaged application.

What is Docker compose used for?
Docker Compose defines an application's services, images, ports, networks,
and volumes in a YAML file. It starts and manages those services together.
This project uses Compose to run the CMS image and persist its SQLite database.

What is the difference between the RUN and CMD commands?
RUN executes a command while building the image, such as installing packages,
and records its filesystem changes in an image layer. CMD specifies the default
command to execute when a container starts and can be overridden at runtime.

