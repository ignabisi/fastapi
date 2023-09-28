# FastAPI-Insights ✨

Welcome to FastAPI-Insights! This repository serves as a curated collection of insights, best practices, and advanced techniques related to the FastAPI framework. Whether you're just getting started with FastAPI or looking to dive deep into its advanced features, this repository aims to provide valuable content to enhance your web development journey with FastAPI.

## 🐍 Setting up Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

## 🔄 Switching Environments

```bash
export ENVIRONMENT=test
```

## 🗃️ Database Access via psql

```bash
postgres=# \c web_dev
# To see the list of relations
web_dev=# \dt
# To exit
web_dev=# \q
```



## 🐳 Handy Docker Commands

```bash
# normal run
$ docker-compose exec web python -m pytest

# disable warnings
$ docker-compose exec web python -m pytest -p no:warnings

# run only the last failed tests
$ docker-compose exec web python -m pytest --lf

# run only the tests with names that match the string expression
$ docker-compose exec web python -m pytest -k "summary and not test_read_summary"

# stop the test session after the first failure
$ docker-compose exec web python -m pytest -x

# enter PDB after first failure then end the test session
$ docker-compose exec web python -m pytest -x --pdb

# stop the test run after two failures
$ docker-compose exec web python -m pytest --maxfail=2

# show local variables in tracebacks
$ docker-compose exec web python -m pytest -l

# list the 2 slowest tests
$ docker-compose exec web python -m pytest --durations=2
```

### 🌐 Must-Visit Links

- [🚀Introduction to ASGI](https://florimond.dev/en/posts/2019/08/introduction-to-asgi-async-python-web/)

- [🛠 Functools - lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)

- [🐳Docker Best Practices](https://testdriven.io/blog/docker-best-practices/)

- [📚Tortoise ORM Migration](https://tortoise.github.io/migration.html)

- [🐢Tortoise-Aerich](https://github.com/tortoise/aerich)

- [🔍Testing|Given-When-Then](https://martinfowler.com/bliki/GivenWhenThen.html)

- [📚Heroku Alternatives for Python-based Applications](https://testdriven.io/blog/heroku-alternatives/)

## 🤝 Join the Party

Contribute to the treasure! From refining docs, adding fresh insights, to sharing your signature FastAPI journey - we’re all ears! Jump right in with a pull request or kick things off with an issue. 🎉
