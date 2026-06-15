# NBA Revenue Intelligence — Data Dictionary

## Overview

This document describes the core datasets used in the NBA Revenue Intelligence platform.

The project contains three major data layers:

- **Warehouse tables**: simulated dimensional and fact tables
- **Analytics outputs**: model-ready and executive reporting datasets
- **SQL views**: dashboard-ready reporting views

---

## Warehouse Tables

| Table | Description | Primary Key |
|---|---|---|
| `dim_games` | Game schedule and game-level metadata | `game_id` |
| `dim_customers` | Simulated customer demographic and loyalty attributes | `customer_id` |
| `dim_sections` | Arena seating sections, capacities, and base prices | `section_id` |
| `dim_promotions` | Promotional offers and discount levels | `promotion_id` |
| `fact_ticket_transactions` | Simulated ticket purchase transactions | `transaction_id` |
| `fact_web_sessions` | Simulated web/app funnel activity | `session_id` |

---

## Analytics Outputs

| Dataset | Description |
|---|---|
| `model_dataset` | Game-level feature dataset used for segmentation and forecasting |
| `game_segments` | K-Means demand segment assignments and recommendations |
| `revenue_forecasts` | Predicted tickets sold, predicted revenue, and sellout probability |
| `executive_kpis` | Aggregated executive KPI summary |
| `executive_recommendations` | Game-level business recommendations |

---

## Key Metrics

| Metric | Description |
|---|---|
| `total_revenue` | Total ticket revenue generated for a game |
| `tickets_sold` | Total seats sold for a game |
| `sell_through_rate` | Percentage of arena capacity sold |
| `inventory_remaining` | Unsold seats remaining |
| `avg_ticket_price` | Average ticket price paid |
| `cart_rate` | Share of web sessions that added tickets to cart |
| `checkout_rate` | Share of cart sessions that started checkout |
| `purchase_rate` | Share of web sessions that completed purchase |
| `cart_abandonment_rate` | Share of cart sessions that did not convert to purchase |
| `predicted_revenue` | Forecasted ticket revenue |
| `sellout_probability` | Estimated likelihood of selling out |

---

## `dim_games`

| Column | Description |
|---|---|
| `game_id` | Unique game identifier |
| `game_date` | Date of the game |
| `opponent` | Opposing team abbreviation |
| `day_of_week` | Day of week for the game |
| `is_weekend` | Indicator for Friday, Saturday, or Sunday games |
| `opponent_strength` | Simulated demand score for the opponent |
| `arena_capacity` | Total arena capacity |

---

## `fact_ticket_transactions`

| Column | Description |
|---|---|
| `transaction_id` | Unique transaction identifier |
| `customer_id` | Customer associated with the purchase |
| `game_id` | Game associated with the transaction |
| `section_id` | Seating section purchased |
| `promotion_id` | Promotion applied to transaction |
| `purchase_date` | Date ticket purchase occurred |
| `seats_purchased` | Number of seats purchased |
| `ticket_price` | Final ticket price after dynamic pricing and promotions |
| `revenue` | Transaction revenue |
| `channel` | Purchase channel |
| `device` | Device used for purchase |

---

## `fact_web_sessions`

| Column | Description |
|---|---|
| `session_id` | Unique web session identifier |
| `game_id` | Game viewed during the session |
| `device` | Device used during session |
| `source` | Marketing/source channel |
| `viewed_ticket_page` | Whether the user viewed the ticket page |
| `added_to_cart` | Whether the user added tickets to cart |
| `checkout_started` | Whether the user began checkout |
| `purchased` | Whether the user completed purchase |