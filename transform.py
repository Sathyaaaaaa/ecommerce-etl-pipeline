import pandas as pd

def transform_data(orders_df, order_details_df, sales_target_df):

    orders_df = orders_df.drop_duplicates().dropna()
    order_details_df = order_details_df.drop_duplicates().dropna()

    
    orders_df["Order Date"] = pd.to_datetime(orders_df["Order Date"], format="%d-%m-%Y")

    merged_df = pd.merge(orders_df, order_details_df, on="Order ID")

    merged_df["total_amount"] = merged_df["Amount"] * merged_df["Quantity"]

    merged_df["month_year"] = merged_df["Order Date"].dt.strftime("%b-%y")


    sales_target_df.rename(columns={
        "Month of Order Date": "month_year"
    }, inplace=True)

    merged_df = pd.merge(
        merged_df,
        sales_target_df,
        on=["month_year", "Category"],
        how="left"
    )

    merged_df["target_status"] = merged_df["total_amount"] >= merged_df["Target"]

    return merged_df