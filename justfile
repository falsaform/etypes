set positional-arguments := true

_default:
    @just --list --unsorted

poetry *args:
    docker compose exec development poetry {{ args }}

build *args:
    docker compose build {{args}}

build-package:
    #!/usr/bin/env bash
    just poetry build

# to publish package first run `just poetry config pypi-token.pypi <AUTH_PYPI_TOKEN>`
publish-package:
    #!/usr/bin/env bash
    just poetry publish

up *args:
    docker compose up {{args}}

# hello world
bash *args:
    docker compose exec development bash {{args}}

test *args:
    #!/bin/bash
    docker compose run --entrypoint "poetry run pytest {{args}}" development

test-ansible *args:
    #!/bin/bash
    docker compose run development ansible-playbook

black *args:
    just poetry run black .

encrypt *args:
    docker compose exec development etypes encrypt {{ args }}

decrypt *args:
    docker compose exec development etypes decrypt {{ args }}

dump *args:
    docker compose exec development etypes dump {{ args }}
