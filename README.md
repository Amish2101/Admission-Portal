# Admission-Portal

Setup Project using Docker
First make sure you have installed docker and docker-compose on your machine. https://docs.docker.com/get-docker/

Clone the project from git repository and move into the project directory.
git clone git@github.com:Amish2101/Admission-Portal.git
cd ap/
Create environment variable file to example file and add your own credentials for third party services.
cp .env.example .env
Then run the following command to setup project using docker:
docker-compose up -d --build
Migrate the database
docker-compose exec web python manage.py migrate
Create a super user with following command; So you can login into the admin site:
docker-compose exec web python manage.py createsuperuser
You can go to the http:///0.0.0.0:8000 to view the application running.

Docker Development
Build the docker containers
docker-compose up -d --build
Run this command to remove double quotes from menu-item name
docker-compose exec web python manage.py remove_quotes
Stop the containers
docker-compose stop
Check the docker containers status
docker-compose ps -a
Check the logs of the docker containers
The below command displays logs of both containers together.

docker-compose logs -f --tail 20
Check the logs for only the database container.

docker-compose logs -f --tail 20 postgres
Check the logs for only the django container.

docker-compose logs -f --tail 20 web
To remove the docker containers
docker-compose down
To remove the docker containers with all the data. Do not use this command. This will removes all the data of database.

docker-compose down -v