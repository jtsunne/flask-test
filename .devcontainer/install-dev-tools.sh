#!/bin/bash

set -ex

pip install poetry

POETRY_VIRTUALENVS_CREATE=false poetry install