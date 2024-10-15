import numpy as np
import matplotlib.pyplot as plt
time_series = np.array([15,23,27,18,13,11,18,29,31,28,23,18,25,27,31,28,25,20,30,34,38,32,26,21,28,31,33,27,
23,17,28,32,38,32,26,23,26,32,42,38,27,24,29,37,41,38,35,25,39,44,49,47,36,31,38,42,47,35,32,23,30,
37,39,32,26,21,31,42,44,34,27,19,23,27,32,29,23,18,21,25,28,25,21,15,13,26,31,28,25,23,25,28,35,31,27,
23,32,35,37,27,21,12,17,29,31,26,24,17])
q = int(input("Enter value of q: "))
n = len(time_series)
Tline = np.zeros(n)
if len(time_series) % 2 == 1:
    for i in range(q, n - q):
        Tline[i] = np.mean(time_series[i - q:i + q + 1])
else:
    d = 2 * q
    for i in range(q, n - q):
        Tline[i] = (0.5 * time_series[i - q] + np.sum(time_series[i - q + 1:i + q]) + 0.5 * time_series[i + q]) / d
seasonal_effect = np.zeros(n)
for i in range(n):
    sum_diff = 0
    count = 0
    for j in range(-(n // q), n // q):
        if 0 <= i + j * q < n:
            sum_diff += time_series[i + j * q] - Tline[i + j * q]
            count += 1
    if count > 0:
        seasonal_effect[i] = sum_diff / count
avg_seasonality = np.mean(seasonal_effect)
adjusted_seasonal = seasonal_effect - avg_seasonality
print("Calculated Trend:", Tline)
print("Extracted Seasonality:", adjusted_seasonal)
plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(time_series, label="Original Data")
plt.legend(loc='upper left')
plt.subplot(312)
plt.plot(Tline, label="Trend", color='orange')
plt.legend(loc='upper left')
plt.subplot(313)
plt.plot(adjusted_seasonal, label="Seasonality", color='green')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()