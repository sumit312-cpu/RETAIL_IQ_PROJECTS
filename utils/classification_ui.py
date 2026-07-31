import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image


def classification_page(
    classification_model,
    label_encoder
):

    st.header("🖼️ Product Classification")

    st.markdown(
        """
Upload a product image and classify it using the
trained **MobileNetV2 Transfer Learning Model**.
"""
    )

    uploaded_file = st.file_uploader(
        "Upload Product Image",
        type=["jpg", "jpeg", "png", "webp", "avif"],
        key="classifier"
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    with col2:

        with st.spinner("Analyzing image..."):

            img = image.resize((224, 224))

            img = np.array(img) / 255.0

            img = np.expand_dims(
                img,
                axis=0
            )

            predictions = classification_model.predict(
                img,
                verbose=0
            )[0]

        predicted_index = np.argmax(predictions)

        confidence = predictions[predicted_index]

        category = label_encoder.inverse_transform(
            [predicted_index]
        )[0]

        st.success(
            f"Prediction: **{category}**"
        )

        st.metric(
            "Confidence",
            f"{confidence*100:.2f}%"
        )

        st.progress(float(confidence))

    st.divider()

    st.subheader("🏆 Top 3 Predictions")

    top3 = np.argsort(predictions)[::-1][:3]

    rows = []

    for idx in top3:

        rows.append({

            "Category":
            label_encoder.inverse_transform(
                [idx]
            )[0],

            "Confidence":
            predictions[idx]

        })

    results = pd.DataFrame(rows)

    for _, row in results.iterrows():

        st.write(
            f"**{row['Category']}**"
        )

        st.progress(
            float(row["Confidence"])
        )

        st.caption(
            f"{row['Confidence']*100:.2f}%"
        )

    st.divider()

    st.subheader("Prediction Table")

    results["Confidence"] = (
        results["Confidence"] * 100
    ).round(2)

    results["Confidence"] = (
        results["Confidence"]
        .astype(str)
        + "%"
    )

    st.dataframe(
        results,
        use_container_width=True
    )