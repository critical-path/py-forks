from json import dumps


API = "https://api.github.com"

USER = "test-user"

REPO0 = "test-repo0"

REPO1 = "test-repo1"

REPOS = [
  {
    "name": "test-repo0"
  }, 
  {
    "name": "test-repo1"
  }
]

FORKS = [
  {
    "name": "test-fork0"
  },
  {
    "name": "test-fork1"
  }
]

REPOS_AND_FORKS = {  
  "test-repo0": 
    [
      {
        "name": "test-fork0"
      },
      {
        "name": "test-fork1"
      }
    ],

  "test-repo1":
    [
      {
        "name": "test-fork0"
      },
      {
        "name": "test-fork1"
      }
    ]  
}

REPO0_AND_FORKS = {
  "test-repo0": 
    [
      {
        "name": "test-fork0"
      }, 
      {
        "name": "test-fork1"
      }
    ]
}

