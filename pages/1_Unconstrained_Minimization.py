import streamlit as st
import numpy as np
import time

st.title("📉 Unconstrained Minimization")

# Sidebar
st.sidebar.title("⚙️ Controls")
x0 = st.sidebar.slider("Initial Value", -10.0, 10.0, 5.0)
lr = st.sidebar.slider("Learning Rate", 0.01, 1.0, 0.1)
iterations = st.sidebar.slider("Iterations", 10, 200, 50)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Iterations", iterations)
col2.metric("Method", "Gradient Descent")
col3.metric("Status", "Running 🚀")

# Function
def f(x):
    return x**2 + 4*np.sin(x)

def grad(x):
    return 2*x + 4*np.cos(x)

# Optimization
x = x0
history = [x]

progress = st.progress(0)

for i in range(iterations):
    x = x - lr * grad(x)
    history.append(x)
    progress.progress((i+1)/iterations)

# Animated chart
chart = st.line_chart([history[0]])

for i in range(1, len(history)):
    chart.add_rows([history[i]])
    time.sleep(0.02)