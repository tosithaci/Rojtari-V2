FROM python:3.9-slim

# Instalo paketat e nevojshme për ping dhe libraritë e Python
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
RUN pip install requests prometheus-client

WORKDIR /app
COPY main.py .

# Krijo direktorinë për JSON nëse nuk ekziston
RUN mkdir -p /app/shared_data

CMD ["python", "main.py"]