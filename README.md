# CTW 課題

このプロジェクトは、日本の[CTW株式会社](https://ctw.inc/)から提供された課題の一環として開発されました。これには、課題要件に従って、元の[リポジトリ](https://github.com/G123-jp/python_assignment)をフォークすることが含まれています。このプロジェクトのタスクは以下の通りです：

1. **株価データの取得**：[AlphaVantage](https://www.alphavantage.co/)から株価データを取得する機能を実装します。特に、最近2週間のIBMとApple Inc.の株価データを取得することに焦点を当てています。
2. **APIの開発**：取得した株価データを問い合わせ、分析するためのAPIを提供します。これには、パラメータベースのフィルタリングやページネーションなどの機能を備えた金融データ取得用APIの開発、および指定期間の平均始値、終値、出来高などを計算する統計分析用APIの開発が含まれます。
このプロジェクトの主な目的は、AlphaVantageから効果的に株価データを取得し、データの問い合わせと分析のための堅牢なAPIを提供することです。

### タスク1：財務データの取得と処理
- AlphaVantage を使用して、IBMとApple Inc.の最近2週間の財務データを取得します。
- データを処理し、ローカルDBの `financial_data` テーブルに挿入します。

### タスク2：APIサービスの実装
- **財務データ取得APIの開発**：`financial_data` テーブルからレコードを取得するAPIを実装します。このAPIは、パラメータベースのフィルタリング（例：start_date、end_date、symbol）およびページネーション（例：limit、page）をサポートする必要があります。APIは、データとページネーションの詳細を返すべきです。
- **統計分析APIの開発**: 財務データに対して統計分析を行うAPIを実装します。このAPIは、指定された期間の平均始値、終値、出来高などを計算する必要があります。エンドポイントは、start_date、end_date、symbolsなどのパラメータを受け入れ、計算された統計結果を返すべきです。

## テックスタック
このプロジェクトで使用された技術スタックは以下の通りです:
- Python 3.10
- SQLAlchemy
- FastAPI
- Docker
- Poetry
- Postgres

## 始め方
1. **リポジトリのクローン**: ローカルマシンにリポジトリをクローンします。
    ```
    git clone git@github.com:tetsufromtw/python_assignment.git
    ```
2. **APIキーの取得**: https://www.alphavantage.co/support/#api-key からAPIキーを取得してください。
3. **環境変数の設定**: `env_template` を `.env` に名前を変更し、`ALPHAVANTAGE_API_KEY` の値を設定します。このステップには、APIキーで `.env` ファイルを修正する作業が含まれます。
    ```
    mv env_template .env
    vim .env
    ```
    - `.env` 内で、`DEMO`を実際のAPIキーに置き換えてください：
      ```
      ALPHAVANTAGE_API_KEY=YourActualAPIKey
      ```
4. **Dockerイメージのビルド**: プロジェクトディレクトリで、以下のコマンドを使用してDockerイメージをビルドします。
    ```
    docker-compose build
    ```
5. **サーバーの起動**:　ビルド後、次のコマンドでサーバーを起動します。
     ```
     docker-compose up
     ```
6. **データの取得と挿入**: これにより、最近2週間の株価データを取得し、Postgresデータベースに挿入します。

## APIの使用方法
**始め方**の第六ステップが完了すると、サーバーも立ち上がります。この時点で、以下の二つのAPIを使用してデータを照会することができます。
1. **財務データの取得API**: `GET localhost:port/api/financial_data`
   - デフォルトのポートは8000です。
   - 以下は使用例です。必要に応じてパラメータを調整してください。
     ```
     127.0.0.1:8000/api/financial_data?start_date=2024-01-10&end_date=2024-01-20&symbol=IBM&limit=3&page=2
     ```
2. **統計データの取得API**：`GET localhost:port/api/statistics`
   - デフォルトのポートは8000です。
   - 以下は使用例です。必要に応じてパラメータを調整してください。
     ```
     127.0.0.1:8000/api/statistics?start_date=2024-01-10&end_date=2024-01-20&symbol=IBM
     ```

## データベースのリセット
データベースをリセットしたい場合は、以下のコマンドを使用できます：
```
docker-compose down --volumes
```
これにより、Postgresのボリュームが削除され、データベース内のすべてのデータが消去されます。

# CTW Assignment
This project is developed as part of an assignment provided by [CTW Inc](https://ctw.inc/?lang=en). It involved forking the [original repository](https://github.com/G123-jp/python_assignment) in accordance with the assignment's requirements. The tasks of this project are listed as follows:

1. **Retrieve Stock Data**: Implement functionality to fetch stock data from [AlphaVantage](https://www.alphavantage.co/). The focus is on retrieving financial data of two specific stocks (IBM and Apple Inc.) for the most recent two weeks.
2. **API Development**: Provide APIs for querying and analyzing the retrieved stock data. This includes developing an API for financial data retrieval with features such as parameter-based filtering and pagination, and another API for statistical analysis, calculating averages like daily open price, closing price, and volume for a given period.
The primary objective of this project is to effectively retrieve stock data from AlphaVantage and to offer robust APIs for data querying and analysis purposes.

## Specific Tasks and Requirements
### Task 1: Financial Data Retrieval and Processing
- Retrieve financial data for IBM and Apple Inc. for the most recent two weeks using [AlphaVantage](https://www.alphavantage.co/).
- Process the raw API data and insert it into a `financial_data` table in the local database.
### Task 2: API Service Implementation
- Develop a Financial Data Retrieval API: Implement an API to retrieve records from the `financial_data` table. This API should support parameter-based filtering (e.g., start_date, end_date, symbol) and pagination (e.g., limit and page). The API should return data along with pagination details.
- Develop a Statistical Analysis API: Implement an API to perform statistical analysis on the financial data. This API should calculate averages such as the daily open price, closing price, and volume for a specified period. The endpoint should accept parameters like start_date, end_date, and symbols, and return the calculated statistical results.
  
## Tech Stack

The tech stack used in this project includes:

- Python 3.10
- SQLAlchemy
- FastAPI
- Docker
- Poetry
- Postgres

## Getting Started

1. **Clone the Repository**: Clone the repository to your local machine.
```
git clone git@github.com:tetsufromtw/python_assignment.git
```
2. **Obtain an API Key**: Get your API key from https://www.alphavantage.co/support/#api-key
3. **Setup Environment Variables**: Rename `env_template` to `.env`, and then set the `ALPHAVANTAGE_API_KEY` value. This step involves modifying the `.env` file with your API key.
```
mv env_template .env
vim .env
```
- Inside `.env`, replace `DEMO` with your actual API key:
```
ALPHAVANTAGE_API_KEY=YourActualAPIKey
```
4. **Build the Docker Image**: In the project directory, build the Docker image using the following command:
```
  docker-compose build
```
5. **Start the Server**: After building, start the server with this command:
```
docker-compose up
```
6. **Data Retrieval and Insertion**: This will retrieve the stock data for the most recent two weeks and insert it into the Postgres database.



### Get Financial Data

The default port of the server is 8000. Here is a sample request for getting financial data:
```
127.0.0.1:8000/api/financial_data?start_date=2024-01-01&end_date=2024-01-14&symbol=IBM&limit=3&page=2
```

### Get Statistics Data

The default port of the server is 8000. Here is a sample request for getting statistics data:

```
127.0.0.1:8000/api/statistics?start_date=2024-01-01&end_date=2024-01-31&symbol=IBM
```

## Reset Database

If you want to reset the database, you can use the following command:

```angular2html
docker-compose down --volumes
```

This will remove the Postgres volume and delete all data from the database.


