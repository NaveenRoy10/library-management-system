
# Library Management System

## Overview
This is a Library Management System built using **Python** and **MySQL**. It allows users to manage books, track issued books, and handle various library-related operations efficiently.

## Features
- Add new books to the library database
- Issue books to users
- Return books and update status
- View all available books
- Search for books by title, author, or status
- Manage issued books

## Technologies Used
- **Python** (for backend logic)
- **MySQL** (for database management)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Server
- MySQL Connector for Python

### Setup Instructions

#### 1. Clone the repository:
```sh
https://github.com/NaveenRoy10/library-management-system.git
cd library-management-system
```

#### 2. Install required dependencies:
```sh
pip install mysql-connector-python
```

#### 3. Set up the database:
- Open MySQL and create a database:
```sql
CREATE DATABASE library_db;
```
- Use the database:
```sql
USE library_db;
```
- Run the following SQL commands to create necessary tables:
```sh
create table books_issued(bid varchar(20) primary key, issueto varchar(30));
```
```sh
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
```

#### 4. Run the application:
```sh
python main.py
```

## Usage
1. Choose an operation from the menu.
2. Follow the prompts to add, issue, return, or search for books.
3. View the database updates in MySQL.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## License
This project is licensed under the MIT License.

---
