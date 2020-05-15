# git-rebase-bootcamp
Training Repo for rebasing

# The task

There is a feature in progress in the messy feature branch. Unfortunately there are 
unnecessary commits and bad commit messages.   
You are now the owner of this branch. Your task is to fix this messy history. You also want 
to merge this feature into the master branch, but this branch is already one commit ahead.
Rebase your branch ontop of master to apply the changes and make a fast fwd merge possible.

Todo:
---
- [ ] Fork or clone this repo
- [ ] Clean up the history
- [ ] Integrate progress of master into feature
- [ ] Merge the feature

# The current state

```
* '5576afa -  (HEAD -> master, origin/master, origin/HEAD) support multiple arguments
|
| * 7b9b4c0 -  (origin/messy_feature, messy_feature) bttr msg ftr
| * ef9353f -  wip
| * 2a0fb36 -  Typo in "woots up" and in "greetngs" was fixed, i must have overseen it in the hurry
| * 3bd0e88 -  create feature
|/
* 4726d7b -  init
* e529e3c -  Initial commit
```

You can look at the status yourself using this command
```shell
git log --oneline --graph --color --all
```

Resources
===

- https://www.atlassian.com/git/tutorials/merging-vs-rebasing

