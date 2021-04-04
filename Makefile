# Makefile for current library.

# Global variables.
PROJECT_NAME = project_template
PYTHON_INTERPRETER = python3
CHECK_DIRS := tests project_template *.py

.PHONY: clean-build
clean-build: ## Remove build artifacts.
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts.
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

.PHONY: style
style: ## Format source code automatically and check is there are any problems left that need manual fixing.
	black $(CHECK_DIRS)
	isort $(CHECK_DIRS)

.PHONY: quality
quality: ## Runs checks on all files.
	@echo "Make sure to run 'style' before to fix any code indentation issues!"
	black --check $(CHECK_DIRS)
	isort --check-only $(CHECK_DIRS)
	pylint $(CHECK_DIRS)

.PHONY: test
test: ## Run tests for the library.
	$(PYTHON_INTERPRETER) -m unittest

.PHONY: docs
docs: ## Rebuild docs automatically and display locally.
	mkdocs serve  --config-file docs/mkdocs.yml

.PHONY: servedocs
servedocs: ## Rebuild docs automatically and push to github.
	mkdocs gh-deploy  --config-file docs/mkdocs.yml --force

.PHONY: help
help: ## Display make help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'