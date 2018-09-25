# 06 Server Side

To run this example in your programming environment first `cd` into
the `mytestsite` and run the following (See **Note** below):

```bash
$ python3 manage.py runserver 0.0.0.0:8080
```

We use the IP address designation `0.0.0.0` to tell Django to bind
or listen on all IP addresses that the computer supports. If you
do not provide this you will not be able to send HTTP requests to
Django running in the class programming environment VM. Take a
look at [this StackOverflow post](https://stackoverflow.com/questions/1621457/about-ip-0-0-0-0-in-django).

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
