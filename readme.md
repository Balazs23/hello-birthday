# Hello World microservice :rocket:

<div align="center">

<!---
[![CircleCI](https://circleci.com/gh/......)](https://circleci.com/gh/...)
[![codecov](https://codecov.io/gh/.../........)](https://codecov.io/gh/.....)
[![Maintainability](https://api.codeclimate.com/v1/badges/......)](https://codeclimate.com/repos/....)
-->

![Python: 3.10](https://img.shields.io/badge/python-3.10-informational.svg)
[![CI](https://github.com/Balazs23/hello-birthday/actions/workflows/code-quality.yml/badge.svg)](https://github.com/Balazs23/hello-birthday/actions/workflows/code-quality.yml)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Balazs23/a6abaa6f4b8ef5450a7e9fc531c179a3/raw/pytest-coverage-comment__main.json)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![mypy: checked](https://img.shields.io/badge/mypy-checked-informational.svg)](http://mypy-lang.org/)


</div>

> ### The application codebase using [FastAPI](https://github.com/tiangolo/fastapi) + [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) to expose HTTP-based APIs. Current setup is designed supports [Google Cloud Platform](https://cloud.google.com) services and the infrastructure is managed by [Terragrunt](https://terragrunt.gruntwork.io)(IaC).


:open_file_folder: Project overview

This Hello-World style application is a Birthday microservice where you can set users birthday and get it back with custom response, based on the day of the birthday. **More details** is at [project documentation](docs/Project.md) like requirement and folders organization.

## :books: Consult the API documentation 
To consult the API documentation just type the following address in a browser.

```
http://localhost:8080/docs/
```

![](docs/img/swagger1.png)

**Endpoints available at `http://localhost:8080/{URI}`**:

|Method|URI|Description|
|------|---|-----------|
| GET | /docs | Application API swagger UI |
| GET | /health | Application health-check endpoint |
| GET | /hello/{username} | Retrieve data from the DB given an username |
| PUT | /hello/{username} | Insert or Update user data in the DB |
| GET | /openapi.json | OpenAPI schema definition |

Run the microservice with the command:
```
./scripts/start.sh
```

**Details of documentation** is at [/docs](/docs) folder

## Getting Started

### :hammer: Development

- [Install Visual Studio Code](https://code.visualstudio.com/download) with [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
- [Install Docker](https://docs.docker.com/engine/install/) (necessary to run as a container instance)
- [Open folder](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container) in container

**more details** is at [development documentation](docs/Development.md)

### :bulb: Useful scripts

- Init credentials for deployments: `./scripts/init.sh`
- Deploy infrastructure into GCP: `./scripts/infra-prod.sh`
- Deploy application for preview: `./scripts/preview.sh`
- Switch preview to production: `./scripts/production.sh`

**more details** is at [/docs](/docs) folder
## :soon: Coming Soon

- [ ] Pipelines
- [ ] Performance measurements
