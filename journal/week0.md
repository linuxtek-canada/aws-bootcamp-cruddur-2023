# Week 0 — Billing and Architecture



## Prerequisites
* Created AWS Account for Bootcamp.
* Created Github repo (which you are reading from).
* Set up Gitpod account authorized with Github.  Followed [Gifted Lane's Video](https://www.youtube.com/watch?v=yh9kz9Sh1T8) for setup, and [Andrew Brown's video](https://www.youtube.com/watch?v=A6_c-hJmehs) for the Gitpod button.



## Required Homework

1. Attended Week 0 Live Stream, and the Discord Q&A Session afterwards.
* Watched follow-up Week 0 -  Generate Credentials, AWS CLI, Budget and Billing Alarm via CLI video.

2. Watched Chirag's Week 0 - Spend Considerations Video.

3. Watched Ashish's Week 0 - Security Considerations Video.
  * I had previously set up an AWS Organization and created the Bootcamp account as a subaccount.  I published [an article](https://www.linuxtek.ca/2023/02/07/aws-cloud-project-boot-camp-week-0-tips-and-tricks/) on this.
  * Activated MFA for root user.
  * Reviewed [blog post](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/) for changes to IAM Policies.  Confirmed no affected policies to update.  

  ![image](../_docs/assets/week0/SecurityRecommendations.png)

  4.  Created IAM Admin user with [unique login](https://linuxtekbootcamp.signin.aws.amazon.com/console) alias.  I use a [hosted Bitwarden server](https://www.linuxtek.ca/2023/01/03/self-hosting-bitwarden-on-aws/) to save all my passwords, and it includes a password generator.

  5. Created Access Key/Secret pair for Admin user.

  6.  Tried out AWS CloudShell.

  7.  Installed AWS CLI for Gitpod using [this video](https://youtu.be/OdUnNuKylHg).  Manually installed, but also edited .gitpod.yml to auto-install if the environment gets restarted.

```
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```

Added persistent Gitpod variables to store AWS credentials for resuse using these commands:

```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=""
```

Confirmed in Gitpod [User Settings > Variables](https://gitpod.io/user/variables) that variables are saved:
![image](../_docs/assets/week0/GitpodVariables.png)

Started up a new Gitpod environment to confirm AWS CLI was installed correctly and AWS credentials were pulled from Gitpod variables to environment variables.  Successfully ran ```aws sts get-caller-identity``` and returned values.