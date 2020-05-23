#!/usr/bin/env python3
import os
import sys

from github import Github

print(sys.argv)

g = Github(sys.argv[1])

repo_name = os.environ["GITHUB_REPOSITORY"]
repo = g.get_repo(repo_name)
pr = repo.get_pull(sys.argv[2])
print(str(pr))
