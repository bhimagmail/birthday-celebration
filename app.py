import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

# Read URL query parameters
query_params = st.query_params

# If shared link contains data
if "friend" in query_params and "sender" in query_params and "message" in query_params:

    friend_name = query_params["friend"]
    sender_name = query_params["sender"]
    message = query_params["message"]

    # Celebration effects
    st.balloons()

    st.markdown(
        """
        <h1 style='text-align:center; color:#ff4b4b;'>
        🎆 HAPPY BIRTHDAY 🎆
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.header(f"🎂 Happy Birthday {friend_name}!")

    st.success(message)

    st.subheader(f"— From {sender_name}")

    st.snow()

    st.markdown("---")

    st.info("Someone special sent you this birthday wish ❤️")

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

        share_link = (
            f"?friend={encoded_friend}"
            f"&sender={encoded_sender}"
            f"&message={encoded_message}"
        )

        st.success("Birthday Link Generated!")

        st.subheader("Share This Link")

        st.code(share_link)

        st.warning(
            "After deployment, copy your Streamlit app URL and add this generated part to the end."
        )

        st.markdown("""
Example:

https://your-app-name.streamlit.app/?friend=John&sender=Alex&message=Happy+Birthday
""")