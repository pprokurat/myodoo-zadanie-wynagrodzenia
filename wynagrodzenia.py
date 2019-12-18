import sys
import numpy as np
import matplotlib.pyplot as plt
import mechanize
from bs4 import BeautifulSoup

brutto = [] #kwoty brutto
netto = [] #kwoty netto


def get_net_salary(gross):
    br = mechanize.Browser()

    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]

    br.open('https://wynagrodzenia.pl/kalkulator-wynagrodzen')

    br.select_form('sedlak_calculator')
    br.form['sedlak_calculator[contractType]'] = ['work', ]
    br.form['sedlak_calculator[calculateWay]'] = ['gross', ]
    br.form['sedlak_calculator[earnings]'] = gross
    br.form['sedlak_calculator[year]'] = ['2019', ]
    br.form['sedlak_calculator[mandateModels]'] = ['otherCompany', ]
    br.form['sedlak_calculator[theSameCity]'] = ['1', ]
    br.form['sedlak_calculator[freeCost]'] = ['1', ]
    br.form['sedlak_calculator[constantEarnings]'] = ['1', ]
    br.form['work_end26Year'] = ['on', ]

    for i in range(0, 12):
        element = 'sedlak_calculator[monthlyEarnings][' + str(i) + ']'
        br.form[element] = gross

    br.form['sedlak_calculator[selfEmployer]'] = ['1', ]
    br.form['sedlak_calculator[rentAndAnnuityCost]'] = ['1', ]
    br.form['sedlak_calculator[sicknesCost]'] = ['1', ]
    br.form['sedlak_calculator[healthCost]'] = ['1', ]
    br.form['sedlak_calculator[FPCost]'] = ['1', ]
    br.form['sedlak_calculator[FGSPCost]'] = ['1', ]
    br.form['mandate_end26Year'] = ['on', ]
    br.form['sedlak_calculator[accidentPercent]'] = '1.67'
    br.form['sedlak_calculator[end26Year]'] = ['1', ]
    br.form['sedlak_calculator[employeePercent]'] = '2'
    br.form['sedlak_calculator[employerPercent]'] = '1.5'
    br.form['sedlak_calculator[octoberIncome]'] = ['1', ]
    br.form['sedlak_calculator[businessExpenses]'] = ['0', ]
    br.form['work_accidentPercent'] = '1.67'
    br.form['nonwork_accidentPercent'] = '1.67'

    resp2 = br.submit()

    html = resp2.read().decode('utf-8')
    soup = BeautifulSoup(html, features="html5lib")
    netsum_tmp = soup.find_all('span', {'class': 'bold'})[1].text

    netsum_tmp = netsum_tmp.split(' ')[0] + netsum_tmp.split(' ')[1]
    result = netsum_tmp.replace(',', '.')

    return result


def check_net_salaries():
    for arg in sys.argv[1:]:
        brutto.append(float(arg))
        netto_tmp = get_net_salary(arg)
        netto.append(float(netto_tmp))

    brutto.sort()
    netto.sort()


def display_plot():
    # stworzenie wykresu
    figure = plt.figure(0)
    figure.canvas.set_window_title('Wynagrodzenia')
    plt.plot(brutto, netto)

    # skalowanie osi x
    xaxis_max = round(max(brutto), -3) + 1000
    xaxis_scale = xaxis_max / 1000
    plt.xticks(np.linspace(0, xaxis_max, xaxis_scale + 1))

    # skalowanie osi y
    yaxis_max = round(max(netto), -3) + 1000
    yaxis_scale = yaxis_max / 1000
    plt.yticks(np.linspace(0, yaxis_max, yaxis_scale + 1))

    # etykiety wykresu
    plt.title("Wynagrodzenia", fontweight='bold')
    plt.xlabel("brutto", fontweight='bold')
    plt.ylabel("netto", fontweight='bold')
    plt.show()


check_net_salaries()
display_plot()