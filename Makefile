.PHONY: clean style quality test style

# Global variables
PROJECT_NAME = project_template
PYTHON_INTERPRETER = python3
CHECK_DIRS := tests project_template


# Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


# Format source code automatically and check is there are any problems left that need manual fixing
style:
	black $(CHECK_DIRS)
	isort $(CHECK_DIRS)


# Runs checks on all files
quality:
	black --check $(CHECK_DIRS)
	isort --check-only $(CHECK_DIRS)
	pylint $(CHECK_DIRS)


# Run tests for the library
test:
	$(PYTHON_INTERPRETER) -m unittest


# Check that docs can build
docs:
	cd docs && make html SPHINXOPTS="-W -j 4"