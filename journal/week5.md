# Week 5 — DynamoDB and Serverless Caching

## Required Homework

### Video Review
* Watched [Week 5 - DynamoDB Utility Scripts](https://youtu.be/pIGi_9E_GwA)
* Watched [Week 5 - DynamoDB Considerations](https://youtu.be/gFPljPNnK2Q)
* Watched [Week 5 - Implement Conversations with DynamoDB](https://youtu.be/dWHOsXiAIBU)

### Actions

### DynamoDB Utility Scripts

* Implemented Schema Load Script
* Implemented Seed Script
* Implemented Scan Script
* Implemented Pattern Scripts for Read/List Conversations (get/list)
* 

### Implement Conversations With DynamoDB

* Updated database drop to only perform if it already exists
* Implemented ddb.py 
* Verified Cognito IDP List Check
* Added AWS_COGNITO_USER_POOL_ID Environment variable to local environment and updated devcontainer settings to import.
* Removed hardcoding of environment variable in docker-compose.yml
* Implemented update_cognito_user_ids
* Updated app.py message_groups
* Updated message_groups.py to use Cognito instead of mock data
* Implemented SQL queries for cognito compatibility
* Updated Frontend MessageGroupPage with authorization
* Implemented CheckAuth.js
* Added Date/Time to patterns
* Updated app.py with new data_create_message function
* Updated create_message.py
* Added MessageGroupNewPage.js
* Added app.route short to App.js and added users_short.py
* Updated MessageGroupFeed.js



