# 🚗 Car Rental Exercise 🚗


## How to run and use the application

Running Application with Django:

```sh
$ python3 manage.py runserver
```

Once running, here are some example requests assuming the `PORT` is set to `8000`:

```bash
# Upload a vehicle
curl -X POST "http://localhost:8000/vehicles/" -H "Content-Type: application/json" -d '{"v_type": "suv", "plate_number": "restful" }'
# Responds with:
# {
#   "plate_number" : "restful",
#   "v_type" : "suv"         
# }
```

```bash
# Upload a reservation
curl -X POST "http://localhost:8000/reservations/" -H "Content-Type: application/json" -d '{"v_type": "suv", "start_time" : "20240401T12:00", "end_time" : "20240402T16:00"}'
# Responds with:
# {
#   "id" : 1,
#   "v_type" : "suv",
#   "plate_number" : "restful",  
#   "start_time": "2024-04-01T12:00:00Z",
#   "end_time": "2024-04-02T16:00:00Z",
# }
```

Tests can be run using the following command

```bash
python3 manage.py test
```


## Database Models

The database contains two models: `vehicles` and `reservations`

#### Vehicles

| Fields | Type | Key |
| - | - | - |
| plate_number | string | Primary |
| v_type | string | |

Assumptions:
- It is assumed that license plate numbers are all unique, and will not change


### Reservations

| Fields | Type | Key |
| - | - | - |
| id | int | Primary |
| v_type | string | |
| start_time | DateTimeField | |
| end_time | DateTimeField | | 
| plate_number | string | Foreign |

Design Notes:
- When a post request is made for a reservation, each `Vehicle` with a matching `v_type` is selected, then the `Reservations` table is checked for any overlap, the first vehicle with no overlap is selected

