# Fastapi Microservice Template

This is a template for creating microservices with `FastAPI`.

## Description

This template uses cookiecutter for creating the project and provides a basic directory structure to create microservices, separating routers and API versioning.

The dependencies are handled with `poetry` with `fastapi` and `uvicorn` packages pre-defined.

## Getting Started

### Dependencies

-   Linux
-   python
-   poetry
-   cookiecutter

### Installing

Once `cookiecutter` is installed, you can download this repository with it:

```bash
cookiecutter git@github.com:ArturLinnik/fastapi-microservice-template.git
```

Then, after filling the different fields that `cookiecutter` needs, you have to enter to the new directory

```bash
cd <directory-name>
```

give permissions of execution to `setup.sh`

```bash
chmod +x setup.sh
```

execute `setup.sh` and enter the virtual environment

```bash
./setup.sh && source .venv/bin/activate
```

### Executing program

In order to execute the example of the template you can run `python3 run.py`.

Then, you can verify that it is working by opening in the browser `http://localhost:8000/docs`.

## Help

-   If you haven't configured `ssh` in your machine you can use `cookiecutter` with HTTPS

-   You can install `cookiecutter` with:

```bash
pip install cookiecutter
```
-   If `cookiecutter` is not in yout PATH you can either add it to your PATH

```bash
PATH=$PATH:$HOME/.local/bin
```

 or use it like: 
 
 ```bash
 python -m cookiecutter ...
 ```
 
 This way you will need to repeat the command every time you enter a new terminal, for avoiding that, you can put it in your `.zshrc` or your `.bashrc`.

## Authors

-   Artur Linnik
-   [@ArturLinnik](https://github.com/ArturLinnik)
