
title: Motor Quotation Project
created at: Sat May 22 2021 07:40:22 GMT+0000 (Coordinated Universal Time)
updated at: Sat May 22 2021 07:42:01 GMT+0000 (Coordinated Universal Time)
---

# Motor Quotation Project

**Software Name: **Motor Quotation Project

**Software Version: 1.0**

**Steps to get started**

| **Steps To Get Started**                                                                               | **Instructions**                                                                              | **Additional Comments** |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ----------------------- |
| \_Download the project and build your local \_environment. eg. pipenv                                  | In simple and action-oriented language, guide users through the first steps of your software. |                         |
| Install the project packages                                                                           | pip install -r requirements.txt\_ \_                                                          |                         |
| _Migrate files to your database _                                                                      | python manage.py migrate                                                                      |                         |
| _Load initial data which includes the admin user "admin123" password "1234" and the coverage defaults_ | python manage.py loaddata fixtures.json                                                       |                         |
| Update the .env file with your Email and Password for the emails sending feature                       |                                                                                               |                         |
| Download Redis (used by Celery)                                                                        | <https://redis.io/download>                                                                   |                         |
| Run server                                                                                             | python manage.py runserver                                                                    |                         |
| Run Redis server for Celery tasks                                                                      | redis-server                                                                                  |                         |
| Run Celery                                                                                             | celery -A <project-name-here> worker -l info                                                  |                         |

**Send Email Feature Notes**

Note that the sender email host shall have Auth 2 Step activated to send the emails and avoid Authenticating errors and for receiver emails its better to allow "Allow-Less-Secure-Apps" to receive emails inbox and not on Spam.

          