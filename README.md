Submission from Karen Bowman, kibowman@andrew.cmu.edu, on June 4, 2019

# File Structure

This application is built with Python using Flask, and can be run using the
included Dockerfile.

- Client
  - test.py
- Server
  - app.py
  - dijkstra.py
  - paths.py
- Dockerfile:
- requirements.txt

# Usage:

Enter the folder containing this file

```$ cd walle-finds-eve```

Build the Docker Image

```$ docker build --tag=wallefindseve .```

Run the server on port 3000

```$ docker run -p 3000:3000 wallefindseve```

If you wish to use it, there is a Python3 test client. It is not run in the Docker container, but externally.

```$ python3 client/test.py ```
