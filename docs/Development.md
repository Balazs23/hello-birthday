# Development

For better interoperability terms the projects is using Visual Studio Code devcontainer feature. Also possible to develop, run and test the code on a local machine. Current state the code and the container is compatible with `amd64` and `arm64` architecture

## Devcontainer development

All the configurations of the development environment is placed in `.devcontainer` folder. For local testing VSCode is using a [docker-compose](https://docs.docker.com/compose/) file to provide PSQL instance for the application. The `devcontainer.env` file sets all runtime environment variable during the development, `cloudrun.env` is usabe in case for reaching the production SQL instance.

### Pre-requisites

- [Install Docker](https://docs.docker.com/engine/install/) (necessary to run as a container instance)
- [Install Visual Studio Code](https://code.visualstudio.com/download) with [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
- [Open folder](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container) in container

### Launch and debug application

Using builtin VSCode debugger.

- `FastAPI - NoSQL`: Application start without DB access, using SQLite database driver, wirte all data into `test.db` file
- `FastAPI - PSQL`: Application start using PSQL service, which is configured by compose file.
- `FastAPI - CloudSQL`: Application start using production database access. This requires extra steps, like installing [cloud-sql-proxy](https://github.com/GoogleCloudPlatform/cloud-sql-proxy) setting IAM authentication and provide preauthentication with [gcloud CLI](https://cloud.google.com/sdk/gcloud)
- `Python: Debug Tests`: Run opened test, use with`./tests/*.py` files

### Testing

Prebuilt script file installs required libs for testing and runs pytest command with coverage output: `./scripts/test.sh`

## Local development

### Pre-requisites

- Install [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- Install [PIP](https://pip.pypa.io/en/stable/) : `python -m ensurepip --upgrade`
- Run `./scripts/init.sh` to install all required lib(s)

### Launch and debug application

[pdb](https://docs.python.org/3/library/pdb.html) is a debugger built right into the python standard library. You don't need to install a library.

Start application: `uvicorn api:app --app-dir ./src/ --reload --port 8080`

Add debug breakpoint to code, like

```
@app.get('/')
def root():
    now = datetime.now()
    import pdb; pdb.set_trace()
    return { "now": now }
```

and restart `uvicorn` with extra `--debug` flag

### Testing

You can use the same script: `./scripts/test.sh`

## Contribute 

For contributing make a fork from reposity, open a fetature branch and the end of the development create a pull request into main repository. You can follow decribed [Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)