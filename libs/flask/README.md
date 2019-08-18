Create environment:

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

On Windows:

```
$ py -3 -m venv venv
```

Activate environment:

```
$ . venv/bin/activate
```

On Windows:

```
$ venv\Scripts\activate
```



Run the application:

```
$ set FLASK_APP=hello.py
$ flask run
```

Run in development mode:

```
$ set FLASK_ENV=development
$ flask run
```

(set on Windows, export on Linux)
