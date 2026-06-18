# Cicd Pipeline Builder

Declarative CI/CD pipeline builder for GitHub Actions.

## Features
- YAML-based pipeline definition
- Multi-stage: build → test → deploy
- Matrix builds (OS, runtime versions)
- Secret management integration

## Example
```yaml
pipeline:
  stages:
    - build: {runs-on: ubuntu-latest, steps: [checkout, setup-python, install, build]}
    - test: {needs: build, steps: [pytest, coverage]}
    - deploy: {needs: test, if: branch == main}
```

## License
MIT
