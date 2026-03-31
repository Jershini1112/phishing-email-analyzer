import re

def analyze_email():
    print("=== Phishing Email Analyzer ===\n")
    print("Paste your email content below (press Enter twice when done):")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    email_text = "\n".join(lines).lower()
    score = 0
    warnings = []

    # Check for urgent words
    urgent_words = ["urgent", "immediately", "verify", "suspend", 
                   "click here", "limited time", "act now", "winner"]
    for word in urgent_words:
        if word in email_text:
            score += 1
            warnings.append(f"⚠️  Urgent language detected: '{word}'")

    # Check for suspicious links
    links = re.findall(r'http[s]?://\S+', email_text)
    for link in links:
        if any(x in link for x in ["bit.ly", "tinyurl", "goo.gl", "login", "verify"]):
            score += 2
            warnings.append(f"⚠️  Suspicious link found: {link}")

    # Check for fake domains
    fake_domains = ["gmail-support", "paypal-secure", "amazon-verify", 
                   "apple-id", "microsoft-alert"]
    for domain in fake_domains:
        if domain in email_text:
            score += 3
            warnings.append(f"⚠️  Fake domain detected: '{domain}'")

    # Check for money related words
    money_words = ["bank account", "credit card", "password", 
                  "ssn", "social security", "otp", "pin number"]
    for word in money_words:
        if word in email_text:
            score += 2
            warnings.append(f"⚠️  Sensitive info requested: '{word}'")

    # Show results
    print("\n=== ANALYSIS RESULTS ===\n")
    if warnings:
        for w in warnings:
            print(w)
    else:
        print("✅ No suspicious patterns found")

    print(f"\nRisk Score: {score}/10")
    if score >= 6:
        print("❌ VERDICT: HIGH PHISHING RISK")
    elif score >= 3:
        print("⚠️  VERDICT: MEDIUM PHISHING RISK")
    else:
        print("✅ VERDICT: LOW RISK")

analyze_email()