# Week 4 — Relational Databases

## Required Homework

### Video Review

* Watched [Week 4 – Live Streamed Video – Relational Databases](https://www.youtube.com/live/EtD7Kv5YCUs) Video.
* Watched [Week 4 - SQL RDS](https://youtu.be/Sa2iB33sKFo) Video.
* Watched [Week 4 - Creating Activities](https://youtu.be/fTksxEQExL4) Video.

### Actions

#### Live Stream Video Tasks

**Set up RDS Instance**

* Ran the following code:

```
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username cruddurroot \
  --master-user-password '<password>' \
  --allocated-storage 20 \
  --availability-zone ca-central-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```
* Temporarily stopped RDS instance.
* Spun up project containers and connected to the local Postgres instance using:

```
psql -U postgres --host localhost
```

* Common PSQL Commands:

```
\x on -- expanded display when looking at data
\q -- Quit PSQL
\l -- List all databases
\c database_name -- Connect to a specific database
\dt -- List all tables in the current database
\d table_name -- Describe a specific table
\du -- List all users and their roles
\dn -- List all schemas in the current database
CREATE DATABASE database_name; -- Create a new database
DROP DATABASE database_name; -- Delete a database
CREATE TABLE table_name (column1 datatype1, column2 datatype2, ...); -- Create a new table
DROP TABLE table_name; -- Delete a table
SELECT column1, column2, ... FROM table_name WHERE condition; -- Select data from a table
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...); -- Insert data into a table
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition; -- Update data in a table
DELETE FROM table_name WHERE condition; -- Delete data from a table
```

#### SQL RDS

* Watched [Week 4 - SQL RDS](https://youtu.be/Sa2iB33sKFo) Video

* Imported schema using the following while in the backend-flask directory:

```
psql cruddur < db/schema.sql -h localhost -U postgres
```

* Standard PostgreSQL Connection String:

```
postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]

export CONNECTION_URL="postgresql://postgres:password@127.0.0.1:5432/cruddur"
psql $CONNECTION_URL

export PROD_CONNECTION_URL="postgresql://cruddurroot:<password>@aws-rds-endpoint:5432/cruddur"
psql $PROD_CONNECTION_URL
```

* Set CONNECTION_URL and PROD_CONNECTION_URL environment variables for Dev Containers and Gitpod

* Created bash scripts for creating and dropping the database, and loading the schema.
* Created bash script for loading seed data and tested loading.
* Created bash scripts for automating setup

* Added psycopg requirements
* [Psycopg 3 Documentation](https://www.psycopg.org/psycopg3/)

* Added local IP to RDS security group

* Added environment variables for storing AWS security group rule and ID to local machine and parameters to pass into Dev Container

```
export LOCAL_IP=$(curl -s ifconfig.me)
export DB_SG_ID="<DB Security Group ID>"
export DB_SG_RULE_ID="<DB Security Group Rule ID>"
```

* Could add these in for Gitpod and would just have to adjust the AWS CLI command to pull the GITPOD_IP env variable instead.

* Command to update the security groups:

```
aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule=
    {Description='Allow Workstation PSQL',IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$LOCAL_IP/32}"
```

#### Cognito Post Confirmation Lambda

* Build Lambda function using ClickOps
* Imported corrected code into aws/lambda directory
* Configured Cognito Post-Confirmation Trigger
* Refreshed db bash scripts
* Pushed schema to production database
* Was able to delete and recreate user and have it successfully insert into database without error:

![image](../_docs/assets/week4/LambdaLogSuccess.png)

![image](../_docs/assets/week4/PSQLDataSuccess.png)

#### Creating Activities

* Watched [Week 4 - Creating Activities](https://youtu.be/fTksxEQExL4) Video.

* Went through 