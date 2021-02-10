.PHONY: clean data lint style test

# Global variables
PROJECT_NAME = project_template
PYTHON_INTERPRETER = python3

CHECK_DIRS := tests src


# Install Python Dependencies
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

# Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) src/data/make_dataset.py data/raw data/processed

# Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Lint using flake8
lint:
	flake8 src

# Format source code automatically
style:
	black --line-length 119 --target-version py36 $(CHECK_DIRS)
	isort $(CHECK_DIRS)

# this target runs checks on all files
quality:
	black --check $(CHECK_DIRS)
	isort --check-only $(CHECK_DIRS)
	flake8 $(CHECK_DIRS)

# Run tests for the library
test:
	python -m pytest -n auto --dist=loadfile -s -v ./tests/

# Check that docs can build
docs:
	cd docs && make html SPHINXOPTS="-W -j 4"