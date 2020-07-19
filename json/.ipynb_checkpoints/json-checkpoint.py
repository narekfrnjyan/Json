{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'http://swapi.dev/api/planets/1/', 'films': ['http://swapi.dev/api/films/1/', 'http://swapi.dev/api/films/2/', 'http://swapi.dev/api/films/3/', 'http://swapi.dev/api/films/6/'], 'species': [], 'vehicles': ['http://swapi.dev/api/vehicles/14/', 'http://swapi.dev/api/vehicles/30/'], 'starships': ['http://swapi.dev/api/starships/12/', 'http://swapi.dev/api/starships/22/'], 'created': '2014-12-09T13:50:51.644000Z', 'edited': '2014-12-20T21:17:56.891000Z', 'url': 'http://swapi.dev/api/people/1/'}\n"
     ]
    }
   ],
   "source": [
    "import urllib\n",
    "import json\n",
    "url = \"https://swapi.dev/api/people/1/\"\n",
    "response = urllib.request.urlopen(url)\n",
    "data = json.loads(response.read())\n",
    "print (data)\n",
    "with open(\"test_json.json\",\"w\") as file:\n",
    "    json.dump(data,file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
