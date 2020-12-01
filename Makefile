build:
	docker build --tag notes-edu:latest .

run:
	docker run --env-file ./.env.prod --publish 5000:8080 --publish 5001:9191 --name notes-edu notes-edu:latest

clean:
	docker stop notes-edu
	docker rm notes-edu
	docker rmi notes-edu:latest