from click import (
  command,
  echo,
  option
)

from json import dumps

from forks.forks_lib import (
  get_repos,
  get_forks_for_one_repo,
  get_forks_for_all_repos
)


API = "https://api.github.com"


@command()
@option("--user", "-u", required=True, type=str, help="User of interest")
@option("--repo", "-r", type=str, help="Repo of interest")
def get_forks(user=None, repo=None):
  """ Util that retrieves a list of forks for a given GitHub user and repo. """

  if user and repo:
    forks = get_forks_for_one_repo(API, user, repo)

  elif user and not repo:
    repos = get_repos(API, user)
    forks = get_forks_for_all_repos(API, user, repos)

  forks = dumps(forks, indent=2)
  echo(forks)


if __name__ == "__main__":
  get_forks()

