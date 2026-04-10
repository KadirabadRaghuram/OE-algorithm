import streamlit as st

st.set_page_config(page_title="Optimization Dashboard", layout="wide")

# 🎨 Custom CSS
st.markdown("""
<style>
.card {
    background-color: #121826;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-10px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.6);
}
.title {
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    color: #9BA3AF;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🚀 Optimization Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Interactive visualization of algorithms</div>', unsafe_allow_html=True)

st.markdown("---")

# Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>📉 Unconstrained Minimization</h3></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>🧬 Genetic Algorithm</h3></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>📊 Pareto Front</h3></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>🔥 Simulated Annealing</h3></div>', unsafe_allow_html=True)

st.success("👉 Use sidebar to explore modules")