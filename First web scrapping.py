from bs4 import BeautifulSoup
import urllib.request, re
from prettytable import PrettyTable

with urllib.request.urlopen("https://cbr.ru/") as html:
    curencies = html.read()

    soup = BeautifulSoup(curencies, 'lxml')

    dates = soup.find_all('div', class_='col-md-2 col-xs-7 _right')
    current_dates = []
    for date in dates:
        current_dates.append(date.get_text())

    dollars = soup.find_all('div', class_='col-md-2 col-xs-9 _right mono-num')
    values = []
    for dollar in dollars:
        s = dollar.get_text()
        s = re.sub('\s+', '', s)
        values.append(s)

    valuesTable = PrettyTable()
    valuesTable.field_names = ["Курсы валют", current_dates[0], current_dates[1]]
    valuesTable.add_row(['CNY', values[0], values[1]])
    valuesTable.add_row(['USD', values[2], values[3]])
    valuesTable.add_row(['EUR', values[4], values[5]])

    print(valuesTable)
