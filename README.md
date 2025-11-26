# Man-in-the-Middle (MITM) Attack Lab

Learn how attackers can intercept unencrypted HTTP traffic and steal passwords.

## What You'll Learn

- How MITM attacks work
- Why HTTPS is important
- How to intercept HTTP traffic
- Network security basics

## Setup (5 minutes)

1. Install Docker Desktop from https://www.docker.com/products/docker-desktop

2. Start the lab:
```bash
docker-compose up
```

3. Open http://localhost:8080 in your browser

## Demo Accounts

- Username: alice | Password: alice123
- Username: bob | Password: bob456

## How to Run the Attack

**Step 1: Start the attacker**
```bash
docker exec -it mitm-attacker bash
cd /app
./start_mitm.sh
```

**Step 2: Generate traffic**
```bash
docker exec -it vulnerable-client bash
python3 client_script.py
```

**Step 3: See captured passwords**
```bash
docker exec mitm-attacker cat /tmp/captured_credentials.txt
```

You'll see all usernames and passwords in plain text!

## Why This Works

- The website uses HTTP (not HTTPS)
- No encryption = attacker can read everything
- This is why you should always use HTTPS

## Stop the Lab

```bash
docker-compose down
```

## Warning

For education only. Never attack real systems without permission.
