import sys
def application(environ, start_response):
    status = '200 OK'
    output = "mod_wsgi executing script via python version:\n{}\n".format(sys.version)
    output = output.encode('utf-8')
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
