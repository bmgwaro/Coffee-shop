# Coffee Shop Management System

## Description
This project simulates a coffee shop management system where customers can place orders for different types of coffee. The system is built around three primary classes: `Coffee`, `Customer`, and `Order`. Each class interacts with one another to manage and track customer orders, compute various statistics, and maintain relationships between customers and their orders.

The project allows you to:
- Create instances of customers and coffee types.
- Place orders, including assigning prices to them.
- View details of all orders associated with specific coffee types.
- Retrieve customers who ordered particular coffee types.
- Calculate the number of orders and the average price for any coffee type.

## Prerequisites
- Python Interpreter

- Code Editor or Integrated Development Environment (IDE)

- Command Line or Terminal


## Getting Started

1.  Click on [this link](https://github.com/bmgwaro/Coffee-shop) in order to access the github repository containing this project.
2.  Click on fork to create copy of the repository.

3.  Open your terminal and navigate into the directory where you would like to save the work using the `cd` command.

         cd <directory_name>

4.  Copy and paste the following command in order to clone the repository into your local storage. Remember to replace `your_github_username` with your actual username.

         git clone git@github.com:your_github_username/Coffee-shop

5.  Navigate into the newly cloned folder and type in the `code .` command in order to open it on your text editor.

6. In order to run the files in your terminal, you can use `python/python3`. This command followed by the file you would like to run will execute the program. For example to run the main.py file you can write `python3 lib/main.py`

## Features

### Coffee Class:
- **Add Orders:** Assigns orders to specific coffee types.
- **List Orders:** Retrieves all orders associated with a specific coffee.
- **List Customers:** Gets all customers who ordered a particular coffee.
- **Number of Orders:** Calculates how many orders were made for a specific coffee.
- **Average Price:** Computes the average price for a particular coffee based on its orders.

### Customer Class:
- **Place Orders:** Customers can place new orders for any coffee with a specified price.
- **List Orders:** View all orders made by a specific customer.
- **List Coffees Ordered:** Get a list of distinct coffee types a customer has ordered.

### Order Class:
- **Order Creation:** Validates that each order is associated with a valid `Customer`, `Coffee`, and `Price` (within a specified range).
- **Relationship Management:** Orders link customers and coffee types.

