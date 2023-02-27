# CTW Assignment

The assignment is made by CTW for retrieving the stock data from AlphaVantage and providing APIs for querying and analyzing from stock data.

## Tech Stack

The tech stack used in this project includes:

- Python 3.10
- SQLAlchemy
- FastAPI
- Docker
- Poetry
- Postgres

## Getting Started

1. Clone the repository to your local machine.
2. Get APIKEY from https://www.alphavantage.co/support/#api-key
3. Rename env_template to .env, and set the value of ALPHAVANTAGE_API_KEY
4. Build the image by running the following command in the project directory:

```angular2html
docker-compose build
```
5. After building, start the server by running the following command:
```angular2html
docker-compose up
```
6. This will retrieve the stock data which is in the most recent two weeks and insert it into Postgres.

### Get Financial Data

The default port of the server is 8000. Here is a sample request for getting financial data:
```angular2html
127.0.0.1:8000/api/financial_data?start_date=2023-01-01&end_date=2023-01-14&symbol=IBM&limit=3&page=2
```

### Get Statistics Data

The default port of the server is 8000. Here is a sample request for getting statistics data:

```angular2html
127.0.0.1:8000/api/statistics?start_date=2023-01-01&end_date=2023-01-31&symbol=IBM
```


## API KEY Management

To retrieve financial data from AlphaVantage, you will need an API key. You should never store this API key 
in your code or in version control, as it can be a security risk.

In both local development and production environments, you should set the API key as an environment variable. 
This can be done in a .env file in your environment.

To retrieve the API key in your code, you can use the `os.getenv()` 
method to read the value of the environment variable.

## Reset Database

If you want to reset the database, you can use the following command:

```angular2html
docker-compose down --volumes
```

This will remove the Postgres volume and delete all data from the database.


