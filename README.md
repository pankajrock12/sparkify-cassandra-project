# Sparkify Data Warehouse Project

## Overview
End-to-end ETL pipeline using AWS Redshift and S3.

## Steps
1. Configure dwh.cfg
2. Run create_tables.py
3. Run etl.py

## Tables
Fact: songplays
Dimensions: users, songs, artists, time

## Architecture
S3 → Staging → Star Schema → Analytics
