# Week 1 — App Containerization

## Required Homework

### Video Review

* Watched [Grading Homework Summaries](https://youtu.be/FKAScachFgk)
* Watched [Week 1 Live Streamed Video](https://www.youtube.com/live/zJnNe5Nv4tE?feature=share) during the livestream.
* Watched [Commit Your Code](https://youtu.be/b-idMgFFcpg) video.

### Spending Considerations




## Stretch Homework

### Added steps to update Gitpod environment

I noticed during the prep phase that NPM complained about being out of date:

![image](../_docs/assets/week1/NPM_Update.png)

From running ```lsb_release -a``` I also found we are running Ubuntu Focal 20.04.  I ran an ```apt update && apt -y upgrade``` and noticed a lot of packages needing upgrades, so I decided to automate the updates.

I thought about switching the image to a newer image but apparently the default [Workspace image](https://www.gitpod.io/docs/configure/workspaces/workspace-image) is configured fairly well and I don't want to set up a full build from scratch each time I launch a new workspace.  I added the following to the .gitpod.yml:

```
  - name: Update Gitpod Workspace Environment
    init: |
      sudo apt update 
      sudo apt upgrade
      sudo apt autoremove
      sudo apt install -y nodejs
      npm install -g npm@latest
```
### Automated Gitpod environment setup for local container testing

As part of the setup to get the app to run locally in Python, we needed to ensure all the modules in requirements.txt are installed, as well as do an npm install before building the container, so it can copy the contents of node_modules.
Added the following to the .gitpod.yml file to automate these steps whenever a new Gitpod workspace is spun up:

```
  - name: Initialize Frontend and Backend
    init: |
      cd /workspace/aws-bootcamp-cruddur-2023/backend-flask
      pip3 install -r requirements.txt
      cd /workspace/aws-bootcamp-cruddur-2023/frontend-react-js
      npm i    
```
Credit for the idea to im__Brooke#9621 in Discord for the idea, and we figured it out together.

