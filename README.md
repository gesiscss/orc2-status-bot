# Open Research Computing v2  Status Bot

This repository has the code to run a bot on [GitLab CI](https://docs.gitlab.com/ee/ci/) and [GitHub Actions](https://github.com/features/actions).

Source: https://git.gesis.org/ilcm/orc2-status-bot

Mirror: https://github.com/gesiscss/orc2-status-bot

## Bot

It's a collection of tests, see [`test`](test).

### Setup local

```bash
conda env create --file environment.yml
```

```bash
conda activate orc2-status-bot
```

### Run local

```bash
export SECRET_GITHUB_TOKEN=REDACTED
pytest --binder-url https://notebooks.gesis.org/binder/ --hub-url https://notebooks.gesis.org/binder/jupyter/ test
```

## GitLab

See [`.gitlab-ci.yml`](.gitlab-ci.yml).

## GitHub

See [`.github/workflows/status-verification.yml`](.github/workflows/status-verification.yml).
