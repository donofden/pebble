# Makefile for Pebble
#
.DEFAULT_GOAL := explain
explain:
	###     Welcome to Pebble
	@echo " Choose a command to run: "
	@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: ## start the container
	docker-compose up

.PHONY: stop
stop: ## stop the container
	docker-compose down

.PHONY: clean-stop
clean-stop: ## stop the container and clean the data
	docker-compose down -v

.PHONY: push
push: ## push data to metrics
	python push.py
