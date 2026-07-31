import streamlit as st
import pandas as pd
import numpy as np


def recommendation_page(
    ann_model,
    user_encoder,
    product_encoder,
    product_lookup
):

    st.header("🛒 Product Recommendation")

    st.markdown(
        "Recommend products using the trained ANN recommendation model."
    )

    customer_id = st.selectbox(
        "Select Customer",
        user_encoder.classes_
    )

    n_recommendations = st.slider(
        "Number of Recommendations",
        min_value=5,
        max_value=20,
        value=10
    )

    if st.button("Recommend Products"):

        with st.spinner("Generating recommendations..."):

            user_encoded = user_encoder.transform(
                [customer_id]
            )[0]

            all_products = np.arange(
                len(product_encoder.classes_)
            )

            user_array = np.full(
                len(all_products),
                user_encoded
            )

            predictions = ann_model.predict(
                [user_array, all_products],
                verbose=0
            ).flatten()

            top_indices = np.argsort(
                predictions
            )[::-1][:n_recommendations]

            recommended_products = (
                product_encoder.inverse_transform(
                    top_indices
                )
            )

            result_df = pd.DataFrame(
                {
                    "StockCode": recommended_products,
                    "Score": predictions[top_indices]
                }
            )

            result_df = result_df.merge(
                product_lookup,
                on="StockCode",
                how="left"
            )

        st.success(
            f"Top {n_recommendations} Recommendations Generated"
        )

        st.dataframe(
            result_df[
                [
                    "StockCode",
                    "Description",
                    "Score"
                ]
            ],
            use_container_width=True
        )

        csv = result_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "📥 Download Recommendations",
            data=csv, 
            file_name=f"{customer_id}_recommendations.csv",
            mime="text/csv"  
        )
        