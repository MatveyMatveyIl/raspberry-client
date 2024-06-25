all: build down migrate up state

build:
	docker-compose build

down:
	docker-compose down

stop:
	docker-compose stop

up:
	docker-compose up -d

db:
	docker-compose up -d db

daemons:
	bash -c "pipenv run python src/manage.py run_daemons"

state:
	docker-compose run --rm app python src/manage.py init_state

init:
	cp .env.example .env

pull:
	git pull

test:
	docker-compose run --rm app pytest src/

migrate:
	docker-compose run --rm app python src/manage.py migrate $(if $m, api $m,)

makemigrations:
	docker-compose run --rm app bash -c 'python src/manage.py makemigrations && sudo chown -R ${USER} src/app/migrations/'

createsuperuser:
	docker-compose run --rm app python src/manage.py createsuperuser

collectstatic:
	docker-compose run --rm app python src/manage.py collectstatic --no-input

dev:
	docker-compose up app

command:
	docker-compose run --rm app python src/manage.py ${c}

shell:
	docker-compose run --rm app python src/manage.py shell

bash:
	docker-compose run --rm app bash

debug:
	docker-compose run --rm app python src/manage.py debug

piplock:
	pipenv install
	sudo chown -R ${USER} Pipfile.lock

lint:
	docker-compose run --rm app bash -c 'isort . && flake8 --config setup.cfg && black --config pyproject.toml .'

check_lint:
	docker-compose run --rm app bash -c 'sort --check --diff . && flake8 --config setup.cfg && black --check --config pyproject.toml .'
