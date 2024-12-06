.PHONY: test
test:
	docker exec fastapi_app pytest

.PHONY: app
app:
	docker-compose -f docker-compose/storage.yaml -f docker-compose/app.yaml up --build -d && docker exec fastapi_app python3.8 src/load_templates.py

