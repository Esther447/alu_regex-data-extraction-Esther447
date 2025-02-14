import re

# Improved regex patterns with better edge-case handling
patterns = {
    # Matches valid emails, including those with subdomains
    "Valid Emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?\b",

    # Matches valid URLs with optional "www" and paths
    "Valid URLs": r"https?://(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]+)+[/\w\-%=&.?]*",

    # Matches various phone number formats
    "Valid Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",

    # Matches credit card numbers in XXXX-XXXX-XXXX-XXXX or XXXX XXXX XXXX XXXX format
    "Valid Credit Card Numbers": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",

    # Matches time formats like HH:MM and HH:MM AM/PM
    "Valid Time Formats": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?: ?[APap][Mm])?\b",

    # Matches HTML tags
    "HTML Tags": r"<\s*[\w]+(?:\s+[^>]*)?>",

    # Matches hashtags
    "Hashtags": r"#\w+",

    # Matches currency amounts with or without the dollar sign
    "Valid Currency Amounts": r"\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
}

# Sample text for testing
sample_text = """
Emails:
 - user@example.com
 - firstname.lastname@company.co.uk
 - valid.email+alias@domain.org
 - user@sub.example.com
 - user@com

URLs:
 - https://www.example.com
 - https://subdomain.example.org/page
 - http://example.com

Phone Numbers:
 - (123) 456-7890
 - 123-456-7890
 - 123.456.7890

Credit Card Numbers:
 - 1234 5678 9012 3456
 - 1234-5678-9012-3456

Time Formats:
 - 14:30
 - 2:30 PM
 - 23:59

HTML Tags:
 - <p>
 - <div class="example">
 - <img src="image.jpg" alt="description">

Hashtags:
 - #example
 - #ThisIsAHashtag

Currency Amounts:
 - $19.99
 - $1,234.56
 - 19.99
"""

# Function to extract and display results
def extract_data(patterns, text):
    print("\n📌 Extracted Data:\n" + "-" * 40)
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        print(f"\n🔹 {label}:")
        if matches:
            for match in matches:
                print(f"   ✅ {match}")
        else:
            print("   ❌ No valid matches found.")

# Run the extraction
if __name__ == "__main__":
    extract_data(patterns, sample_text)
