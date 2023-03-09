# Week 3 — Decentralized Authentication

## Required Homework

### Video Review

* Watched [Week 3 – Live Streamed Video – Decentralized Authentication](https://www.youtube.com/live/9obl7rVgzJw)
* Watched [Week 3 - Cognito Custom Pages](https://youtu.be/T4X4yIzejTc)

### Actions

#### Live Stream Video Tasks

* Followed livestream video to implement custom sign-in.  Got to the point where I got the same error:

```
Cannot read properties of null (reading 'accessToken')
```

#### Cognito Custom Pages Video Tasks

* Ran the following command on my user created in Cognito to force a permanent password:

```
aws cognito-idp admin-set-user-password \
  --user-pool-id <your-user-pool-id> \
  --username <username> \
  --password <password> \
  --permanent
```
* Updated Sign-Up Page
* Now able to sign in properly.
* Recreated my user pool multiple times to fix the fields for email, preferred_username, and name.
* Updated values in docker-compose.yml and restarted - now able to sign up and log in.
* Updated Recovery Page with onsubmit send/confirm code.
* Tested password recovery - it does send an email with a verification code.

## Stretch Homework

-Make password recovery page pretty