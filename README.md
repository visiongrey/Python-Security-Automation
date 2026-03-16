# 🔐 Python Security Automation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Security](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Automation](https://img.shields.io/badge/Focus-Automation-green)

A collection of **Python automation scripts** that simulate common tasks in **security testing and log analysis environments**.

This project demonstrates practical skills useful for **security engineering, test automation, and DevSecOps**, including:

- Firewall log parsing
- IP/CIDR rule matching
- REST API interaction
- Concurrent script execution
- File processing and JSON handling

The scripts are orchestrated using a **main automation runner (`main.py`)** that executes multiple security tasks in parallel.

---

# 📂 Project Structure

```
Python-Security-Automation/
│
├── main.py                # Runs all scripts concurrently
├── parse_fwlogs.py        # Parses firewall logs and detects suspicious IPs
├── match_fwrules.py       # Matches IPs against firewall rules
├── api_requests.py        # Demonstrates REST API GET/POST automation
│
├── firewall_logs.txt      # Sample firewall log file
├── ip_list.txt            # Input list of IPs
├── fw_rules.txt           # Firewall rule set
│
└── README.md
```

---

# ⚙️ Automation Workflow

`main.py` triggers all scripts concurrently using **ThreadPoolExecutor**.

```
             +----------------+
             |    main.py     |
             +--------+-------+
                      |
          ---------------------------
          |            |            |
   parse_fwlogs   match_fwrules   api_requests
   (log analysis) (rule matching) (API testing)
```

Each script performs a **different security automation task**.

---

# 🧠 Script Descriptions

## 1️⃣ Firewall Log Parser (`parse_fwlogs.py`)

This script parses firewall logs and identifies IP addresses that have been **denied more than 5 times**.

### Key Concepts Demonstrated

- Regex-based log parsing
- Dictionary-based counting
- Security event analysis
- File processing

### Example Log Entry

```
DENY src=192.168.1.10 dst=10.1.1.5
```

### Output Example

```
The IPs having DENY more than 5 is: ['192.168.1.10']
```

---

## 2️⃣ Firewall Rule Matcher (`match_fwrules.py`)

Matches IP addresses from `ip_list.txt` against firewall rules defined in `fw_rules.txt`.

Supports:

- **Single IP rules**
- **CIDR network rules**

### Key Concepts Demonstrated

- Python `ipaddress` module
- Regex parsing
- CIDR matching
- Network rule processing
- Firewall rule evaluation

### Example Rule

```
ALLOW 192.168.1.0/24
DENY 10.0.0.5
```

### Example Output

```
192.168.1.10 : ALLOW
10.0.0.5 : DENY
```

---

## 3️⃣ API Automation (`api_requests.py`)

Demonstrates interaction with a **REST API** using Python.

### Implemented Features

- GET requests
- POST requests
- Retry logic
- JSON parsing
- File storage of API responses

### API Used

```
https://api.restful-api.dev/objects
```

### Key Concepts Demonstrated

- `requests` library
- JSON serialization/deserialization
- HTTP headers
- Retry mechanisms
- API response handling

---

# 🚀 Running the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Python-Security-Automation.git
cd Python-Security-Automation
```

## 2️⃣ Install Required Dependencies

```bash
pip install requests
```

*(The `ipaddress` module should be included in Python 3 by default.)*

## 3️⃣ Run the Automation Script

```bash
python3 main.py
```

This will execute all scripts concurrently.

Example output:

```
#############
PASS: parse_fwlogs.py
#############

#############
PASS: match_fwrules.py
#############

#############
PASS: api_requests.py
#############
```

---

# 🛠 Skills Demonstrated

This project showcases several **security engineering and automation skills**:

- Python scripting
- Security log parsing
- Firewall rule processing
- Network programming concepts
- REST API interaction
- Concurrent task execution
- Error handling
- File and JSON processing

---

# 🎯 Use Cases

This type of automation can be used in:

- Security Operations (SOC) tooling
- Firewall log monitoring
- Automated rule validation
- Security test automation
- DevSecOps pipelines
- API security testing

---

# 🔮 Possible Improvements

Future enhancements could include:

- Parallel log parsing for large files
- CIDR matching optimization
- Support for IPv6
- Integration with SIEM tools
- Unit tests with `pytest`
- Logging with Python `logging` module
- Docker containerization

---

