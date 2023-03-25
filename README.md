# Description
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

**Monday - Friday**

- 00:01 - 09:00 25 USD
- 09:01 - 18:00 15 USD
- 18:01 - 00:00 20 USD

**Saturday and Sunday**

- 00:01 - 09:00 30 USD
- 09:01 - 18:00 20 USD
- 18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

- MO: Monday
- TU: Tuesday
- WE: Wednesday
- TH: Thursday
- FR: Friday
- SA: Saturday
- SU: Sunday

- Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

- Output: indicate how much the employee has to be paid

For example:

**Case 1:**

INPUT
- RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:
- The amount to pay RENE is: 215 USD

**Case 2:**

INPUT
- ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
- The amount to pay ASTRID is: 85 USD

# SOLUTION 
An application was developed using Python-Django and DjangoRESTFramework.

The following models were developed

![image](https://user-images.githubusercontent.com/24283414/227744393-61822c60-ccda-461e-8d86-e7ff37064b13.png)

The architecture used in this solution was Model-View-Template.

# HOW TO DEPLOY 

1. Clone the repository
2. Install docker (https://docs.docker.com/engine/install/)
3. Install postgresql (https://www.postgresql.org/download/)
4. Create a postgres database called "acme_db" with "postgres" as user and password.
5. Execute the script "run.sh" (The application will be start in localhost:8000)
6. Populate the database loading the fixtures, there are three fixture in this path "apps\payments\fixtures".
7. Execute: docker-compose exec web python3 manage.py loaddata apps/payments/fixtures/payments.day.json
8. Execute: docker-compose exec web python3 manage.py loaddata apps/payments/fixtures/payments.schedule.json
9. Execute: docker-compose exec web python3 manage.py loaddata apps/payments/fixtures/payments.rate.json
10. If the information was uploaded correctly, you can now use the application.

# VIEWS AND URLS
The application has two main views 

1. http://localhost:8000/payments/

![image](https://user-images.githubusercontent.com/24283414/227744799-ed06caf8-6419-4b73-94dc-bd9df56a441a.png)
In this view the user can select a text file to be processed.
Once the user selects the file and clicks on the "submit" button the system will display a notification in the output format.

![image](https://user-images.githubusercontent.com/24283414/227744858-ebd4d189-a90e-4216-bf26-08c2a65f66e6.png)

2. http://localhost:8000/payments/api

![image](https://user-images.githubusercontent.com/24283414/227744878-66072dd1-3a83-4b83-8586-f6917ee4af07.png)

This view is an endpoint which is in charge of processing the content of the file to give the information of the total amount to be paid to the employee.

# UNIT TESTS

This project has a tests.py file with four unit tests written in pytest

![image](https://user-images.githubusercontent.com/24283414/227744972-4a353159-8236-4ae2-9fc3-c1c3d8f4cf9d.png)



