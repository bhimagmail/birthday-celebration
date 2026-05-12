import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

# Your deployed Streamlit URL
BASE_URL = "https://birthday-celebration.streamlit.app"

# Read URL parameters
query_params = st.query_params

# If someone opens shared link
if "friend" in query_params and "sender" in query_params and "message" in query_params:

    friend_name = query_params["friend"]
    sender_name = query_params["sender"]
    message = query_params["message"]

    # Celebration effects
    st.balloons()
    st.snow()

    st.markdown(
        """
        <h1 style='text-align:center; color:#ff4b4b; font-size:60px;'>
        🎆 HAPPY BIRTHDAY 🎆
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            background-color:#fff5f5;
            padding:30px;
            border-radius:20px;
            text-align:center;
            box-shadow:0px 0px 20px rgba(0,0,0,0.1);
        ">
            <h1>🎂 Happy Birthday {friend_name}!</h1>
            <h3>{message}</h3>
            <h2>— From {sender_name}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.title("🎉 Birthday Celebration Generator")

    friend_name = st.text_input("Birthday Person's Name")
    sender_name = st.text_input("Your Name")

    message = st.text_area(
        "Birthday Wish",
        "Wishing you happiness, success, and endless joy on your special day!"
    )

    if st.button("Generate Shareable Birthday Link"):

        encoded_friend = urllib.parse.quote(friend_name)
        encoded_sender = urllib.parse.quote(sender_name)
        encoded_message = urllib.parse.quote(message)

        full_link = (
            f"{BASE_URL}"
            f"?friend={encoded_friend}"
            f"&sender={encoded_sender}"
            f"&message={encoded_message}"
        )

        st.success("🎉 Your Birthday Link is Ready!")

        st.subheader("Copy & Share This Link")

        st.code(full_link)

        st.markdown(
            f"""
            <a href="{full_link}" target="_blank">
                <button style="
                    background-color:#ff4b4b;
                    color:white;
                    padding:12px 20px;
                    border:none;
                    border-radius:10px;
                    font-size:18px;
                    cursor:pointer;
                ">
                    🎂 Preview Birthday Page
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )