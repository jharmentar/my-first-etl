
# My first ETL project

## Description
Pipeline ETL that processes e-commerce data to generate sales metrics.

## How to run
```bash
pip install pandas pyarrow
python etl.py
```

## Clean decisions
- **Types**: Convert order_date to datetime, total and quantity to numeric

## Output
- `sales_by_customer.csv`: Total Spend & Order Count per Customer
- `sales_by_month.csv`: Total Spend per Month
- `orders_clean.parquet`: Clean dataset in optimized format

## Autor
[Josue Armenta] - [2025-12-29]
