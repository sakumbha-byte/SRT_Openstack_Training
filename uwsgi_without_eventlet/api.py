def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('content-type' , 'text/plain')]
    start_response(status, headers)
    return [b"Hello from oslo_service running on uWSGI!"]
