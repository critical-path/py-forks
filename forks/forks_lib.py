from requests import get


def get_repos(api, user):
    """Get list of all repos for a given user.

    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    The parameters help to form the API endpoint.
    """

    repos = []

    endpoint = "{}/users/{}/repos".format(api, user)
    response = get(endpoint)
    response_body = response.json()

    for element in response_body:
        repo = element["name"]
        repos.append(repo)

    return repos


def get_forks_for_one_repo(api, user, repo):
    """Get list of all forks for a given repo.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    repos : str
        The repo of interest.

    The parameters help to form the API endpoint.
    """

    forks = {}

    endpoint = "{}/repos/{}/{}/forks".format(api, user, repo)
    response = get(endpoint)
    response_body = response.json()
    forks[repo] = response_body

    return forks


def get_forks_for_all_repos(api, user, repos):
    """Get list of all forks for a given list of repos.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    repos : list
        The repos of interest.

    The parameters help to form the API endpoint.
    """

    forks = {}

    for repo in repos:
        endpoint = "{}/repos/{}/{}/forks".format(api, user, repo)
        response = get(endpoint)
        response_body = response.json()
        forks[repo] = response_body

    return forks


def write_results(user=None, repo=None, forks=None):
    """Write results to disk.

    Parameters
    ---------
    user : str
      The user of interest.

    repo : str, optional
      The repo of interest.

    forks : str in JSON format
      The forks associated with the user and repo.

    The parameters help to form the filename.
    """

    if user and repo:
        filename = "forks-{0}-{1}.json".format(user, repo)
    elif user and not repo:
        filename = "forks-{0}.json".format(user)

    with open(filename, "w") as output:
        output.write(forks)
