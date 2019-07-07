import json

x = {
  "name": "Naveen",
  "age": 21,
  "country": "India",
  "education": [
    {"sslc": 8.9},
    {"hse": 7.9},
    {"btech":8.35}
  ]
}

writer = open("details.json", "a")
writer.write(json.dumps(x))
writer.close()