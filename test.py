import os 
import json

def divide_by_zero():
    return 1 / 0  

def sql_injection():
    user_input = request.args.get("username")
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)  


def test_func():
    var=True

