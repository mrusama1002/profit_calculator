import streamlit as st
import pandas as pd

# 🔹 Page Config
st.set_page_config(page_title="UrbanRitz Profit Dashboard", layout="wide")

# 🔹 Top Branding (Logo + Title)
col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.png", width=120)  # 👈 apna logo yahan load hoga

with col2:
    st.markdown(
        """
        <h1 style='color:#4CAF50;'>UrbanRitz Profit Dashboard</h1>
        <p>Smart Decisions • Better Margins • Scalable Growth</p>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# 🔹 Sidebar Inputs
with st.sidebar:
    st.header("📥 Input Parameters")

    product_cost = st.number_input("Product Cost", value=1350)
    shipping_cost = st.number_input("Shipping Cost", value=350)
    packaging_cost = st.number_input("Packaging Cost", value=60)
    daily_ad_spend = st.number_input("Daily Ad Spend", value=3300)
    selling_price = st.number_input("Selling Price", value=3299)
    
    orders_per_day = st.slider("Orders per Day", 1, 20, 5)
    cod_return_rate = st.slider("COD Return %", 0, 50, 20)

# 🔹 Calculations
base_cost = product_cost + shipping_cost + packaging_cost
ad_per_order = daily_ad_spend / orders_per_day
total_cost = base_cost + ad_per_order

effective_orders = orders_per_day * (1 - cod_return_rate / 100)
profit_per_order = selling_price - total_cost
daily_profit = profit_per_order * effective_orders

break_even_cpa = selling_price - base_cost

# 🔹 Metrics
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Base Cost", f"{base_cost:.0f} Rs")
col2.metric("Ad / Order", f"{ad_per_order:.0f} Rs")
col3.metric("Profit / Order", f"{profit_per_order:.0f} Rs")
col4.metric("Daily Profit", f"{daily_profit:.0f} Rs")

# 🔹 Status
if profit_per_order > 700:
    st.success("🔥 Strong Profit Model")
elif profit_per_order > 300:
    st.warning("⚠️ Optimize Ads / Pricing")
else:
    st.error("❌ Risky Model")

# 🔹 Chart
st.markdown("### 📈 Profit vs Orders")

orders_range = list(range(1, 21))
profits = []

for o in orders_range:
    ad_cost = daily_ad_spend / o
    total = base_cost + ad_cost
    profit = (selling_price - total) * (o * (1 - cod_return_rate / 100))
    profits.append(profit)

df = pd.DataFrame({
    "Orders": orders_range,
    "Profit": profits
})

st.line_chart(df.set_index("Orders"))

# 🔹 Footer Branding (Website + Contact)
st.markdown(
    """
    <hr>
    <p style='text-align:center; font-size:14px;'>
        🌐 <a href="https://urbanritz.com" target="_blank">urbanritz.com</a> |
        📞 03322208090
    </p>
    <p style='text-align:center; color:gray; font-size:13px;'>
        © UrbanRitz — Scaling E-commerce Brands 🚀
    </p>
    """,
    unsafe_allow_html=True
)