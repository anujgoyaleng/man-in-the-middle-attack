#!/usr/bin/env python3
import requests
import time

SERVER_URL = "http://172.25.0.10"

def login(username, password):
    print(f"\n[+] Login as {username}...")
    response = requests.post(f"{SERVER_URL}/login", json={"username": username, "password": password})
    
    if response.status_code == 200:
        data = response.json()
        print(f"[✓] Success! Balance: ${data['balance']}")
        return response.cookies
    else:
        print(f"[✗] Failed")
        return None

def transfer_money(cookies, amount, to_account):
    print(f"\n[+] Transfer ${amount}...")
    response = requests.post(f"{SERVER_URL}/transfer", json={"amount": amount, "to_account": to_account}, cookies=cookies)
    
    if response.status_code == 200:
        print(f"[✓] Done! New balance: ${response.json()['new_balance']}")

def main():
    print("="*50)
    print("  Bank Client Demo")
    print("="*50)
    
    cookies = login("alice", "alice123")
    if cookies:
        time.sleep(2)
        transfer_money(cookies, 100, "9999-8888")
    
    time.sleep(3)
    
    cookies = login("bob", "bob456")
    if cookies:
        time.sleep(2)
        transfer_money(cookies, 50, "7777-6666")

if __name__ == "__main__":
    main()
