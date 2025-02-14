import re

# Define patterns for each type of data
patterns = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://[^\s]+",
    "Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "Credit Card Numbers": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "Time (24h & 12h)": r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b\d{1,2}:\d{2}\s?[APap][Mm]\b",
    "HTML Tags": r"<[^>]+>",
    "Hashtags": r"#\w+",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*\.\d{2}"
}

def extract_data(input_text):
    extracted_data = {}
    for category, pattern in patterns.items():
        matches = re.findall(pattern, input_text)
        extracted_data[category] = matches
    return extracted_data

# Example input string
input_text = """
Email addresses: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Card Numbers: 1234 5678 9012 3456, 1234-5678-9012-3456
Time: 14:30, 2:30 PM
HTML Tags: <p>, <div class="example">, <img src="image.jpg" alt="description">
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56
"""

# Extract data from input
extracted_data = extract_data(input_text)

# Display extracted data
for category, matches in extracted_data.items():
    if matches:
        print(f"\n{category}:")
        for match in matches:
            print(f" - {match}")
    else:
        print(f"\n{category}: No matches found")
