Creating a simple web 2 tier web application from 2 containers [WebApp, and Redis] using Docker Compose.
The application utilizes the Flask Python framework to build a web application that counts the number of visits to a website.
Redis database is used for the database tier to keep track of the counter
The High Level Design for this web application architecture is below with description:
<img alt="image" src="https://github.com/user-attachments/assets/2c3d311b-9a97-4f4b-8046-828f0fbbe5c8" />

	•	Flask serves as the web framework for building the web application.
	•	The application’s primary function is to count website visits.
	•	Redis acts as the cache/database layer to store and manage the visit counter data.
