build:
	docker build --tag notes-edu:latest .

docker-run-dev:
	docker run --env-file ./.env.dev --publish 5000:8080 --publish 5001:91 --name notes-edu notes-edu:latest

docker-run-prod:
	docker run --env-file ./.env.prod --publish 5000:8080 --publish 5001:9191 --name notes-edu notes-edu:latest

clean:
	docker rm notes-edu
	docker rmi notes-edu:latest