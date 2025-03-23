start:
		python3 manage.py runserver

migrations:
		python3 manage.py makemigrations

migrate:
		python3 manage.py migrate

shell:
		python3 manage.py shell

admin:
		python3 manage.py createsuperuser

redis-stop:
		sudo service redis-server stop

redis:
		redis-server

celery-run:
		celery -A nda worker -l info
