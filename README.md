# Tourism recommendation system

A toy example.

### Requirements

* Any linux distro
* [conda](https://www.anaconda.com/products/individual)

### Setup project

**Step 1**: Create conda environment to run project notebook.

```bash
conda env create -f environment.yml
```

**Step 2**: Enable installed environment.

```bash
conda activate tourism-recommendation-system
```

**Step 3**: Install a upyter extension required to support a progress bar in a notebook.

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

### Getting started Notebook

**Step 1**: Enable installed environment.

```bash
conda activate tourism-recommendation-system
```

**Step 2**: run jupyter lab IDE:

```bash
jupyter lab
```

**Step 3**: Open [toy-example](toy-example.ipynb) jypiter notebook.

**Note**: Can use query browser from http://localhost:7474.


### Getting started API


**Step 1**: Enable installed environment.

```bash
conda activate tourism-recommendation-system
```

**Step 2**: Start api server.

```bash
./start-api
```

**Step 3**: Query trends and recommendations.

**More purchased hotels in last 60 days**

```bash
curl -X  GET "http://localhost:8080/api/recommendations/hotels/more-purchased?time-window=60" | json_pp
```

```json
{
    "hotels": [
        {
            "destination": "SLA",
            "name": "Posada Santana",
            "score": 4
        },
        {
            "destination": "RIO",
            "name": "Hakuna Matata Hotel Bar",
            "score": 3
        },
        {
            "destination": "RIO",
            "name": "Rio See Resort",
            "score": 3
        },
        {
            "destination": "BCN",
            "name": "Barcelona Hotel",
            "score": 2
        },
        {
            "destination": "MIA",
            "name": "Madagascar Palace",
            "score": 1
        }
    ]
}
```

**More searched hotels in last 60 days**

```bash
curl -X  GET "http://localhost:8080/api/recommendations/hotels/more-searched?time-window=60" | json_pp
```

```json
{
   "hotels" : [
      {
         "destination" : "MIA",
         "score" : 23
      },
      {
         "destination" : "BCN",
         "score" : 20
      },
      {
         "destination" : "SLA",
         "score" : 15
      },
      {
         "destination" : "RIO",
         "score" : 10
      },
      {
         "destination" : "COR",
         "score" : 5
      }
   ]
}

```


**More purchased flights in last 60 days**

```bash
curl -X  GET "http://localhost:8080/api/recommendations/flights/more-purchased?time-window=60" | json_pp
```

```json
{
   "flights" : [
      {
         "airline" : "LA",
         "destination" : "SLA",
         "score" : 3
      },
      {
         "airline" : "AA",
         "destination" : "RIO",
         "score" : 2
      },
      {
         "airline" : "LA",
         "destination" : "RIO",
         "score" : 2
      },
      {
         "airline" : "EK",
         "destination" : "BCN",
         "score" : 1
      },
      {
         "airline" : "AA",
         "destination" : "MIA",
         "score" : 1
      }
   ]
}
```

**More purchased flights in last 60 days**

```bash
curl -X  GET "http://localhost:8080/api/recommendations/flights/more-searched?time-window=60" | json_pp
```

```json
{
    "flights": [
        {
            "destination": "SLA",
            "score": 42
        },
        {
            "destination": "BCN",
            "score": 25
        },
        {
            "destination": "RIO",
            "score": 25
        },
        {
            "destination": "MIA",
            "score": 16
        },
        {
            "destination": "COR",
            "score": 5
        }
    ]
}
```


**Recommended hotels for users that bought flights for a given destination in last 60 days**

```bash
curl -X  GET "http://localhost:8080/api/recommendations/cross-selling/hotels?email=adrian.marino@almundo.com&time-window=60" | json_pp
```

```json
{
    "hotels": [
        {
            "city": "SLA",
            "id": "8",
            "name": "Posada Santana",
            "score": 4
        },
        {
            "city": "RIO",
            "id": "12",
            "name": "Hakuna Matata Hotel Bar",
            "score": 3
        },
        {
            "city": "RIO",
            "id": "10",
            "name": "Rio See Resort",
            "score": 2
        },
        {
            "city": "MIA",
            "id": "2",
            "name": "See Palace Resort",
            "score": 1
        },
        {
            "city": "RIO",
            "id": "11",
            "name": "Pipa Hotel",
            "score": 1
        }
    ]
}
```

**Recommended airlines for users that bought hotels in a given city in last 60 days**


```bash
curl -X  GET "http://localhost:8080/api/recommendations/cross-selling/airlines?email=adrian.marino@almundo.com&time-window=60" | json_pp
```

```json
{
    "airlines": [
        {
            "destination": "SLA",
            "name": "LATAM",
            "score": 3
        },
        {
            "destination": "RIO",
            "name": "American Airlines",
            "score": 2
        },
        {
            "destination": "RIO",
            "name": "LATAM",
            "score": 2
        },
        {
            "destination": "MIA",
            "name": "American Airlines",
            "score": 1
        }
    ]
}
```
