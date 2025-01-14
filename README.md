# Data Transformation API

## Setup Instructions

1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Go to transformation_project: `cd transformation_project`
4.  Run migrations: `python manage.py makemigrations` and `python manage.py migrate`

## Command to Run Server

- Start the server: `python manage.py runserver`

## Testing

Run `pytest` to execute the tests.

## API Documentation

Access Swagger at `http://127.0.0.1:8000/swagger/`.

## POST Endpoint

**URL**: `http://127.0.0.1:8000/api/sort-numbers/`

**Method**: `POST`

**Content-Type**: `application/json`

**Request Body**:

```json
{
  "numbers": [19, 4, 12]
}
```

**Response**:

- **200 Created**: Successfully processed the data.
- **400 Bad Request**: Bad Request with custom message detailing the error.

**Example**:

```bash
curl --location 'http://127.0.0.1:8000/api/sort-numbers/' \
--header 'Content-Type: application/json' \
--data '{
    "numbers": [19,4,12]
}'
```

**Example output**

```json
{
  "sorted_numbers": [4, 12, 19]
}
```
