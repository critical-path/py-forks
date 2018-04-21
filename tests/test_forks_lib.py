from constants import (
  API, 
  FORKS, 
  REPO0,
  REPO1, 
  REPOS, 
  REPO0_AND_FORKS,
  REPOS_AND_FORKS,
  USER
)

from forks.forks_lib import (
  get_repos,
  get_forks_for_all_repos,
  get_forks_for_one_repo
)

from json import dumps

from requests import get

from responses import (
  activate, 
  add, 
  GET
)


@activate
def test_get_repos():
  endpoint = "{}/users/{}/repos".format(API, USER)

  add(
    method=GET, 
    url=endpoint, 
    body=dumps(REPOS), 
    status=200
  )

  repos = get_repos(API, USER)

  assert repos == ["test-repo0", "test-repo1"]


@activate
def test_get_forks_for_one_repo():
  endpoint = "{}/repos/{}/{}/forks".format(API, USER, REPO0)

  add(
    method=GET, 
    url=endpoint, 
    body=dumps(FORKS), 
    status=200
  )

  forks = get_forks_for_one_repo(API, USER, REPO0)

  assert forks == REPO0_AND_FORKS


@activate
def test_get_forks_for_all_repos():
  repos_endpoint = "{}/users/{}/repos".format(API, USER)

  add(
    method=GET,
    url=repos_endpoint,
    body=dumps(REPOS),
    status=200
  )

  forks_endpoint0 = "{}/repos/{}/{}/forks".format(API, USER, REPO0)

  add(
    method=GET,
    url=forks_endpoint0,
    body=dumps(FORKS),
    status=200
  )

  forks_endpoint1 = "{}/repos/{}/{}/forks".format(API, USER, REPO1)

  add(
    method=GET,
    url=forks_endpoint1,
    body=dumps(FORKS),
    status=200
  )

  repos = get_repos(API, USER)
  forks = get_forks_for_all_repos(API, USER, repos)

  assert forks == REPOS_AND_FORKS

