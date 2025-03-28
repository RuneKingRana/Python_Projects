import matplotlib.pyplot as plt
import numpy as np

# Data for India's population distribution
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]  # Population in millions
percentages = [3.61, 5.70, 6.9]  # Corresponding percentages
colors = ['yellow', 'blue', 'pink']  # Colors for the areas

# Simulated X-axis range for ages (representing 0 to 100 years)
x = np.linspace(0, 100, 300)  # Smooth age distribution

# Simulated stacked population distribution
y1 = np.piecewise(x, [x <= 20, (x > 20) & (x <= 64), x > 64],
                  [lambda x: population[0], 0, 0])
y2 = np.piecewise(x, [x <= 20, (x > 20) & (x <= 64), x > 64],
                  [0, lambda x: population[1], 0])
y3 = np.piecewise(x, [x <= 20, (x > 20) & (x <= 64), x > 64],
                  [0, 0, lambda x: population[2]])

# Stacked area chart
plt.figure(figsize=(10, 7))
plt.fill_between(x, y1, color=colors[0], label=f"{age_groups[0]} ({percentages[0]}%)")
plt.fill_between(x, y1 + y2, y1, color=colors[1], label=f"{age_groups[1]} ({percentages[1]}%)")
plt.fill_between(x, y1 + y2 + y3, y1 + y2, color=colors[2], label=f"{age_groups[2]} ({percentages[2]}%)")

# Add median age and labels
plt.axvline(x=28, color='black', linestyle='--', label='Median Age = 28')
plt.text(28.5, max(population) / 2, "Median Age = 28", fontsize=10, color='black')

# Add chart details
plt.title("India's Population Distribution by Age in 2023", fontsize=16)
plt.xlabel("Age (in Years)", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, max(population)+100, 100))
plt.legend(loc='upper right', fontsize=10)
plt.grid(alpha=0.5, linestyle='--')

# Add source information
plt.text(-5, -100, "Source: Simulated data based on World Population Prospects (2022)", fontsize=10, color='gray')

# Show plot
plt.tight_layout()
plt.show()
