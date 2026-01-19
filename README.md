# E-Commerce Performance Analysis 🛒

## Project Overview  
This project analyzes e-commerce sales data to evaluate business performance, product contribution, and refund behavior. The analysis focuses on identifying revenue drivers, understanding pricing and sales volume patterns, and highlighting areas of potential revenue leakage through refunds.

The analysis was conducted using **SQL (SQLite) for data aggregation**, **Python for data validation and export**, and **Power BI for interactive dashboarding**.

----

## Objectives  
- Analyze overall sales performance and key business KPIs  
- Identify top-performing products by revenue and sales volume  
- Understand product pricing patterns  
- Analyze refund value and refund rate by product  
- Build a clean and professional Power BI dashboard for business insights  

---

## Dataset  
Source: Maven Analytics (Toy Store E-commerce Dataset)  
Data Format: CSV files  
Records: Order-level and product-level transactional data  

---

## Tools Used  
- **SQLite (SQL)** – Data aggregation, joins, and KPI calculations  
- **Python** – Data validation, cleaning, and exporting analysis-ready datasets  
- **Power BI** – Interactive dashboard creation and visualization  
- **GitHub** – Project version control and portfolio hosting  

---

## Key KPIs  
- **Total Revenue**  
- **Average Order Value (AOV)**
- **Total Orders**
- **Conversion Rate**
- **Revenue by Product**
- **Units Sold by Product**
- **Refund Value and Refund Rate**

---

## Power BI Dashboard  
An interactive Power BI dashboard was created using cleaned and aggregated datasets exported from Python.

📊 Key visuals include:  
- Executive KPI cards (Revenue, AOV, Conversion Rate)  
- Revenue contribution by product  
- Sales volume (units sold) by product  
- Average selling price by product  
- Refund value and refund rate analysis  
- Product-level slicer for interactive filtering  

---

## SQL Analysis  
SQL was used to aggregate raw transactional data and calculate business metrics before visualization.

Sample SQL Query – Revenue by Product  
```sql
SELECT
  p.product_name,
  ROUND(SUM(oi.price_usd), 2) AS revenue
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;
```
---

## Key Insights
 - The Original Mr. Fuzzy is the highest revenue-generating and best-selling product.
 - A small number of products contribute to the majority of total revenue.
 - The Birthday Sugar Panda shows a relatively high refund rate, indicating potential quality or expectation issues.
 - Higher-priced products generally have lower refund rates, suggesting better perceived value.

## Business Recommendations
 - Prioritize inventory and marketing efforts for top-performing products.
 - Investigate high-refund products to identify quality, pricing, or description gaps.
 - Use refund rate as a quality and customer satisfaction metric.
 - Reduce dependency on a single product by diversifying product offerings.
