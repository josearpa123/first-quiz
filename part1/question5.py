################################################################################
#     ____                          __     _                           ______
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____           / ____/
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         /___ \  
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ____/ /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_____/   
#                                                                            
#  Question 5
################################################################################
#
# Instructions:
# This questions continues to use the database we worked with in Question 4. In 
# this question, we will made some modifications ot the table.

# Part 5.A:
# Create a new table, 'favorite_foods.' It should have the columns:
# food_id integer
# name text
# vegetarian integer

# SQL code for question5.py

# Part 5.A:
# Create a new table, 'favorite_foods.'
sql_create_favorite_foods = """
CREATE TABLE favorite_foods (
    food_id integer,
    name text,
    vegetarian integer
);
"""

# Part 5.B:
# Alter the animals and people tables by adding a new 'favorite_food_id' column.
sql_alter_tables_with_favorite_food = """
ALTER TABLE animals ADD COLUMN favorite_food_id integer;
ALTER TABLE people ADD COLUMN favorite_food_id integer;
"""

# Part 5.C:
# Query to select all vegetarian pets.
sql_select_all_vegetarian_pets = """
SELECT a.name, ff.name
FROM animals a
JOIN favorite_foods ff ON a.favorite_food_id = ff.food_id
WHERE ff.vegetarian = 1;
"""
