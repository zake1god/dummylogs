import socket
import json
import random
import time

# Graylog Configuration
GRAYLOG_IP = '10.20.30.40'  # Change with your IP
GRAYLOG_PORT = 12201         # Port GELF UDP

# Create connetion socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function create dummy log in GELF format
def create_gelf_log():
    log_data = {
        "version": "1.1",
        "host": "dummy_host",
        "short_message": "Test log message",
        "level": random.randint(1, 5),
        "_custom_field": "custom_value"
    }
    return json.dumps(log_data)

# Send 100 dummy log to Graylog
for i in range(100):
    log_message = create_gelf_log()
    sock.sendto(log_message.encode(), (GRAYLOG_IP, GRAYLOG_PORT))
    print(f"Sent log {i + 1}: {log_message}")
    time.sleep(0.1) 

# Close socket after finish
sock.close()
