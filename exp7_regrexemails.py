import re

text = """
You can contact us at abc@gmail.com or support@example.com.
For more information, email test123@yahoo.com.
"""

# Regular expression for email pattern
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)