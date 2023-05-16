# Contributing

## Install Mamba

Check https://mamba.readthedocs.io/en/latest/installation.html#automatic-installation for updated instructions.

```bash
curl micro.mamba.pm/install.sh | bash
```

## Install Dependencies

```bash
micromamba install \
    -y \
    -c conda-forge \
    -n orc2-status-bot \
    -f requirements.dev.txt \
    -f requirements.prod.txt
```

## Run local

```bash
micromamba activate orc2-status-bot
```

```bash
export SECRET_GITHUB_TOKEN=REDACTED
```

```bash
pytest \
    --binder-url https://notebooks.gesis.org/binder/ \
    --hub-url https://notebooks.gesis.org/binder/jupyter/ \
    test
```
