# 🧪 Multi-Platform Backup Testing

This QA project demonstrates manual and automated testing of a backup application running on multiple platforms (Windows/Linux). It includes test plans, test cases, bug reports, API testing via Postman, UI automation via Selenium, and system configuration checks.

---

## 📁 Project Structure

<pre>
multi-platform-backup-testing/
├── manual-testing/
│   ├── test-plan.md
│   ├── test-cases.xlsx
│   ├── bug-reports/
│   └── bug-reports.md
├── api-testing/
│   └── postman-collections/
├── automation-testing/
│   ├── selenium-scripts/
│   └── requirements.txt
├── system-config-checks/
│   ├── linux/
│   └── windows/
└── README.md
</pre>

---

## ✅ Testing Coverage

### 🔹 Manual Testing
- [✔] Test Plan
- [✔] Test Cases (Excel format)
- [✔] Bug Reports with severity & steps to reproduce

### 🔹 API Testing
- [✔] Prepared Postman collections for key endpoints (GET, POST)
- [ ] Optional: include `.json` files in `api-testing/`

### 🔹 Automation Testing
- [✔] Selenium test support
- [✔] `requirements.txt` with dependencies

### 🔹 System Configuration
- [✔] DNS/DHCP config check on Linux and Windos
---

## 🧪 Tools Used

- 🧰 **Selenium WebDriver** – for UI automation
- 📮 **Postman** – for API validation
- 📊 **Excel** – for test case management
- 💻 **Bash + OS tools** – for system checks
- 🐧 **Ubuntu**, 🪟 **Windows 10**

---

## 🚀 How to Run

### UI Tests:
```bash
cd automation-testing/
pip install -r requirements.txt
python <your_test_file>.py

