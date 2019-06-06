dev-build:
	docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml build --no-cache

dev:
	docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml up

test:
	./python-tests.sh