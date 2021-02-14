# Project Template


My template for data science projects

## Project Organization

```
    project_template/   <- Project name.
    │
    ├───data/               <- Keep all versions of data for this project.
    │   ├── external/               <- Data from third party sources.
    │   ├── interim/                <- Intermediate data that has been transformed.
    │   ├── processed/              <- The final, canonical data sets for modeling.
    │   └── raw/                    <- The original, immutable data dump.
    │
    ├───docker/             <- Dockerfiles used to run project in container. If project only had one Dockerfile it can
    │                       moved inside the project without a `docker/` folder.
    │
    ├───docs/               <- A default Sphinx project; see sphinx-doc.org for details
    ├───models/             <- Trained and serialized models, model predictions, or model summaries
    ├───notebooks/          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├───project_template/   <- Source code for use in this project. You can put it in `src` if you preffer.
    │   │                   Has similar name to project name.
    │   │
    │   ├───data/           <- Scripts to deal with data.
    │   │   │   __init__.py         <- Makes data code a Python module.
    │   │   └   make_dataset.py     <- Process data
    │   │
    │   ├───features/       <- Process raw data into features for modeling.
    │   │   │   __init__.py         <- Makes raw data into features code a Python module.
    │   │   └   build_features.py   <- Script to process data to features.
    │   │
    │   ├───models/         <- Scripts for modeling: training and inference
    │   │   │   __init__.py         <- Makes modeling code a Python module.
    │   │   │   predict_model.py    <- Script for making model predicitons.
    │   │   └   train_model.py      <- Script for training model.
    │   │
    │   ├───visualization/  <- Create exploratory and results oriented visualizations
    │   │   │   __init__.py         <- Makes exploratory and results oriented visualizations code a Python module.
    │   │   └   visualize.py        <- Script to create exploratory and results oriented visualizations. 
    │   │   
    │   │   __init__.py     <- Makes source code a Python module.
    │   └   __main__.py     <- Make the module execute some functionality when run as the entry point of the program.
    │                       Execute this script when running `python project_template`.
    │  
    ├───references          <- Data dictionaries, manuals, and all other explanatory materials.
    ├───reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └───figures/                <- Generated graphics and figures to be used in reporting
    │
    ├───tests               <- Keep all testing code.
    │   └   __init__.py             <- Make testing code a Python module.
    │
    │   README.md           <- The top-level README for developers using this project.
    │   LICENSE             <- Project license.
    │   Makefile            <- Makefile with commands like `make data` or `make train`.
    │   setup.cfg           <- Ini file that contains option defaults for setup.py commands.
    │   setup.py            <- Makes project pip installable (pip install -e .) so source code can be imported.
    └   requierements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                            generated with `pip freeze > requirements.txt`
```