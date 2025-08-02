import streamlit as st
from gtts import gTTS
import os

# App settings
st.set_page_config(page_title="Dyslexia Text Reader", page_icon="📖")

# App intro
st.markdown("""
# 📖 Dyslexia Text Reader  
This tool helps people with **dyslexia** read better by improving the **text appearance** and reading it **aloud**.
📝 **Paste any text**, and we'll show it in a dyslexia-friendly format with a **Listen** option.
""")

# Text input
text = st.text_area("Enter your text:", height=200)

# Apply styling
if text:
    st.markdown("### 👁️‍🗨️ Dyslexia-Friendly View")
    st.markdown(f"""
        <div style="font-family: 'OpenDyslexic3', sans-serif;
                    font-size: 20px;
                    line-height: 1.8;
                    letter-spacing: 2px;
                    background-color: #f4f4f4;
                    padding: 20px;
                    border-radius: 10px;">
            {text}
        </div>
        """, unsafe_allow_html=True)

    # Text-to-Speech
    if st.button("🔊 Listen"):
        tts = gTTS(text)
        tts.save("speech.mp3")
        audio_file = open("speech.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

# Footer
st.markdown("---")
st.markdown("💙 _Made to support and empower readers with dyslexia._")
