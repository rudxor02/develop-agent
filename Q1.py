prompt = """Request: Please develop a website that displays hello world.

Additional informations
-----
1. You have python3 in shell. Don't use another program, for example python.
2. Develop in /root/develop-agent/Q1/hello_world_server.py file and execute server by using command 'python3 /root/develop-agent/Q1/hello_world_server.py > /root/develop-agent/Q1/output &'
3. In python there is flask package installed, so use flask.
4. After you run the server, then immediately return the URL of the website.
5. URL of the server should be http://localhost:8000
6. If user connects to http://localhost:8000, user should see 'Hello, world!' messege.
-----
"""