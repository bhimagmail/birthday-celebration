import streamlit as st

st.set_page_config(
    page_title="Birthday Celebration",
    page_icon="🎂",
    layout="centered"
)

st.balloons()

st.title("🎉 Birthday Celebration App")

friend_name = st.text_input("Enter Birthday Person's Name")
sender_name = st.text_input("Your Name")

message = st.text_area(
    "Write Your Birthday Wish",
    "Wishing you happiness, success, and joy on your special day!"
)

if st.button("Generate Birthday Wish"):

    st.success("Birthday Wish Generated Successfully!")

    st.markdown("---")

    st.header(f"🎂 Happy Birthday {friend_name}!")

    st.write(message)

    st.subheader(f"— From {sender_name}")

    st.balloons()

    share_text = f"""
Happy Birthday {friend_name}!

{message}

— From {sender_name}
"""

    st.code(share_text)

    st.info("Copy this message and share the Streamlit app link with your friend.")