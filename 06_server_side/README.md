# 06 Server Side

To run this example in your programming environment first `cd` into
the `mytestsite` and run the following:

```bash
$ python3 manage.py runserver 0.0.0.0:8080
```

Next, you need to contact the HTTP server using an HTTP client. You
can easily test this from the command line:

```bash
$ curl http://localhost:8080
```

Alternatively, and perhaps more interesting, you can open a browser on
your host operating system and navigate to http://localhost:8080. We
recommend using chrome, however, any browser should work. The HTTP
request will be sent to your localhost and port. We have mapped port
8080 on your host operating system to port 8080 in your virtual
machine environment.

**Note**: In order for us to make sure this application works from
  within the class programming environment we had to update the
  `mytestsite/mytestsite/settings.py` file to include the following:

```python
ALLOWED_HOSTS = [
    '0.0.0.0'
]
```