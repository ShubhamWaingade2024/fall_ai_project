
import streamlit as st

import requests


st.title("AI Fall Detection")


video=st.file_uploader("Upload video")


if video:

    st.video(video)

    files={"file":video}

    res=requests.post(

    "http://127.0.0.1:8000/detect",

    files=files

    )


    if res.status_code!=200:

        st.error("Backend error")

    else:

        data=res.json()

        if "confidence" in data:

            st.error("PERSON FALL DETECTED")

            st.write("Confidence")

            st.progress(int(data["confidence"]*100))

            st.subheader("Location")

            st.markdown(data["location"])

            st.map({

            "lat":[18.5204],

            "lon":[73.8567]

            })


            st.subheader("First Aid")

            st.write(data["aid"])


            st.subheader("Nearest hospitals")

            for h in data["hospitals"]:

                st.write(h)

        else:

            st.success("No fall detected")