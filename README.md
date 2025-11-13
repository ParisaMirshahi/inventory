#Shoe Inventory Manager

A Python-based inventory management system for tracking shoe products, their cost, and quantity. This project demonstrates object-oriented programming, file handling, and basic data parsing.

# Overview

The program defines a `Shoe` class and reads inventory data from a text file (`inventory.txt`). Each line in the file is converted into a `Shoe` object and stored in a list for further processing.

# Features

- `Shoe` class with attributes: country, code, product, cost, and quantity
- Methods to retrieve cost and quantity
- String representation for easy display
- Reads and parses inventory data from `inventory.txt`
- Stores all shoe objects in a global `shoe_list`

# How It Works

1. `inventory.txt` contains shoe data in CSV format.
2. `read_shoes_data()` opens the file, skips the header, and reads each line.
3. Each line is split into components and used to create a `Shoe` object.
4. All objects are stored in `shoe_list` for future use.

# File Structure
inventory.txt        Input file with shoe data
inventory.py    Main Python script 

# inventory.txt Format

The file should look like this:
Country,Code,Product,Cost,Quantity
UK,SKU001,Nike Air Max,120.0,10
US,SKU002,Adidas Ultraboost,150.0,5

#Author
Parisa Mirshahi





