.PHONY: install run test seed_db clean

install:
	pipenv install

run: 
	pipenv run uvicorn app.app:app --reload  

test:
	pipenv run pytest

seed_db:
	pipenv run python ./app/utils/seed_db.py

clean:
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} +
