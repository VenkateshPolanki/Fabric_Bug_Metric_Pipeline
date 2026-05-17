# Fabric Bug Metric Pipeline

## Project Overview

This project implements an end-to-end Microsoft Fabric data engineering solution using Medallion Architecture (Bronze, Silver, Gold) to analyze Azure DevOps work item bug metrics.

The solution ingests CSV data, performs data cleansing and transformations using PySpark, builds reporting-ready dimensional models, and creates analytical reporting using Power BI.

## Business Requirement

The business requirement is to analyze:

- Number of bugs created per product
- Monthly bug trends
- Product-wise bug distribution

The solution provides a scalable reporting model to support business analytics and decision-making.

## Architecture

Source CSV File  
↓  
Bronze Layer (Raw Ingestion)  
↓  
Silver Layer (Data Cleansing & Transformations)  
↓  
Gold Layer (Star Schema Reporting Model)  
↓  
Semantic Model  
↓  
Power BI Report

## Technologies Used

- Microsoft Fabric
- PySpark
- Delta Lake
- Power BI
- Azure Devops

## Bronze Layer

The Bronze layer is responsible for raw data ingestion.

### Activities Performed

- Loaded CSV source file into Fabric Lakehouse
- Preserved raw source structure
- Added metadata columns:
  - ingestion_timestamp
  - source_file_name
- Performed schema validation
- Validated row counts

### Output Table

- bronze.bronze_azdo_workitems

## Silver Layer

The Silver layer performs data cleansing, standardization, and business transformations.

### Activities Performed

- Removed duplicate records using work_item_id
- Handled null and blank values
- Created bug identification logic using is_bug flag
- Created reporting_month column for analytics
- Applied data quality validations
- Selected only required columns
### Output Table
- silver.silver_workitems

## Gold Layer

The Gold layer creates reporting-ready dimensional models using star schema design.

### Fact Table

- fact_bug_metrics

### Dimension Tables

- dim_product
- dim_date

### Activities Performed

- Generated surrogate keys
- Built star schema relationships
- Optimized model for Power BI reporting

## Reporting

Power BI report was created using the semantic model.

### Report Visuals

- Total Bugs KPI Card
- Bug Count by Product
- Bug Count by Month
- Product vs Month Matrix

## Data Quality Handling

The following data quality checks were implemented:

- Duplicate validation
- Null handling
- Schema validation
- Row count validation
- Standardization of business fields

## Future Improvements

The following enhancements can be implemented in production environments:

- Incremental data loading
- Fabric pipeline orchestration
- CI/CD integration
- Monitoring and alerting
- Partition optimization
- Row-level security (RLS)

Thanks
Venkat
