GIT
===

### Emergency F-up

    git reflog


cd /path/to/your/existing/code

    git init 
    git add .
    git commit -m "REPO"
    [create new project on github]
    git remote add <remote_name> <remote_repo_url>
    git push origin master

/// DOWNSTREAM/UPSTREAM ///

you pull from upstream and then push back to it 

    set upstream: 
    git push --set-upstream origin master


move to another branch with:

    git checkout [Branch]

---
### AutoLogin

    check 
    git config -l
    change
    git config remote.origin.url git@github.com:your_username/your_project.git

---

### PUSH 

before a push, the file needs to be added and then committed

    git add .
    git commmit -c "update"
    git push

---
### REMOVE 

    git rm file
    git rm -r folder
