# Generating the documentation

To generate the documentation, you first have to build it. Several packages are necessary to build the doc, you can install them with the following command, at the root of the code repository:

```bash
pip install -e ".[docs]"
```

To test if the documentation can build:

```bash
mkdocs build --config-file mkdocs.yml
```

To deploy the docs on github pages:

```bash
mkdocs gh-deploy --config-file mkdocs.yml
```

