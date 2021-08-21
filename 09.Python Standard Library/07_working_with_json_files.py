# WORKING WITH JSON FILES

import json

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993},
    {"id": 3, "title": "Ada Apa dengan Cinta 2", "year": 2016}
]

data = json.dumps(movies)
print(data)
