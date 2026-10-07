# ai_sast_test.py
# Test file for AI-SAST vulnerability detection

import os
import sqlite3
import subprocess
import hashlib
import pickle
import requests


# 1. SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    return cursor.fetchall()


# 2. Command Injection
def ping_host(host):
    command = "ping -c 4 " + host
    result = subprocess.check_output(command, shell=True)

    return result.decode()


# 3. Hardcoded Secret
API_KEY = "sk_test_51AI_SAST_TEST_123456789"
DATABASE_PASSWORD = "SuperSecretPassword123!"


# 4. Weak Cryptographic Hash
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# 5. Unsafe Deserialization
def load_user_data(data):
    user = pickle.loads(data)
    return user


# 6. SSRF
def fetch_url(url):
    response = requests.get(url)
    return response.text


# 7. Path Traversal
def read_file(filename):
    base_dir = "/var/app/uploads/"
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "r") as f:
        return f.read()


# 8. Code Injection
def execute_expression(expression):
    return eval(expression)


# 9. Debug Information Exposure
def authenticate(username, password):
    if username == "admin" and password == DATABASE_PASSWORD:
        print("DEBUG: Admin authentication successful")
        print("DEBUG: Password:", password)
        return True

    return False


# 10. Insecure TLS Verification
def download_data(url):
    response = requests.get(url, verify=False)
    return response.text


if __name__ == "__main__":
    print(get_user("admin"))
