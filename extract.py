import pandas as pd

def extract_data():
    orders_df = pd.read_csv("data/orders.csv")
    order_details_df = pd.read_csv("data/order_details.csv")
    sales_target_df = pd.read_csv("data/sales_target.csv")

    return orders_df, order_details_df, sales_target_df