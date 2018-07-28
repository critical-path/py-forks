"""command-line interface for py-forks."""


from json import dumps

from click import (
    command,
    echo,
    option
)

from forks.forks_lib import (
    get_repos,
    get_forks_for_one_repo,
    get_forks_for_all_repos,
    write_results
)


API = "https://api.github.com"


@command()
@option("--user", "-u", required=True, type=str, help="User of interest")
@option("--repo", "-r", type=str, help="Repo of interest")
@option("--write", "-w", is_flag=True, help="Write results to disk")
def get_forks(user=None, repo=None, write=False):
    """Util that retrieves a list of forks for a given GitHub user and repo."""

    if user and repo:
        forks = get_forks_for_one_repo(API, user, repo)

    elif user and not repo:
        repos = get_repos(API, user)
        forks = get_forks_for_all_repos(API, user, repos)

    forks = dumps(forks, indent=2)

    if write:
        write_results(user=user, repo=repo, forks=forks)

    echo(forks)


if __name__ == "__main__":
    get_forks()
