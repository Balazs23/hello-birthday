# Project

# Requirements

- <username> must contain only letters. 
- YYYY-MM-DD must be a date before the today date.
- Request content: `{ “dateOfBirth”: “YYYY-MM-DD” }`
- Response Examples
    - If username’s birthday is in N days: `{ “message”: “Hello, <username>! Your birthday is in N day(s)”}`
    - If username’s birthday is today: `{ “message”: “Hello, <username>! Happy birthday!” }`


## Organization 
------------

    │
    ├── README.md
    ├── /.devcontainer
    │   ├── /library-scripts                        <- install scripts for devcontainer
    │   ├── cloudrun.env                            <- parameters for GCP environment
    │   ├── cloudrun.env                            <- devcontainer env variables
    │   ├── devcontainer.json                       <- devcontainer configuration
    │   ├── docker-compose.devcontainer.yml         <- devcontainer compose file for PSQL service
    │   └── Dockerfile                              <- container file
    ├── /.github
    │   └── /worfklows                              <- GitHub Actions files
    ├── /.vscode
    │   ├── launch.json                             <- IDE Debugger configuration
    │   └── settings.json                           <- IDE settings
    ├── /docs                                       <- Documentation of details
    ├── /scripts
    │   ├── build.sh                                <- local container image builder
    │   ├── clean.sh                                <- remove local container
    │   ├── common.sh                               <- shared variables for scripts
    │   ├── infra-prod.sh                           <- infrastucture deployment
    │   ├── init-gcloud.sh                          <- set credentials for GCP project
    │   ├── init.sh                                 <- install application required lib(s)
    │   ├── preview.sh                              <- deploys application for review with url
    │   ├── start.sh                                <- start application in local built container
    │   └── test.sh                                 <- application unit tests
    ├── /src
    │   ├── /core
    │   │   ├── __init__.py
    │   │   ├── exceptions.py                       <- ORM exceptions
    │   │   └── user.py                             <- Implemented ORM methods for 'User' model
    │   ├── endpoints
    │   │   ├── __init__.py
    │   │   └── hello.py                            <- Endpoint HTTP API implementation
    │   ├── models
    │   │   ├── __init__.py
    │   │   └── user.py                             <- 'User' model implementation
    │   ├── schemas
    │   │   ├── __init__.py
    │   │   ├── base.py                             <- Base configuration for requrest and response schemas
    │   │   ├── hello.py                            <- 'hello' endpoint response schema(s)
    │   │   └── user.py                             <- 'user' request schema(s)
    │   ├── __init__.py
    │   ├── api.py                                  <- Main python file to run the app
    │   └── settings.py                             <- Application settings handler
    ├── terragrunt
    │   ├── _envcommon                              <- Environments shared parameters
    │   │   ├── cloudrun.hcl
    │   │   └── database.hcl
    │   ├── _resources                              <- Terraform modules
    │   │   ├── cloudrun
    │   │   │   ├── main.tf
    │   │   │   └── vars.tf
    │   │   └── database
    │   │       ├── main.tf
    │   │       ├── outputs.tf
    │   │       └── vars.tf
    │   ├── prod                                    <- Production environment
    │   │   ├── europe-west3
    │   │   │   ├── prod
    │   │   │   │   ├── cloudrun
    │   │   │   │   │   └── terragrunt.hcl
    │   │   │   │   ├── database
    │   │   │   │   │   └── terragrunt.hcl
    │   │   │   │   └── env.hcl
    │   │   │   └── region.hcl
    │   │   └── project.hcl
    │   ├── readme.md
    │   └── terragrunt.hcl                          <- Main terragrunt file
    ├── tests
    │   ├── conftest.py                             <- HTTP TestClient
    │   ├── test_endpoints.py                       <- HTTP endpoint tests
    │   ├── test_models.py                          <- Model(s) function(s) test
    │   └── test_schemas.py                         <- Schema(s) validator(s) test
    ├── CHANGELOG.md
    ├── mypy.ini
    ├── project.toml
    ├── pytest.ini
    ├── requirements.txt                            <- Requirements file with the list of the libraries needed
    └── test-requirements.txt                       <- Requirements file with the list of the libraries needed for testing