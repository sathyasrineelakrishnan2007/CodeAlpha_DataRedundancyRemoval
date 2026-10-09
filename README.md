# CodeAlpha_DataRedundancyRemoval
Data Redundancy Removal System


# Agile Data Guard
## Data Redundancy Removal System

Agile Data Guard is a Python-based project that
detects duplicate text records and stores only
unique records in an SQLite database.

## Features
- Detects duplicate records
- Ignores differences in letter case
- Handles extra spaces
- Stores unique records in SQLite
- Displays saved records
- Uses parameterized SQL queries

## Technologies Used
- Python
- SQLite
- SHA-256 hashing

## How It Works
1. The user enters a text record.
2. The system normalizes the text.
3. A fingerprint is generated.
4. Duplicate records are rejected.
5. Unique records are stored in the database.

## Project File
- main.py

## Note
This project is a learning prototype.
