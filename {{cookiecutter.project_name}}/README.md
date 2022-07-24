# {{cookiecutter.project_name}}

{{project}}

{{cookiecutter.project_description}}


## Get started


#### Install requirements & pre-commit hooks

```bash
$ make setup
```

#### Testing
```bash
$ make test
```

#### Documentation

##### Locally

Serve docs locally

```bash
$ make docs-dev
```

##### Build site

```bash
$ make docs-build
```


#### Linters requirements & pre-commit hooks

##### Run flake8

```bash
$ make lint
```

##### Run black & isort

```bash
$ make black
```