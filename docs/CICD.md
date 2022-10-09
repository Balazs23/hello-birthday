# CICD

The joining of development and operations) and combines the practices of continuous integration and continuous delivery. CI/CD automates much or all of the manual human intervention traditionally needed to get new code from a commit into production such as build, test, and deploy, as well as infrastructure provisioning. 

Fundamentals:
- A single source repository
- Frequent check-ins to main branch
- Automated builds
- Self-testing builds
- Frequent iterations
- Stable testing environments
- Maximum visibility
- Predictable deployments anytime

## Continuous integration (CI)

### [Code quality checks](../.github/workflows/code-quality.yml)
Runs for all open [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to validate formatting and linting of the code itself
- [Black](https://black.readthedocs.io/en/stable/index.html) for code formatting
- [Pylint](https://pylint.pycqa.org/en/latest/) static code analyzer
- [mypy](https://mypy.readthedocs.io/en/stable/) another static code analyzer using the Python 3 annotation syntax (using [PEP 484](https://peps.python.org/pep-0484/) and [PEP 526](https://peps.python.org/pep-0526/) notation)
- [flake8](https://flake8.pycqa.org/en/latest/) Python linting tool

### [Application tests](../.github/workflows/app-test.yml)
Runs for pull request and pushes on `main` branch. Builds the application from the current codebase and runs unit tests from `tests` library, at the end summarize the test coverage with a report. For this approach the pipeline use the same [pytest](https://docs.pytest.org/en/7.1.x/) framework with [mock](https://mock.readthedocs.io/en/latest/) library.

Further enhancement can be also to use [githooks](https://git-scm.com/docs/githooks) which are are scripts that Git executes before or after events such as: **commit**, **push**, and **receive**. Git hooks are a built-in feature - no need to download anything. Git hooks are run locally. Linting can be also done locally before pushing any commit to repository or feature branch, a minimal testing also can be useful.

For better security also recommended to set a pipeline jobs which runs security and vulnerability scanning for the built container despite we are using Google provided build-packs.

## Continuous deployment (CD)
Current state the deployment can be done with the provided scripts, but GitHub also provides option for deploying. 
The following may be a working model in the future:
1. make a `non-prod` environment to deploy all changes from open pull requests
    - similar env with test data, isolated from prod environment
1. all pushes to main branch (merged pull requests) should be deployed as `GREEN` revision
1. running E2E (end to end) tests on the `GREEN` revision to ensure application quality
1. Manual triggered job should split traffic with the given percentage between `BLUE` (current) and `GREEN` (new) revision
    - in any cases, the job can be reverted and rollback traffic to `BLUE`
1. in case of git [release tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) the `GREEN` revision should be marked as `BLUE` and route 100% traffic on it

These steps would also cover the continues delivery process for the application lifecycle.
