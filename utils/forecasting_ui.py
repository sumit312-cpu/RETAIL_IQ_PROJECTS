import streamlit as st
import pandas as pd


def forecasting_page(xgb_model):

    st.header("📈 Sales Forecasting")

    col1, col2 = st.columns(2)

    with col1:

        store = st.number_input(
            "Store ID",
            min_value=1,
            max_value=1115,
            value=1
        )

        day_of_week = st.selectbox(
            "Day Of Week",
            [1,2,3,4,5,6,7]
        )

        open_store = st.selectbox(
            "Store Open",
            [0,1]
        )

        promo = st.selectbox(
            "Promotion Running",
            [0,1]
        )

        school_holiday = st.selectbox(
            "School Holiday",
            [0,1]
        )

        store_type_raw = st.selectbox(
            "Store Type",
            ["a","b","c","d"]
        )

        store_type = {
            "a":0,
            "b":1,
            "c":2,
            "d":3
        }[store_type_raw]

        assortment_raw = st.selectbox(
            "Assortment",
            ["a","b","c"]
        )

        assortment = {
            "a":0,
            "b":1,
            "c":2
        }[assortment_raw]

    with col2:

        competition_distance = st.number_input(
            "Competition Distance",
            value=1000.0
        )

        competition_open_month = st.number_input(
            "Competition Open Month",
            min_value=1,
            max_value=12,
            value=1
        )

        competition_open_year = st.number_input(
            "Competition Open Year",
            min_value=1990,
            max_value=2030,
            value=2010
        )

        promo2 = st.selectbox(
            "Promo2",
            [0,1]
        )

        promo2_week = st.number_input(
            "Promo2 Since Week",
            min_value=0,
            max_value=52,
            value=0
        )

        promo2_year = st.number_input(
            "Promo2 Since Year",
            min_value=0,
            max_value=2030,
            value=0
        )

        promo_interval_raw = st.selectbox(
            "Promo Interval",
            [
                "Feb,May,Aug,Nov",
                "Jan,Apr,Jul,Oct",
                "Mar,Jun,Sept,Dec",
                "nan"
            ]
        )

        promo_interval = {
            "Feb,May,Aug,Nov":0,
            "Jan,Apr,Jul,Oct":1,
            "Mar,Jun,Sept,Dec":2,
            "nan":3
        }[promo_interval_raw]

    st.subheader("📅 Date Information")

    selected_date = st.date_input(
        "Select Date"
    )

    year = selected_date.year
    month = selected_date.month
    day = selected_date.day
    week = selected_date.isocalendar().week
    quarter = ((month-1)//3)+1
    weekend = 1 if selected_date.weekday() >= 5 else 0

    holiday_flag = st.selectbox(
        "Holiday Flag",
        [0,1]
    )

    if st.button("Predict Sales"):

        df = pd.DataFrame([{

            "Store":store,
            "DayOfWeek":day_of_week,
            "Open":open_store,
            "Promo":promo,
            "SchoolHoliday":school_holiday,
            "StoreType":store_type,
            "Assortment":assortment,
            "CompetitionDistance":competition_distance,
            "CompetitionOpenSinceMonth":competition_open_month,
            "CompetitionOpenSinceYear":competition_open_year,
            "Promo2":promo2,
            "Promo2SinceWeek":promo2_week,
            "Promo2SinceYear":promo2_year,
            "PromoInterval":promo_interval,
            "Year":year,
            "Month":month,
            "Day":day,
            "Week":week,
            "Quarter":quarter,
            "Weekend":weekend,
            "Holiday_Flag":holiday_flag

        }])

        prediction = xgb_model.predict(df)[0]

        st.success(
            f"💰 Predicted Sales : ₹ {prediction:,.2f}"
        )