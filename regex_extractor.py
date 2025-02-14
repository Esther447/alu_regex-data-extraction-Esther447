import re

text = """
Contact me at e.mushimiyi@alustudent.com or visit https://github.com/Esther447 My number is (250) 793316246 and my credit card is 1234 567 8909 8765 I will be there at 2:30 PM, and here is an HTML tag: <div class="example"> #ThisIsAHashtag and the price is $19.99.


email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_regex, text)

url_regex = r'https?://[a-zA-Z0-9.-]++\.[a-zA-Z]{2,6}(/[\w.-]*)*'
urls = re.findall(phone_regex, text)

phone_regex = r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})'
phones = re.findall(phone_regex, text)

credit_card_regex = r'(\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4})'
credit_cards = re.findall(credit_card_regex, text)

time_regex = r'(\d{1,2}:\d{2} (AM|PM)?)|(\d{2}:\d{2})'
times = re.findall(html_tag_regex, text)

hashtag_regex = r'#\w+'
hashtags = re.findall(hashtag_regex, text)

currency_regex = r'\$\d{2,3}(?:,\d{3}*(?:\.\d{2})?'
currencies = re.findall(currency_regex, text)

print("Emails:", emails)
print("URLs:", urls)
print("Phones:", phones)
print("Credit Cards:", credit_cards)
print("Times:", times)
print("HTML Tags:", html_tags)
print("Hashtags:", hashtags)
print("Currencies:", currencies)
