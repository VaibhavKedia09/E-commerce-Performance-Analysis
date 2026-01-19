import sqlite3
import pandas as pd
import matplotlib.pyplot as pl

#connecting to the database
con = sqlite3.connect(r"C:\Users\vaibh\e_commerce.db")

#importing data through queries
qry1 = """SELECT
  COUNT(DISTINCT ws.website_session_id) AS total_sessions,
  COUNT(DISTINCT o.order_id) AS total_orders,
  ROUND(
    COUNT(DISTINCT o.order_id) * 1.0 /
    COUNT(DISTINCT ws.website_session_id), 4
  ) AS conversion_rate
FROM website_sessions ws
LEFT JOIN orders o
  ON ws.website_session_id = o.website_session_id;
"""

#validation
df1 = pd.read_sql(qry1,con)
df1.info()
df1.isna().sum()
print(df1)


qry2 = """SELECT
  ROUND(SUM(price_usd), 2) AS total_revenue
FROM order_items;
"""
df2 = pd.read_sql(qry2,con)
print(df2)


qry3 = """SELECT
  ROUND(
    SUM(price_usd) * 1.0 /
    COUNT(DISTINCT order_id), 2
  ) AS average_order_value
FROM order_items;
"""

df3 = pd.read_sql(qry3, con)
print(df3)


qry4 = """SELECT
  p.product_name,
  ROUND(SUM(oi.price_usd), 2) AS revenue
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;
"""

df4 = pd.read_sql(qry4, con)
print(df4)


qry5 = """SELECT
  p.product_name,
  ROUND(AVG(oi.price_usd), 2) AS avg_price,
  COUNT(oi.order_item_id) AS units_sold
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY units_sold DESC;
"""

df5 = pd.read_sql(qry5, con)
print(df5)


qry6 = """SELECT
  p.product_name,
  ROUND(SUM(r.refund_amount_usd), 2) AS total_refunds
FROM order_item_refunds r
JOIN order_items oi
  ON r.order_item_id = oi.order_item_id
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_refunds DESC;
"""

df6 = pd.read_sql(qry6, con)
print(df6)


qry7 = """SELECT
  p.product_name,
  COUNT(DISTINCT r.order_item_id) AS refunded_items,
  COUNT(DISTINCT oi.order_item_id) AS total_items,
  ROUND(
    COUNT(DISTINCT r.order_item_id) * 1.0 /
    COUNT(DISTINCT oi.order_item_id), 4
  ) AS refund_rate
FROM order_items oi
LEFT JOIN order_item_refunds r
  ON oi.order_item_id = r.order_item_id
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY refund_rate DESC;
"""

df7 = pd.read_sql(qry7, con)
print(df7)


#merging kpis in one dataframe
df_kpis = pd.concat([df1, df2, df3], axis = 1)
print(df_kpis)


#exporting to csv
df_kpis.to_csv("executive_kpis.csv", index = False)
df4.to_csv("product_revenue.csv", index = False)
df5.to_csv("price_volume.csv", index = False)
df6.to_csv("refund_value.csv", index = False)
df7.to_csv("refund_rate.csv", index = False)

print("Export Successful")
