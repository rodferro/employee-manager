# Employee Manager

You need the following packages to run this application:

```
Django==2.0.6  
djangorestframework==3.8.2  
pytz==2018.4  
```

To start the application, run **python manage.py runserver** on the command-line. Navigate to http://127.0.0.1:8000/ to access the admin panel.

You can access the API from the command-line using the following examples:

* curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/employee/
* curl -H 'Content-Type: application/json' -X POST http://127.0.0.1:8000/employee/ -d '{"name":"Rodrigo Ferro", "email":"rodrigo@luizalabs.com", "department": "Architecture"}'
* curl -X DELETE http://127.0.0.1:8000/employee/14/
