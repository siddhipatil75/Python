import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [30, 32, 31, 29, 28, 27, 31]

plt.figure(figsize=(8,4))
plt.plot(days, temperature, marker='o', color='blue', linestyle='--', label='Temperature (°C)')
plt.title('Weekly Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()