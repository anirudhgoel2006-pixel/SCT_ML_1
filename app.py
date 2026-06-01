import streamlit as st

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 House Price Predictor")

st.write(
    "Predict the value of your property using a Linear Regression model."
)

sqft = st.number_input(
    "Square Footage (sqft)",
    min_value=100,
    max_value=10000,
    value=1500
)

bedrooms = st.slider(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.slider(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

if st.button("Calculate Estimated Price"):
    estimated_price = (sqft * 200) + (bedrooms * 50000) + (bathrooms * 30000)

    st.success(
        f"Estimated House Price: ₹ {estimated_price:,.0f}"
    )
