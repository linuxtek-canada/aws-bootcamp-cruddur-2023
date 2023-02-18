**Video Notes**
=======================

-You are a Cloud Engineer
-Founder = Sam
-Investors = Board of Directors, funding
-Fractional CTO - technical

-Startup Cruddr
-Microblogging Platform, Expiring Posts, Community, Trust, Users, SQL/MySql/NoSQL, Authentication
-Ephemeral first microblogging platform = App expiring post social media platform.  Twitter without dumpsterfire, Snapshat but more community focused
-Time limited content, user content, in platform advertising and traction? 
-Marketing team - lots of $ invested in Marketing team -> generating content?
    -Students? Young Professionals?
    -Authenticate age? Age limited content??
    -Tony:  Pitched to business professionals, anyone who doesn't want to maintain a presence online.  Less trust and safety issues the company has to deal with.
    -Limit customer personal info that can get leaked out.
-Awesome domain but platform not ready tet.
-Share lots of content, won't track long term.  Hoping to attract users and scale quickly.  Process lots of frequent transactions.
-Lots of logins, transactions, authentication.

Tony: App Tech
    -ABCo 6 months salary funded, fractional cto, office space, marketing space
    -Fractional CTO - someone partly committed to company, time split between consulting, advise other startups,
    -Our CTO is part time teacher
    -We can work with what dev firm created, or start fresh, mix/match.

ORM - Object Relational Mappings

Application Layers:  User Interface, Business Logic, Data Access

INFRASTRUCTURE BUDGET = Low as possible, spend money on marketing lol
    Iron Triangle of Project Management - Cost / Scope / Time - choose 2.  Cheap/Fast/Good - choose 2.

        Frontend - Javascript using React
        Backend - Python using Flask
        API driven - Only connects to exact endpoints
        Microservices
        NoSQL Database

**HOMEWORK** Technical Report due for investors
    -Architecture Diagram - Show AWS services in scope
    -Budget
    -Ongoing Cost Estimate

gitpod.io - CDE
    npm install after launching
    wait for docker to show up on the side
    then docker compose up


**Architecture**
=========================
Chris Williams - @vBrownBag Podcast

Requirements, Risks, Assessments, Constraints

Requirement - Project must achieve - ephemral, looks like twitter

Risks - identify and mitigate
    -User commitment
    -Delivery timeline

Assumptions
    -Network bandwidth sufficient, enough budget approved to complete projects

Constraints - policy, technical limitations
    -AWS is vendor - technical limitation
    -Timeframe 14+ weeks
    -Budget - low as possible (free tier)

After RRAC, create design
Conceptual
    -napkin design
    
Logical
    -separate blocks for components
Physical
    -ARN for the service, S3 bucket name
    -Load balancer frontend,backend names - granular names


*** Add napkin image to the homework

Ask dumb questions, be the packet, document everything*
    -> 

--------------------------------------
-6 Pillars Well-Architected Framework
-TOGAF/DADAF Architecture Frameworks
-"Well Architected Tool" > Define Workload - AWS Console

-The 4C Model - c4model.com


============================
Diagramming - lucid.app
    -Insert Content - AWS Architecture 2021
    -Then can add shapes

Conceptual Diagram - How does the business person realize their money


============================
HOMEWORK ->>> Deadline:  Submitted by next class

-Outline - Week 0 - Homework Challenges
-Suggested Ideas
-Automate SNS to send notification if health issue 
-Architectural Diagram for sure homework
    - Adrian Cantril- Cat Pipeline -> CI/CD components
    - https://github.com/acantril/learn-cantrill-io-labs
-AWS Service Limits - CloudFront - Hard Limits - request service limit
-Don't use root account credentials.


===============================================

Marking Project - 
-Build tool to check specific resources in AWS account, give permission to external app into AWS account to check for services
-and/or hit API endpoints
-Don't see sensitive information in accounts

Main homework -technical diagrams
*** Definitely do the napkin

-Branch/Tag code in Github for homework
-TA tag and put in bucket, reviewed second time to make completion
-Technical Essay - Documentation