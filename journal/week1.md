# Week 1 — App Containerization

## Required Homework

### Video Review

* Watched [How to Ask for Technical Help](https://youtu.be/tDPqmwKMP7Y) video.
* Watched [Grading Homework Summaries](https://youtu.be/FKAScachFgk) video.
* Watched [Week 1 Live Streamed Video](https://www.youtube.com/live/zJnNe5Nv4tE?feature=share) during the livestream and followed along with the tasks.
* Watched [Commit Your Code](https://youtu.be/b-idMgFFcpg) video.
* Watched [Chirag's Week 1 Spend Consideration](https://youtu.be/OAMHu1NiYoI) video.
* Watched [Ashish's Week 1 Security Consideration](https://youtu.be/OjZz4D0B-cA) video.
* Watched [Week 1 - Create the notification feature (Backend and Front)](https://youtu.be/k-_o0cCpksk) video.
  * The hardcoded confirmation code is '1234'.
  * [OpenAPI Specification v3.1.0](https://spec.openapis.org/oas/v3.1.0)

### Actions

* Completed all steps during the livestream to containerize the application.
* Went through [video](https://youtu.be/k-_o0cCpksk) steps and added frontend and backend notifications functionality.
  * Documented notification endpoint for OpenAPI document.
  * Wrote Flask backend endpoint for notifications.
  * Wrote React page for notifications. 
* Went through [video](https://youtu.be/CbQNMaa6zTg) steps to set up PostgreSQL and DynamoDB Local
  * Ran DynamoDB Local container to ensure it worked
  * Ran Postgres container to ensure it worked
  * [AWS Documentation - DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)

## Spending Considerations

## Security Considerations

## Stretch Homework

### Added steps to update Gitpod environment

I noticed during the prep phase that NPM complained about being out of date:

![image](../_docs/assets/week1/NPM_Update.png)

From running ```lsb_release -a``` I also found we are running Ubuntu Focal 20.04.  I ran an ```apt update && apt -y upgrade``` and noticed a lot of packages needing upgrades, so I decided to automate the updates so it would be handled anytime a new Gitpod workspace spins up.  I thought about switching the image to a newer major version, but apparently the default [Workspace image](https://www.gitpod.io/docs/configure/workspaces/workspace-image) is configured fairly specifically, and I don't want to set up a full build from scratch each time I launch a new workspace.  I added the following to the .gitpod.yml init section:

```
      sudo apt update && sudo apt upgrade -y
      sudo apt autoremove -y    
      npm install -g npm@latest      
```

### Automated Gitpod environment setup for local container testing

As part of the setup to get the app to run locally in Python, we needed to ensure all the modules in requirements.txt are installed, as well as do an npm install before building the container, so it can copy the contents of node_modules.
Added the following to the .gitpod.yml init section to automate these steps whenever a new Gitpod workspace is spun up:

```
      cd /workspace/aws-bootcamp-cruddur-2023/backend-flask
      pip3 install -r requirements.txt
      cd /workspace/aws-bootcamp-cruddur-2023/frontend-react-js
      npm i
      cd /workspace/aws-bootcamp-cruddur-2023/     
```
Credit for the idea to im__Brooke#9621 in Discord for the idea, and we figured it out together.

### Fell down the Rabbit Hole with Gitpod for about 10 hours

From some troubleshooting in the #gitpod Discord channel, we were trying to figure out why the AWS CLI utility was hanging on install.  The workaround solution I had was to group all of the init Tasks into one block, but I knew this wasn't the correct answer.  Andrew posted this message in announcements with a clue:

![image](../_docs/assets/week1/GitpodAnnouncementHint.png)

* I started by reviewing Andrew's [Cloud Development Environment](https://www.exampro.co/exp-cde-01) course on ExamPro.
* Tested a number of Tasks scenarios, enabled and tested Prebuilds, and set up a Custom Workspace Image using a .gitpod.Dockerfile.
* Based on what I found, we shouldn't be doing any global package/module installs using Tasks as the install won't persist if it's part of the init stage, or modifies files outside of the /workspace directory.

![image](../_docs/assets/week1/10hourslater.jpg)

* Wrote up [an article](https://www.linuxtek.ca/2023/02/21/diving-deeper-gitpod-cloud-development-environment/) detailing everything I had found.
* Asked some questions in the Gitpod Discord, and got some feedback to fix up the article.

## Publications

* [AWS Cloud Project Bootcamp – Week 1: Unofficial Homework Guide](https://www.linuxtek.ca/2023/02/18/aws-cloud-project-bootcamp-week-1-unofficial-homework-guide/)
* [Diving Deeper – Gitpod Cloud Development Environment](https://www.linuxtek.ca/2023/02/21/diving-deeper-gitpod-cloud-development-environment/)
