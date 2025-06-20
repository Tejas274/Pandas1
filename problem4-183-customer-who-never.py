import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')

    df = df[df['customerId'].isnull()][['name']].rename(columns={'name': 'Customers'})
    return df