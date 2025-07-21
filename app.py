import streamlit as st
import datetime
import random

# Page config
st.set_page_config(page_title="AniGPT V2", layout="wide", page_icon="🤖")

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "mood_data" not in st.session_state:
    st.session_state.mood_data = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Simple AI Chat
def simple_ai_chat(user_input):
    responses = [
        "Haan bhai, samajh gaya! Aur kya help chahiye?",
        "Bilkul sahi! Keep it up!",
        "Accha point! Daily consistency important hai!",
        "Waah yaar, good thinking!"
    ]
    return random.choice(responses)

# Header
st.markdown('<div class="main-header"><h1>🚀 AniGPT V2</h1><p>Hinglish AI Assistant 🇮🇳</p></div>', unsafe_allow_html=True)

# Sidebar
user = st.sidebar.text_input("Apna naam:", "testuser")
st.sidebar.metric("Mood Entries", len(st.session_state.mood_data))

# Main tabs
tab1, tab2 = st.tabs(["😊 Mood", "🤖 Chat"])

# Mood Tab
with tab1:
    st.header("😊 Mood Tracker")
    
    mood = st.text_input("Aaj ka mood:", placeholder="😊 Happy")
    reason = st.text_input("Kya ho raha hai:", placeholder="Reason")
    intensity = st.slider("Intensity:", 1, 10, 5)
    
    if st.button("Save Mood"):
        if mood:
            entry = {
                "user": user,
                "time": datetime.datetime.now().strftime('%H:%M'),
                "mood": mood,
                "reason": reason,
                "intensity": intensity
            }
            st.session_state.mood_data.append(entry)
            st.success(f"✅ Mood saved: {mood}")
            st.balloons()
    
    # Show recent moods
    if st.session_state.mood_data:
        st.markdown("### Recent Moods")
        for entry in st.session_state.mood_data[-3:]:
            st.info(f"⏰ {entry['time']} | {entry['mood']} | {entry['intensity']}/10")

# Chat Tab  
with tab2:
    st.header("🤖 Chat")
    
    # Chat input
    user_input = st.text_input("Type karo:", placeholder="Hello!")
    
    if st.button("Send"):
        if user_input:
            ai_response = simple_ai_chat(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("AI", ai_response))
            st.rerun()
    
    # Show chat
    if st.session_state.chat_history:
        for speaker, msg in st.session_state.chat_history[-6:]:
            if speaker == "You":
                st.markdown(f"**🧑 You:** {msg}")
            else:
                st.markdown(f"**🤖 AI:** {msg}")

st.markdown("---")
st.markdown("<center>AniGPT V2 - Working Version! 🚀</center>", unsafe_allow_html=True)
