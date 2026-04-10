import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Pareto Front")

# Sidebar
st.sidebar.title("⚙️ Controls")
n = st.sidebar.slider("Number of Points", 20, 200, 100)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Points", n)
col2.metric("Type", "Multi-objective")
col3.metric("Status", "Generated")

# Data
x = np.random.rand(n)
y = 1 - x**2 + np.random.rand(n)*0.1

pareto = []
for i in range(n):
    if not any((x[j] <= x[i] and y[j] <= y[i] and (x[j] < x[i] or y[j] < y[i])) for j in range(n)):
        pareto.append((x[i], y[i]))

px, py = zip(*pareto)

# Plot
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5)
ax.scatter(px, py, s=80)
ax.set_title("Pareto Front")
ax.grid(True)

st.pyplot(fig)