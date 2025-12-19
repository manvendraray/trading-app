import streamlit as st

# Page config 
st.set_page_config(
    page_title="Time-Series Forecasting",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Social badges
st.markdown(
    """
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@manvendraroy22)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/manvendraray)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/manvendraray)
""",
    unsafe_allow_html=True,
)

# Title
st.markdown("# Time-Series Forecasting")
st.markdown(
    """
**An end-to-end Time-Series Forecasting and technical analysis dashboard built with Python.**
"""
)
st.markdown("---")
col1, col2 = st.columns([1, 2])

with col1:
    st.image("Flowchart.png", use_container_width=True)

# Intro (aligned with pipeline)
with col2:
    st.markdown(
    """
This application explores **historical stock price behavior** using classical
time-series techniques and presents the results through **interactive visualizations**.

The focus is on understanding **how prices evolve over time**, validating statistical
assumptions, and producing **interpretable short-term forecasts** rather than
black-box predictions.
"""
)
    # Pipeline explanation
    st.markdown("## Forecasting Pipeline")
    col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-box">
          <h3> Stock Forecasting</h3>
          <p>
          Explore how stock prices may move in the near future
          using historical data and time-series models.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-box">
          <h3> Technical Analysis</h3>
          <p>
          View indicators like Moving Averages, RSI, and MACD
          to better understand trends and momentum.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-box">
          <h3> Clear Evaluation</h3>
          <p>
          See how well the model performs using easy-to-understand
          error measures instead of black-box scores.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Navigation hint
st.markdown("---")
st.markdown(
    """
### Explore the App
Use the sidebar to navigate between **Stock Analysis** and **Stock Prediction**
to interact with the models and visualizations.
"""
)
col1, col2= st.columns(2)
with col1:
    with st.expander("⚠️ Model Assumptions & Limitations"):
        st.markdown(
        """
        - Forecasts are based solely on historical price patterns  
        - No fundamental, macro, or news data is used  
        - ARIMA assumes stable statistical behavior over time  
        - Results are best interpreted as a **baseline**, not trading advice  
        """
    )
    
with col2:
    with st.expander("🧭 How to Use"):
        st.markdown(
        """
        1. Choose a stock from the list or enter a ticker  
        2. Explore historical price behavior  
        3. Run the forecast to view short-term projections  
        4. Inspect model error and indicators  
        """
    )
    



# Disclaimer
st.markdown(
    """
---
⚠️ **Disclaimer:**  
This project is for educational and analytical purposes only and does not constitute
financial or investment advice.
"""
)

# Footer
st.markdown(
    """
---
© 2025 Time-Series Forecasting · Built with Streamlit, Plotly, Statsmodels & Yahoo Finance
"""
)
