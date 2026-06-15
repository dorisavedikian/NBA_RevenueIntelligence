# NBA Revenue Intelligence — System Architecture

## Overview

NBA Revenue Intelligence is an end-to-end analytics platform that simulates the ticketing and revenue analytics workflows of a professional sports organization.

The platform follows a layered architecture in which each component has a single responsibility, allowing data to flow from raw operational events to executive decision support.

---

## High-Level Architecture

```
                    NBA Schedule (nba_api)
                            │
                            ▼
                Simulation Engine (Python)
                            │
                            ▼
              Raw Ticketing & Web Activity
                            │
                            ▼
                     ETL Pipeline
                            │
                            ▼
              SQLite Data Warehouse
             (Dimensions + Fact Tables)
                            │
                            ▼
                Feature Engineering
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
        K-Means Clustering        Regression Models
              │                           │
              └─────────────┬─────────────┘
                            ▼
                 Executive Analytics
          KPIs • Forecasts • Recommendations
                            │
                            ▼
                    SQL Reporting Views
                            │
                            ▼
                   Power BI Dashboard
```

---

# Architecture Layers

## 1. Data Simulation

The simulation engine generates realistic business data using actual NBA schedules as the foundation.

Generated datasets include:

- Games
- Customers
- Arena sections
- Promotions
- Ticket transactions
- Website sessions

The synthetic data models:

- Dynamic pricing
- Customer purchasing behavior
- Promotional campaigns
- Checkout funnels
- Inventory management

---

## 2. ETL Layer

The ETL process validates and loads CSV datasets into a centralized SQLite warehouse.

Responsibilities include:

- Reading source files
- Loading dimension tables
- Loading fact tables
- Building a relational warehouse
- Preserving referential integrity

---

## 3. Data Warehouse

The warehouse follows a dimensional star schema optimized for analytics.

### Dimension Tables

- dim_games
- dim_customers
- dim_sections
- dim_promotions

### Fact Tables

- fact_ticket_transactions
- fact_web_sessions

---

## 4. Feature Engineering

Business metrics are aggregated into a game-level modeling dataset.

Examples include:

- Revenue
- Tickets sold
- Sell-through rate
- Inventory remaining
- Promotion usage
- Checkout conversion
- Cart abandonment

---

## 5. Machine Learning

Two machine learning workflows support business decision-making.

### K-Means Clustering

Segments games into demand profiles:

- Premium Demand
- Promotion Opportunity
- Inventory Risk

### Regression

Forecasts:

- Ticket demand
- Revenue
- Sellout probability

---

## 6. Executive Analytics

Business intelligence modules calculate:

- Executive KPIs
- Revenue summaries
- Forecast metrics
- Business recommendations

Outputs are exported as CSV files and SQL tables for downstream reporting.

---

## 7. Reporting Layer

SQL views expose dashboard-ready datasets for reporting tools.

These views simplify querying and separate analytical logic from presentation.

---

## Design Principles

The project emphasizes software engineering best practices:

- Modular package architecture
- Separation of concerns
- Centralized configuration
- Reproducible analytics pipeline
- Automated testing
- Continuous Integration (GitHub Actions)
- Enterprise-style project organization
- Dashboard-ready outputs

---

## End-to-End Workflow

```
NBA API
    ↓
Simulation
    ↓
ETL
    ↓
SQLite Warehouse
    ↓
Feature Engineering
    ↓
Machine Learning
    ↓
KPIs
    ↓
Recommendations
    ↓
SQL Views
    ↓
Power BI Dashboard
```