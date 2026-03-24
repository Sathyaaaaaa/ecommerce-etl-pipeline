import config
import logging
from extract import extract_data
from transform import transform_data
from load import load_data

logging.info("ETL Pipeline Started")

orders_df, order_details_df, sales_target_df = extract_data()
logging.info("Data Extracted Successfully")

final_df = transform_data(orders_df, order_details_df, sales_target_df)
logging.info("Data Transformed Successfully")

load_data(final_df)
logging.info("Data Loaded into MySQL")

logging.info("ETL Pipeline Completed")