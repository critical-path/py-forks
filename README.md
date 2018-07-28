[![Build Status](https://travis-ci.com/critical-path/py-forks.svg?branch=master)](https://travis-ci.com/critical-path/py-forks)

## py-forks v1.0.0

py-forks is a util that retrieves a list of forks for a given GitHub user and repo.


## Dependencies

py-forks requires Python as well as the pip, click, requests, pylint, pytest-cov, and responses packages.


## Installing py-forks with test cases and testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command and the --editable option.

```
sudo pip3 install --editable .[test] .
```


## Installing py-forks without test cases or testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command.

```
sudo pip3 install .
```


## Using py-forks with long options

To retrieve a list of forks for all repos associated with a given user, run forks with the --user option.

```
forks --user <user>
```

To retrieve a list of forks associated with a given user and a given repo, run forks with the --user and --repo options.

```
forks --user <user> --repo <repo>
```

To write the retrieved list of forks to disk, run forks with the --write option.

```
forks --user <user> --write
forks --user <user> --repo <repo> --write
```


## Using py-forks with short options

To retrieve a list of forks for all repos associated with a given user, run forks with the -u option.

```
forks -u <user>
```

To retrieve a list of forks associated with a given user and a given repo, run forks with the -u and -r options.

```
forks -u <user> -r <repo>
```

To write the retrieved list of forks to disk, run forks with the -w option.

```
forks -u <user> -w
forks -u <user> -r <repo> -w
```


## Testing py-forks after installation

1. Run pylint.

```
pylint forks
```

2. Change to the tests directory.

```
cd ./tests
```

3. Run pytest with the -v, --cov, and, --cov-report options.

```
pytest -v --cov=forks --cov-report=term-missing
```


## Note

py-forks makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.

