print("Cybersecurity Log Analyzer")
print("----------------------------")

log_file = open("server.log", "r")

failed_attempts = {}

for line in log_file:
    if "LOGIN_FAILED" in line:
        parts = line.split("ip=")
        ip = parts[1].strip()

        if ip in failed_attempts:
            failed_attempts[ip] = failed_attempts[ip] + 1
        else:
            failed_attempts[ip] = 1

log_file.close()

print("\nSuspicious IP addresses:")

for ip in failed_attempts:
    if failed_attempts[ip] >= 5:
        print(ip, "→", failed_attempts[ip], "failed logins")
