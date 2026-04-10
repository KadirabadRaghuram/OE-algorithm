import streamlit as st
import numpy as np
import time

st.title("🧬 Genetic Algorithm - Knapsack")

# Sidebar
st.sidebar.title("⚙️ Controls")
pop_size = st.sidebar.slider("Population Size", 10, 100, 30)
generations = st.sidebar.slider("Generations", 10, 200, 100)
capacity = st.sidebar.slider("Capacity", 5, 15, 10)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Population", pop_size)
col2.metric("Generations", generations)
col3.metric("Capacity", capacity)

weights = np.array([2,3,4,5])
values = np.array([3,4,5,6])

def fitness(sol):
    w = np.sum(sol * weights)
    v = np.sum(sol * values)
    return v if w <= capacity else 0

# Initialize
population = np.random.randint(0, 2, (pop_size, len(weights)))
best_scores = []

# Chart placeholder
chart = st.line_chart([])

progress = st.progress(0)

# GA loop
for gen in range(generations):
    scores = np.array([fitness(ind) for ind in population])
    
    best_scores.append(np.max(scores))
    chart.add_rows([best_scores[-1]])  # 📈 update graph

    parents = population[np.argsort(scores)[-2:]]

    children = []
    for _ in range(pop_size):
        p1, p2 = parents
        cross = np.random.randint(1, len(weights))
        child = np.concatenate([p1[:cross], p2[cross:]])

        # Mutation
        if np.random.rand() < 0.1:
            idx = np.random.randint(len(weights))
            child[idx] = 1 - child[idx]

        children.append(child)

    population = np.array(children)

    progress.progress((gen+1)/generations)
    time.sleep(0.02)

# Final result
best = max(population, key=fitness)

st.success(f"Best Solution: {best}")
st.metric("Max Value", fitness(best))