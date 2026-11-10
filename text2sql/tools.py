from langchain.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import ToolMessage


import ast

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='readonly-agent',
    password='bird',
    database='bird_mini_dev'
)

cursor = conn.cursor(dictionary=True)
database = SQLDatabase.from_uri("mysql+pymysql://readonly-agent:bird@localhost:3306/bird_mini_dev", max_string_length = 3000, sample_rows_in_table_info=3)


# Get Tables
def get_tables():
    """Performs the tool call"""
    return database.get_usable_table_names()

@tool
def get_tables_tool():
    """Performs the tool call"""

    tables = get_tables()
    response = str(tables)
    result = ToolMessage(content=response, tool_call_id="get_tables_node")
    return {"messages":result}


# Get Schemas
def get_table_schemas_and_samples(tables:list[str]):
    return database.get_table_info_no_throw(tables)

# Tools
@tool
def get_table_schemas_tool(table_list: list[str]) -> str:
    """Get detailed information about a list of tables including columns, types, constraints, and the top 3 rows.
    
    Args:
        table_names: List of table name strings

    Returns:
        Formatted string containing schema and sample data for each table
    """

    return get_table_schemas_and_samples(table_list)

def get_distinct_values(table, column):
    try:
        response = database.run(f'SELECT DISTINCT {column} FROM {table}')
        list_data = ast.literal_eval(response)
        # If you want just the values without the tuples:
        flat_list = [item[0] for item in list_data]
        if len(flat_list) > 25:
            return str(flat_list[:26])
        return str(flat_list)
    except Exception as e:
        return str(e)



@tool
def get_distinct_values_tool(table, column):
    """Get detailed information about a list of tables including columns, types, constraints, and the top 3 rows.
    
    Args:
        table_names: List of table name strings

    Returns:
        Formatted string containing schema and sample data for each table
    """
    return get_distinct_values(table, column)


def search_columns_for_value(table, columns, value):
    """Search one or more columns in a table for a specific value.
    
    Args:
        table: The table name strings
        columns: A list of column name strings
        value: the value to search for string

    Returns:
        Formatted string containing schema and sample data for each table
    """
    query = f"SELECT *, ({columns[0]} = {value}) AS {columns[0]}_match"

    for i, column in enumerate(columns[1:]):
        query += f", ({column} = '{value}') AS {column}_match"

    query += f" FROM {table} WHERE {columns[0]} = '{value}'"
    
    for column in columns[1:]:
        query += f"OR {column} = '{value}'"

    query += " LIMIT 3;"

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

@tool 
def search_columns_for_value_tool(table, columns, value):
    """Search one or more columns in a table for a specific value.
    
    Args:
        table: The table name strings
        columns: A list of column name strings
        value: the value to search for string

    Returns:
        Formatted string containing schema and sample data for each table
    """
    return search_columns_for_value(table, columns, value)

