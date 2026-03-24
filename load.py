import mysql.connector
import pandas as pd
import logging

def get_last_loaded_date(cursor):
    cursor.execute("SELECT MAX(order_date) FROM ecommerce_data")
    result = cursor.fetchone()
    return result[0] if result[0] else None


def load_data(df):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sathya@123",
        database="ecommerce_db"
    )

    cursor = conn.cursor()
    logging.info("Connected to MySQL")

    # Ensure datetime format
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # Incremental loading
    last_date = get_last_loaded_date(cursor)

    if last_date:
        last_date = pd.to_datetime(last_date)
        df = df[df["Order Date"] > last_date]

    logging.info(f"New records to insert: {len(df)}")

    # Insert data
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO ecommerce_data (
            order_id, order_date, customer_name, state, city,
            amount, profit, quantity, category, sub_category,
            total_amount, target, target_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["Order ID"],
            row["Order Date"],
            row["CustomerName"],
            row["State"],
            row["City"],
            row["Amount"],
            row["Profit"],
            row["Quantity"],
            row["Category"],
            row["Sub-Category"],
            row["total_amount"],
            row["Target"],
            row["target_status"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

    logging.info("Data inserted successfully")