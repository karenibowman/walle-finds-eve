import requests

# Tests Specified on Github

r = requests.post("http://localhost:3000/api/maps/", json={'row': 5, 'col': 5})
print(r.status_code, r.reason, r.json())

r = requests.post("http://localhost:3000/api/paths/start", json={'i': 0, 'j': 0})
print(r.status_code, r.reason, r.json())

r = requests.post("http://localhost:3000/api/paths/goal/", json={'i': 4, 'j': 4})
print(r.status_code, r.reason, r.json())

r = requests.post("http://localhost:3000/api/costs", json={
    'costs': [
        {'i': 0, 'j': 1, 'value': 10.0},
        {'i': 1, 'j': 1, 'value': 10.0},
        {'i': 3, 'j': 0, 'value': 10.0},
        {'i': 3, 'j': 1, 'value': 10.0},
        {'i': 1, 'j': 3, 'value': 10.0},
        {'i': 2, 'j': 3, 'value': 10.0},
        {'i': 3, 'j': 3, 'value': 10.0},
    ]
})
print(r.status_code, r.reason, r.json())

r = requests.get("http://localhost:3000/api/paths")
print(r.status_code, r.reason, r.json())
