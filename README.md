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
Than use Postman for POST requests for new user creation<br>
![Screenshot]()


### API from the browser:
You can work on the API directly in your browser

http://127.0.0.1:8000/auth/users/ <br>
![Screenshot]() <br>
or http://127.0.0.1:8001/auth/jwt/create
![Screenshot]()
