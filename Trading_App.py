import streamlit as st
st.markdown(
    """
[![Star](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@manvendraroy22)
[![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/DennisNiggl)

""",
    unsafe_allow_html=True,
)

st.markdown(
    """

# Trading Guide App

""",
    unsafe_allow_html=True,
)
st.markdown('---')

st.set_page_config(
    page_title='Trading Guide',
    page_icon='https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png',
    layout="wide",
)


# Inject custom font and background image
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="css"] {
            font-family: 'Nunito Sans', sans-serif;
        }
        .stApp {
            background-image: url("cool-color-background-0j9ek9305ppp3l19.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .overlay {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #1f4e79;
        }
        .feature-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# Main content with overlay
st.markdown('<div class="overlay">', unsafe_allow_html=True)



# Banner image
st.image("pexels-anna-nekrashevich-6801648.jpg", use_column_width=True)

# Intro section
st.markdown("""
Welcome to the Trading Guide App — a professional platform designed to empower investors with data-driven insights. Whether you're a beginner or a seasoned trader, our tools help you make informed decisions backed by time series forecasting and market analysis.
""")

# Features section
st.markdown("### 🔍 Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>📈 Stock Forecasting</h3>
    <p>Leverage time series models to predict future stock trends and price movements.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>📊 Technical Analysis</h3>
    <p>Visualize moving averages, RSI, MACD, and other indicators to guide your strategy.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
    <h3>🧠 Smart Insights</h3>
    <p>Get actionable recommendations based on historical patterns and predictive analytics.</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation prompt
st.markdown("---")
st.markdown("👉 Use the sidebar to explore **Stock Analysis** and **Forecasting Tools**")

# Footer
st.markdown("""
---
© 2025 Trading Guide App | Built with ❤️ using Streamlit
""")

# Close overlay
st.markdown('</div>', unsafe_allow_html=True)
