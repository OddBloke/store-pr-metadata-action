#!/usr/bin/env python3
import os
import subprocess
import sys

from github import Github

print(sys.argv)

g = Github(sys.argv[1])

repo_name = os.environ["GITHUB_REPOSITORY"]
repo = g.get_repo(repo_name)
pr = repo.get_pull(int(sys.argv[2]))
print(str(pr))

remote_repo = (
    "https://{GITHUB_ACTOR}:{token}@github.com/{GITHUB_REPOSITORY}.git".format(
        token=sys.argv[1],
        **os.environ
    )
)

process = subprocess.run(["git", "clone", remote_repo], capture_output=True)
print(process.stdout)
print(process.returncode)
print(process.stderr)

print(os.environ)
