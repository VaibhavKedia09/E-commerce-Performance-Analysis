E-Commerce Performance Analysis 🛒
Project Overview

This project analyzes e-commerce sales data to understand overall business performance, product-level revenue contribution, pricing behaviour, and refund patterns.

The analysis follows an end-to-end data analytics workflow, starting from raw CSV files and using SQL, Python, and Power BI to generate actionable business insights.

Objectives

Evaluate overall sales performance using key business KPIs

Identify top-performing and underperforming products

Analyse product pricing and sales volume relationships

Understand refund behaviour and potential revenue leakage

Build an interactive and professional Power BI dashboard

Dataset

Source: Maven Analytics (Toy Store E-commerce Dataset)

Initial Format: CSV files

Data Scope:

Website sessions

Orders

Order items

Products

Refunds

Tools Used

SQLite (SQL) – Data aggregation, joins, KPI calculations

Python (Pandas) – Data validation, cleaning, and CSV exports

Power BI – Interactive dashboard and data visualization

GitHub – Project version control and portfolio hosting

Key KPIs

Total Revenue

Average Order Value (AOV)

Total Website Sessions

Total Orders

Conversion Rate

Refund Rate

Product-level Revenue and Sales Volume

Power BI Dashboard

An interactive Power BI dashboard was created using cleaned and analysis-ready datasets exported from Python.

📊 Key visuals include:

Executive KPI cards (Revenue, AOV, Conversion Rate)

Revenue by Product

Units Sold by Product

Average Selling Price by Product

Refund Value and Refund Rate by Product

Product-level slicer for interactive analysis

SQL Analysis

SQL (SQLite) was used to join relational tables and calculate KPIs before visualization.

Sample SQL Query – Conversion Rate

SELECT
  COUNT(DISTINCT ws.website_session_id) AS total_sessions,
  COUNT(DISTINCT o.order_id) AS total_orders,
  ROUND(
    COUNT(DISTINCT o.order_id) * 1.0 /
    COUNT(DISTINCT ws.website_session_id), 4
  ) AS conversion_rate
FROM website_sessions ws
LEFT JOIN orders o
  ON ws.website_session_id = o.website_session_id;


All SQL queries used in this project are available in the repository as a .sql file.

Key Insights

The Original Mr. Fuzzy is the highest revenue-generating and most sold product.

A small number of products contribute to the majority of total revenue.

The Birthday Sugar Panda has the highest refund rate, indicating potential quality or expectation issues.

Higher-priced products generally show lower refund rates.

Refund analysis highlights areas of revenue leakage that can be improved.

Business Recommendations

Focus marketing and inventory planning on top-performing products.

Investigate products with high refund rates to reduce losses.

Improve product descriptions or quality checks for frequently refunded items.

Diversify product offerings to reduce dependency on a single product.
