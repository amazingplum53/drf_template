config_path := app/database

migrations:
	$(COMPOSE) exec server ./django_api/manage.py makemigrations 

migrate:
	$(COMPOSE) exec server ./django_api/manage.py migrate 

