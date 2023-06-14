import requests
url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=&json"
url1 = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=PLN&date=&json"
r = requests.get(url)
r1 = requests.get(url1)
print(r.json()[0]["rate"])
print(r1.json()[0]["rate"])