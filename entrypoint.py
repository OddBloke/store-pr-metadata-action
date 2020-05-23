#!/usr/bin/env python3
import os
import subprocess
import sys

from github import Github

print(sys.argv)

token = sys.argv[1]
pr_number = int(sys.argv[2])

g = Github(token)

actor = os.environ["GITHUB_ACTOR"]
repo_name = os.environ["GITHUB_REPOSITORY"]

repo = g.get_repo(repo_name)
pr = repo.get_pull(pr_number)
print(str(pr))

remote_repo = "https://{}:{}@github.com/{}.git".format(actor, token, repo_name)


def _run(*args, **kwargs):
    print(args, kwargs)
    process = subprocess.run(*args, **kwargs)
    print(process.stdout)
    print(process.returncode)
    print(process.stderr)


_run(["git", "config", "--global", "user.email", "bot@example.com"])
_run(["git", "config", "--global", "user.name", "Store PR Metadata Bot"])

directory = "repo"

_run(["git", "clone", remote_repo, directory], capture_output=True)
_run(
    ["git", "notes", "add", "-F", "-"], cwd=directory, input=str(pr), text=True
)
_run(["git", "push", "origin", "refs/notes/*"], cwd=directory)

print(os.environ)
