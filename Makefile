up-prod:
	sudo docker compose --rm --env-file .env -f docker-compose.prod.yml up -d

down-prod:
	sudo docker compose --env-file .env -f docker-compose.prod.yml down

pull-prod:
	sudo docker compose -f docker-compose.prod.yml pull

migrate-prod:
	sudo docker compose -f docker-compose.prod.yml exec web ./manage.py migrate

populate_db-prod:
	sudo docker compose -f docker-compose.prod.yml exec web ./manage.py populate_db ./flower_app/bouquets.json

start-prod: pull-prod down-prod up-prod
