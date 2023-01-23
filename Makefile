up:
	sudo docker compose --env-file .env up -d

down:
	sudo docker compose --env-file .env down

pull:
	sudo docker compose pull

migrate:
	sudo docker compose exec web ./manage.py migrate

populate_db-prod:
	sudo docker compose exec web ./manage.py populate_db ./flower_app/bouquets.json

start-prod: pull down up
