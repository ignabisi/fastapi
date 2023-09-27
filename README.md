# Fastapi-Insights

Welcome to FastAPI-Insights! This repository serves as a curated collection of insights, best practices, and advanced techniques related to the FastAPI framework. Whether you're just getting started with FastAPI or looking to dive deep into its advanced features, this repository aims to provide valuable content to enhance your web development journey with FastAPI.

## Working with venv

```bash
python3 -m venv env
source env/bin/activate
```

## Switch environments

```bash
export ENVIRONMENT=test
```

## Access database via psql

```bash
docker-compose exec web-db psql -U postgres

postgres=# \c web_dev

# See List of relations
web_dev=# \dt

web_dev=# \q
```

## Contribution

We welcome contributions! Whether it's improving documentation, adding new insights, or sharing your unique experience with FastAPI, please feel free to make a pull request or open an issue.

### Useful Links

[Introduction to ASGI](https://florimond.dev/en/posts/2019/08/introduction-to-asgi-async-python-web/)
[Functools - lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
[Docker Best Practices](https://testdriven.io/blog/docker-best-practices/)
