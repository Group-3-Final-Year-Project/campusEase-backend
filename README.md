<h1 align=center><strong>CampusEase FastApi Backend</strong></h1>

This is a template repository aimed to kick-start your project with a setup from a real-world application! This template utilizes the following tech stack:

- 🐳 [Dockerized](https://www.docker.com/)
- 🐘 [Asynchronous PostgreSQL](https://www.postgresql.org/docs/current/libpq-async.html)
- 🐍 [FastAPI](https://fastapi.tiangolo.com/)

When the `Docker` is started, these are the URL addresses:

- Backend Application (API docs) $\rightarrow$ `http://localhost:8001/docs`
- Database editor (Adminer) $\rightarrow$ `http//localhost:8081`

## Setup Guide

This backend application is setup with `Docker`.

1. Before setting up the backend app, please create a new directory called `coverage` for the testing report purpose:

   ```shell
   mkdir coverage
   ```

2. Backend app setup:

   ```shell
   # Creating VENV
   python -m venv anyname

   # Install dependencies
   pip install -r requirements.txt

   # Test run your backend server
   uvicorn src.main:backend_app --reload
   ```

3. Testing with `PyTest`:
   Make sure that you are in the `backend/` directory.

   ```shell
   # For testing without Docker
   pytest

   # For testing within Docker
   docker exec backend_app pytest
   ```

4. `Pre-Commit` setup:

   ```shell
   # Make sure you are in the ROOT project directory
   pre-commit install
   pre-commit autoupdate
   ```

5. Backend app credentials setup:
   If you are not used to VIM or Linux CLI, then ignore the `echo` command and do it manually. All the secret variables for this template are located in `.env.example`.

   If you want to have another name for the secret variables, don't forget to change them also in:

   - `backend/src/config/base.py`
   - `docker-compose.yaml`

   ```shell
   # Make sure you are in the ROOT project directory
   touch .env

   echo "SECRET_VARIABLE=SECRET_VARIABLE_VALUE" >> .env
   ```

6. `CODEOWNERS` setup:
   Go to `.github/` and open `CODEOWNERS` file. This file is to assign the code to a specific team member so you can distribute the weights of the project clearly.

7. Docker setup:

   ```shell
    # Make sure you are in the ROOT project directory
    chmod +x entrypoint.sh

    docker-compose build
    docker-compose up

    # Every time you write a new code, update your container with:
    docker-compose up -d --build
   ```

8. (IMPORTANT) Database setup:

   ```shell
    # (Docker) Generate revision for the database auto-migrations
    docker exec backend_app alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    docker exec backend_app alembic upgrade head    # to register the database classes

    # (Local) Generate revision for the database auto-migrations
    alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    alembic upgrade head    # to register the database classes
   ```

9. Go to https://about.codecov.io/, and sign up with your github to get the `CODECOV_TOKEN`

10. Go to your GitHub and register all the secret variables (look in .env.example) in your repository (`settings` $\rightarrow$ (scroll down a bit) `Secrets` $\rightarrow$ `Actions` $\rightarrow$ `New repository secret`)

**IMPORTANT**: Without the secrets registered in Codecov and GitHub, your `CI` will fail and life will be horrible 🤮🤬
**IMPORTANT**: Remember to always run the container update every once in a while. Without the arguments `-d --build`, your `Docker` dashboard will be full of junk containers!
