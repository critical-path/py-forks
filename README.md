## py-forks v1.0.0

py-forks is a util that retrieves a list of forks for a given GitHub user and repo.


## Dependencies

py-forks requires Python 3.x as well as the pip, click, requests, pytest, pytest-cov, and responses packages.


## Installing py-forks (with test cases and testing dependencies)

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command and the --editable option.

```
sudo pip3 install --editable .[test] .
```


## Installing py-forks (without test cases or testing dependencies)

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command.

```
sudo pip3 install .
```


## Using py-forks (long options)

To retrieve a list forks for all repos associated with a given user, run forks with the --user option.

```
forks --user <user>
```

To retrieve a list of forks associated with a given user and a given repo, run forks with the --user and --repo options.

```
forks --user <user> --repo <repo>
```


## Using py-forks (short options)

To retrieve a list forks for all repos associated with a given user, run forks with the -u option.

```
forks -u <user>
```

To retrieve a list of forks associated with a given user and a given repo, run forks with the -u and -r options.

```
forks -u <user> -r <repo>
```


## Testing py-forks

1. Change to the tests directory.

```
cd ./tests
```

2. Run pytest with the -v --cov and --cov-report options.

```
pytest -v --cov=forks --cov-report=term-missing
```


## Note

py-forks makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.

