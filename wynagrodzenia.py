import sys
import matplotlib.pyplot as plt

inputs = [] #kwoty brutto
results = [] #kwoty netto

for arg in sys.argv[1:]:
    inputs.append(arg)
    tmp = int(arg) * 0.75
    result = int(tmp)
    results.append(result)

figure = plt.figure(0)
figure.canvas.set_window_title('Wynagrodzenia')
plt.plot(inputs,results)
plt.title("Wynagrodzenia", fontweight='bold')
plt.xlabel("brutto", fontweight='bold')
plt.ylabel("netto", fontweight='bold')
plt.show()