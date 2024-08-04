# Rigz Finance Tracker

## Overview

The Personal Finance Tracker is a Python application designed to help users manage their personal finances. It allows users to register, sign in, add transactions, view transactions, and generate financial reports. The application uses SQLite for database management and demonstrates object-oriented programming principles.

## Features

- **User Registration**: Create an account with name, phone number, email, and password.
- **User Sign In**: Sign in with email and password.
- **Transaction Management**: Add transactions and view them using various filters.
- **Financial Reports**: Generate reports to view income, expenses, and net balance.

## Prerequisites

- Python 3.x
- SQLite (included with Python)

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/personal-finance-tracker.git
   cd personal-finance-tracker

## Code Structure
lib/models/_init_.py: Initializes the database and creates the necessary tables.
lib/models/transaction.py: Defines the Transaction class for managing transactions.
lib/models/user.py: Defines the User class for managing user information.
lib/cli.py: Provides the command-line interface for user interaction.
lib/helpers.py: Contains helper functions for user registration, sign-in, and transaction management.