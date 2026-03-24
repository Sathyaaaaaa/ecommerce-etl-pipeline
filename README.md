# 🛒 E-commerce ETL Pipeline

## 📌 Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, and MySQL.

It extracts raw e-commerce data, transforms it into meaningful insights, and loads it into a MySQL database.

---

## ⚙️ Tech Stack

* Python
* Pandas
* MySQL
* Logging
* Git & GitHub

---

## 🔄 ETL Workflow

### 1. Extract

* Reads data from CSV files:

  * orders.csv
  * order_details.csv
  * sales_target.csv

### 2. Transform

* Removes duplicates and null values
* Converts date formats
* Merges datasets
* Calculates total_amount
* Adds monthly target data
* Creates target_status (Target achieved or not)

### 3. Load

* Loads processed data into MySQL
* Supports incremental loading

---

## 📊 Features

* Automated ETL pipeline
* Data cleaning & transformation
* Target vs Actual analysis
* Logging system

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📁 Project Structure

ecommerce_etl_pipeline/
│
├── data/
├── extract.py
├── transform.py
├── load.py
├── main.py
├── config.py
├── .gitignore

---

## 👨‍💻 Author

K Ajay Sathya
