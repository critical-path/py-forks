from json import dumps

from os import (
    remove,
    stat
)

from click.testing import CliRunner

from forks.cli import get_forks

from responses import (
    activate,
    add,
    GET
)

from constants import (
    API,
    FILENAME_USER,
    FILENAME_USER_REPO,
    FORKS,
    REPO0,
    REPO1,
    REPOS,
    REPO0_AND_FORKS,
    REPOS_AND_FORKS,
    USER
)


def test_cli_help():
    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "--help"
        ]
    )

    assert result.exit_code == 0
    assert "Usage" in result.output


def test_cli_no_user_no_repo_no_write():
    runner = CliRunner()

    result = runner.invoke(
        get_forks
    )

    assert result.exit_code != 0
    assert "Missing" in result.output


@activate
def test_cli_user_repo_no_write_long():
    endpoint = "{}/repos/{}/{}/forks".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(FORKS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "--user", USER,
            "--repo", REPO0
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_FORKS, indent=2) + "\n"


@activate
def test_cli_user_repo_no_write_short():
    endpoint = "{}/repos/{}/{}/forks".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(FORKS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "-u", USER,
            "-r", REPO0
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_FORKS, indent=2) + "\n"


@activate
def test_cli_user_no_repo_no_write_long():
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

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "--user", USER
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_FORKS, indent=2) + "\n"


@activate
def test_cli_user_no_repo_no_write_short():
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

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "-u", USER
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_FORKS, indent=2) + "\n"


@activate
def test_cli_user_repo_write_long():
    endpoint = "{}/repos/{}/{}/forks".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(FORKS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "--user", USER,
            "--repo", REPO0,
            "--write"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_FORKS, indent=2) + "\n"
    assert stat(FILENAME_USER_REPO)
    remove(FILENAME_USER_REPO)


@activate
def test_cli_user_repo_write_short():
    endpoint = "{}/repos/{}/{}/forks".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(FORKS),
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "-u", USER,
            "-r", REPO0,
            "-w"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPO0_AND_FORKS, indent=2) + "\n"
    assert stat(FILENAME_USER_REPO)
    remove(FILENAME_USER_REPO)


@activate
def test_cli_user_no_repo_write_long():
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

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "--user", USER,
            "--write"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_FORKS, indent=2) + "\n"
    assert stat(FILENAME_USER)
    remove(FILENAME_USER)


@activate
def test_cli_user_no_repo_write_short():
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

    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "-u", USER,
            "-w"
        ]
    )

    assert result.exit_code == 0
    assert result.output == dumps(REPOS_AND_FORKS, indent=2) + "\n"
    assert stat(FILENAME_USER)
    remove(FILENAME_USER)


def test_cli_repo_no_user_long():
    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "--repo", REPO0
        ]
    )

    assert result.exit_code != 0
    assert "Missing" in result.output


def test_cli_repo_no_user_short():
    runner = CliRunner()

    result = runner.invoke(
        get_forks,
        [
            "-r", REPO0
        ]
    )

    assert result.exit_code != 0
    assert "Missing" in result.output
