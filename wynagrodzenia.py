import sys
import numpy as np
import matplotlib.pyplot as plt

brutto = [] #kwoty brutto
netto = [] #kwoty netto

for arg in sys.argv[1:]:
    brutto.append(int(arg))
    tmp = int(arg) * 0.75
    result = int(tmp)
    netto.append(result)

brutto.sort()
netto.sort()

#stworzenie wykresu
figure = plt.figure(0)
figure.canvas.set_window_title('Wynagrodzenia')
plt.plot(brutto,netto)

#skalowanie osi x
xaxis_max = round(max(brutto), -3)+1000
xaxis_scale = xaxis_max/1000
plt.xticks(np.linspace(0, xaxis_max, xaxis_scale+1))

#skalowanie osi y
yaxis_max = round(max(netto), -3)+1000
yaxis_scale = yaxis_max/1000
plt.yticks(np.linspace(0, yaxis_max, yaxis_scale+1))

#etykiety wykresu
plt.title("Wynagrodzenia", fontweight='bold')
plt.xlabel("brutto", fontweight='bold')
plt.ylabel("netto", fontweight='bold')
plt.show()