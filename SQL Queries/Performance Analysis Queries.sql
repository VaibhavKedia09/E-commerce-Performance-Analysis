1) Total revenue
SELECT
  ROUND(SUM(price_usd), 2) AS total_revenue
FROM order_items;

2) Average Order Value (AOV)
SELECT
  ROUND(
    SUM(price_usd) * 1.0 /
    COUNT(DISTINCT order_id), 2
  ) AS average_order_value
FROM order_items;

3) Products generating the most revenue
SELECT
  p.product_name,
  ROUND(SUM(oi.price_usd), 2) AS revenue
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

4) Price vs volume analysis
SELECT
  p.product_name,
  ROUND(AVG(oi.price_usd), 2) AS avg_price,
  COUNT(oi.order_item_id) AS units_sold
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY units_sold DESC;

5) Refund value by product
SELECT
  p.product_name,
  ROUND(SUM(r.refund_amount_usd), 2) AS total_refunds
FROM order_item_refunds r
JOIN order_items oi
  ON r.order_item_id = oi.order_item_id
JOIN products p
  ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_refunds DESC;

6) Refund rate by product
SELECT
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
