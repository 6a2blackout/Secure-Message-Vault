.PHONY: install run clean

install:
	pip install flask flask-cors pycryptodome

run:
	@echo "Starting Flask server..."
	@echo "Open http://localhost:5000 in your browser"
	python app.py

clean:
	rm -f Users.json
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete