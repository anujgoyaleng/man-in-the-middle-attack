FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    iptables \
    net-tools \
    tcpdump \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mitm_script.py .
COPY start_mitm.sh .
RUN chmod +x start_mitm.sh

EXPOSE 8888

CMD ["/bin/bash"]
