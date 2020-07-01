# RepoCreation
Autonomous creation of git repo, and cloned locally through one command.  
Author: Damien Pilat,
Start Date: 19/06/2020

### Instructions
1. Add username, password and local path inside .env file,
2. Run `python createRepo.py <name of new repo>`

### Technologies used
* `PyGithub:` interact with Github,
* `pygit2:` allow git cloning,
* `dotenv:` interact with .env files.

### Acknolegements
This project is heavly based off the work done by [Kalle Hallden](https://www.github.com/KalleHallden/ProjectInitializationAutomation), 
and suplmented by [Bar Smith](https://www.stackoverflow.com/a/49458412/13777580).  
This is not original work, but rather a first introduction in working with github calls, .env files and local directories.