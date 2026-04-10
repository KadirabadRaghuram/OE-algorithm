import streamlit as st
import numpy as np
import time

st.title("🔥 Simulated Annealing")

# Sidebar
st.sidebar.title("⚙️ Controls")
x0 = st.sidebar.slider("Initial x", -10.0, 10.0, 5.0)
T = st.sidebar.slider("Temperature", 1.0, 100.0, 20.0)
alpha = st.sidebar.slider("Cooling Rate", 0.8, 0.99, 0.95)
iterations = st.sidebar.slider("Iterations", 20, 200, 100)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Iterations", iterations)
col2.metric("Cooling", alpha)
col3.metric("Method", "Annealing")

def f(x):
    return x**2 + 10*np.sin(x)

x = x0
history = [x]

progress = st.progress(0)

for i in range(iterations):
    x_new = x + np.random.uniform(-1, 1)
    delta = f(x_new) - f(x)

    if delta < 0 or np.random.rand() < np.exp(-delta / T):
        x = x_new

    T *= alpha
    history.append(x)
    progress.progress((i+1)/iterations)

# Animated chart
chart = st.line_chart([history[0]])

for i in range(1, len(history)):
    chart.add_rows([history[i]])
    time.sleep(0.02)