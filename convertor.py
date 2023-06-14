from PyQt5.QtWidgets import *
import requests
app = QApplication([])
window = QWidget()
valInput = QLineEdit()
valInput.setPlaceholderText("Введіть валюту")

perevestuBtn = QPushButton("Перевести")
date = QLineEdit()
date.setPlaceholderText("Введіть дату")
valut = QLineEdit()
valut.setPlaceholderText("Введіть іншу валюту")
suma = QLineEdit()
suma.setPlaceholderText("Введіть кількість")
suma1 = QLineEdit()
suma1.setReadOnly(True)
linia = QVBoxLayout()
linia.addWidget(valInput)
linia.addWidget(date)
linia.addWidget(suma)
linia.addWidget(valut)
linia.addWidget(perevestuBtn)
linia.addWidget(suma1)



def result():
    val = valInput.text()
    dat = date.text()
    val1 =valut.text()
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={dat}&json"
    url1 = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val1}&date={dat}&json"
    r = requests.get(url)
    r1 = requests.get(url1)
    if r.status_code == 200:
        data = r.json()
        data1 = r1.json()
        res = int(suma.text()) * data[0]["rate"] / data1[0]["rate"]
        suma1.setText(str(res))

perevestuBtn.clicked.connect(result)
window.setLayout(linia)
window.show()
app.exec()