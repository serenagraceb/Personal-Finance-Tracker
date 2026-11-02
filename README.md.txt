# Personal Finance Tracker

A simple Personal Finance Tracker built with Python and MySQL.
The project allows users to record income and expenses, calculate totals, and view spending information.

## Features

* Add income and expense records
* Store financial data in MySQL
* Calculate total income and expenses
* Calculate totals by category
* Display financial information using Python
* Create charts using Matplotlib
* Keep the MySQL password secure using environment variables

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* MySQL
* MySQL Connector
* Matplotlib
* python-dotenv

## Project Files

* `main.py` – Main program
* `sub.py` – Functions used by the main program
* `requirements.txt` – Required Python packages
* `.gitignore` – Prevents sensitive files such as `p.env` from being uploaded

## Database

The project uses MySQL to store finance records.

The database contains information such as:

* Amount
* Category
* Income/Expense

## Setup

1. Install Python.
2. Install MySQL.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Create the required MySQL database and table.
5. Create a `p.env` file containing your MySQL password.
6. Run `main.py`.

> **Note:** The `p.env` file contains sensitive information and should never be uploaded to GitHub.

## What I Learned

Through this project, I practiced:

* Python programming
* Object-Oriented Programming
* Functions and modules
* MySQL database connectivity
* Storing and retrieving data
* Environment variables
* Data visualization using Matplotlib
* Working with Git and GitHub
