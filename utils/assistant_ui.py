import streamlit as st

from utils.chat import load_retriever
from utils.gemini import ask_gemini


def assistant_page():

    retriever = load_retriever()

    st.header("🤖 RetailIQ AI Assistant")

    st.markdown(
        """
Ask anything about the RetailIQ project.

Examples:

• Why did we choose XGBoost?

• Explain the ANN Recommendation System.

• Why MobileNetV2?

• Explain the project architecture.

• Which datasets were used?

• Explain feature engineering.
"""
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask anything about the project..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Searching documentation..."):

            context, sources = retriever.retrieve(prompt)

            answer = ask_gemini(
                prompt,
                context
            )

        with st.chat_message("assistant"):

            st.markdown(answer)

            st.divider()

            st.subheader("📄 Sources")

            for src in sources:
                st.success(src)

            with st.expander(
                "Retrieved Context"
            ):
                st.write(context)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    st.divider()

    st.subheader("💡 Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Why XGBoost?"):
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": "Why was XGBoost selected?"
                }
            )

        if st.button("Explain ANN"):
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": "Explain the ANN recommendation system."
                }
            )

    with col2:

        if st.button("Why MobileNetV2?"):
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": "Why MobileNetV2?"
                }
            )

        if st.button("Explain Architecture"):
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": "Explain the architecture."
                }
            )