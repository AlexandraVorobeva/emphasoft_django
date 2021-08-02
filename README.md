# emphasoft_django
## DJANGO REST application.
REST API application for users with authentication.<br>

### Stack of technologies:<br>
-Python >= 3.8<br>
-Django REST<br>
-linter: Black<br>



### Basic functionality:<br>
1.Web REST API<br>
2.For a start you should sign up or sign in (if you was registered before)<br>
3.Functionality for users:<br>
  -List of all user<br>
  -Current user information<br>
  -Information about any user by id<br>
  -Change or delete any information about users<br>
  -Create new users<br>

### API endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /users/all | list of all users |
| GET | /users/< id> | user info by id |
| DELETE | /users/< id> | delete user by id |
| PUT | /users/< id> | change info about user by id |
| GET | /auth/users/me | info about user |
| POST | /auth/users | create new user |
| POST | /auth/jwt/create/ | create new token |
| POST | /auth/jwt/refresh/ | refresh old token |




## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/emphasoft_django<br>
$ cd emphasoft_django<br>


### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>

### Dependency
$ pip install -r requirements.txt<br>

### Run the sample server:<br>
$ python3 manage.py runserver<br>


### Run tests:<br>
$ pytest<br>

### API from Postman
You can use desktop app Postman fot rest requests.<br>
Run app in command line:<br>
$ python3 manage.py runserver<br>
Than use Postman for POST requests for creating a new user:<br>
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2021.02.09.png)
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2021.02.29.png)
Than create new token for authentication:
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2021.03.17.png)
 
With valid token you can get list of all user:
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2021.04.00.png)
Or just info about yourself:
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2021.04.51.png)

### API from the browser:
You can work on the API directly in your browser

http://127.0.0.1:8000/auth/users/ <br>
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2020.52.13.png) <br>
or http://127.0.0.1:8001/auth/jwt/create
![Screenshot](https://github.com/SparklingAcidity/emphasoft_django/blob/in_process/img_for_readme/Снимок%20экрана%202021-08-01%20в%2020.53.39.png)
