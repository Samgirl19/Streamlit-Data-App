import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator

# Run with: streamlit run dashboard.py

st.title("Water Quality Dashboard")

st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

# Clean column names
df.columns = df.columns.str.strip()

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2D Plots",
     "3D Plots",
     "NASA APOD"]
)

# ------------------- TAB 1 -------------------
with tab1:
    st.info("Dataset Overview")
    st.dataframe(df)
    st.caption("Raw Data")

    st.divider()

    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")


# ------------------- TAB 2 -------------------
with tab2:
    fig1 = px.line(
        df,
        x="Time",
        y="Temperature (c)",
        color="pH"
    )
    st.plotly_chart(fig1, use_container_width=True)


# ------------------- TAB 3 -------------------
with tab3:
    fig3 = px.scatter_3d(
        df,
        x="Longitude",
        y="Latitude",
        z="Total Water Column (m)",
        color="Temperature (c)"
    )
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3, use_container_width=True)


# ------------------- TAB 4 -------------------
with tab4:
    st.warning("NASA Astronomy Picture of the Day")

    apod_data = apod_generator()

    if "error" in apod_data:
        st.error("Failed to fetch NASA APOD data.")
        st.write(apod_data["error"])
    else:
        st.subheader(apod_data.get("title", "No Title Available"))
        st.caption(apod_data.get("date", ""))

        if apod_data.get("media_type") == "image":
            image_url = apod_data.get("hdurl") or apod_data.get("url")
            st.image(image_url, use_container_width=True)

        elif apod_data.get("media_type") == "video":
            st.video(apod_data.get("url"))

        st.write(apod_data.get("explanation", "No explanation available."))