# 🎣 Phishing Email Analyzer

A Python tool that analyzes emails and detects phishing attempts with a risk score.

## 🔍 What it detects
- Urgent language (act now, limited time, verify)
- Suspicious links (bit.ly, tinyurl)
- Fake domains (paypal-secure, gmail-support)
- Sensitive info requests (OTP, PIN, bank account)

## 🛠️ Tools Used
- Python 3
- Regex (re module)

## ▶️ How to Run
```bash
python phishing_analyzer.py
```

## 📊 Sample Output
```
⚠️  Urgent language detected: 'urgent'
⚠️  Suspicious link found: http://bit.ly/paypal-verify
⚠️  Fake domain detected: 'gmail-support'
❌  VERDICT: HIGH PHISHING RISK — Score: 23/10
```

## 💡 Skills Demonstrated
- Email threat analysis
- Pattern matching with Python
- Cybersecurity awareness
