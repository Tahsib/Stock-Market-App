# Stock-Market-App
Users can search for stock market details of renowned companies using ticker symbol and can add company ticker symbols to get their latest stock market information in the dashboard.

## Installing
* Start a virtual environment
```
virtualenv env <environment name>
source <environment name>/bin/activate
```
* Install all the dependencies
```
pip3 install -r requirements.txt
``` 
* Create a superuser
```
python3 manage.py createsuperuser
```
* Make migrations and migrate the database
```
python3 manage.py makemigrations
python3 manage.py migrate
```
* Get free API KEY from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
* Create '''.env''' file and add ```API_KEY=<your api key>```

## Running the project
```
python3 manage.py runserver
```

### In windows use ```python``` instead of ```python3``` and ```pip``` instead of ```pip3``` in all the commands.

## Built with 
* Python 3.8
* Django 3.0.8
