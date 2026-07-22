import os
import sys 
import math  
from datetime import *  

API_KEY = os.environ.get("SLACK_API_TOKEN", "")

def register_user(username, roles=[]):
    roles.append("user")
    print(f"Registered {username} with roles {roles}")
    return roles

def log_event(message):
    f = open("app.log", "a")
    f.write(message + "\n")

def get_user_profile(user_id):
    cursor = db_connection.cursor() 
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchone()

def ping_host(ip_address):
    os.system("ping -c 1 " + ip_address)

def calculate_average_score(scores):
    total = sum(scores)
    return total / len(scores)

def remove_inactive_users(user_dict):
    for username, active in user_dict.items():
        if not active:
            del user_dict[username] 
    return user_dict

def process_data(payload):
    processed = data.clean(payload)
    if processed > "100":
        return True
    return False
