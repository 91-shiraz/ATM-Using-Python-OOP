# 🏧 ATM System (Python)

A simple **ATM simulation in Python** that allows users to securely check their balance, withdraw cash, deposit funds, and change their PIN. It includes a basic authentication system with a **3-attempt limit** for security.

## ✨ Features

* ✅ **Check Balance** – View your current account balance after PIN authentication
* ✅ **Withdraw Funds** – Withdraw a valid amount without exceeding balance
* ✅ **Deposit Funds** – Deposit any valid amount into the account
* ✅ **Change PIN** – Update your ATM PIN securely
* ✅ **Security Limit** – 3 incorrect PIN attempts will lock the session
* ✅ **Interactive Console Menu** – User-friendly text-based interface

## 📂 Project Structure

```
ATM-System/
│── index.py          # Main ATM class implementation
│── README.md       # Project documentation
```

## 🚀 How to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/91-shiraz/ATM-Using-Python-OOP.git
   cd atm-system
   ```

2. **Run the Script**

   ```bash
   python3 index.py
   ```

3. **Follow the On-Screen Menu**

   * Select an option (1-5)
   * Enter your PIN when prompted (default: `1234`)

## 🛠️ Requirements

* Python **3.x**

No additional dependencies required.

## 🖥️ Example Output

```
=================================            
Hello, Welcome to the ATM System
=================================
                               
Please Select an Option:
1. Check Balance
2. Withdraw
3. Deposit
4. Change Pin
5. Exit
=================================
Choose an Option:  
```

## 📌 Future Improvements

* Add multiple user accounts
* Save user data in a database or JSON file
* Add transaction history feature
* Implement a GUI version
