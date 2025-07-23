import streamlit as st
import datetime
import random
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="AniGPT V2 - Your AI Productivity Assistant", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with Modern Design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {visibility: hidden;}

/* Global Styling */
body {
    font-family: 'Inter', sans-serif !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: #FFFFFF !important;
    margin: 0; padding: 0;
}

/* Welcome Screen */
.welcome-container {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 60px 40px;
    text-align: center;
    margin: 40px auto;
    max-width: 700px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.welcome-title {
    font-size: 4rem;
    font-weight: 900;
    margin-bottom: 20px;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.welcome-subtitle {
    font-size: 1.4rem;
    opacity: 0.9;
    margin-bottom: 30px;
    font-weight: 400;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2rem;
    margin: 2rem 0;
    color: #fff;
    border: 1px solid rgba(255,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

# Initialize Session State
def init_state():
    if "user" not in st.session_state: st.session_state.user = ""
    if "authenticated" not in st.session_state: st.session_state.authenticated = False
    for name in ("mood_entries","journal_entries","goals","habits","tasks","chat_history"):
        if name not in st.session_state: st.session_state[name] = []
init_state()

# Simple AI Chat Stub
def ai_chat(prompt):
    options = [
        "🚀 Aaj ka din badiya banao!",
        "💪 Consistency hi key hai!",
        "🌟 Small steps pave big results!",
        "🎯 Focus on progress, not perfection!",
        "🤖 Main yahan hun, push karte raho!"
    ]
    return random.choice(options)

# Welcome / Login
if not st.session_state.authenticated:
    st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
    st.markdown("## 🤖 Welcome to AniGPT V2")
    st.markdown("Your Personal AI Productivity Companion")
    st.markdown("</div>", unsafe_allow_html=True)
    
    name = st.text_input("👤 Enter your name to begin", key="name_input")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌟 Start"):
            if name.strip():
                st.session_state.user = name.strip()
                st.session_state.authenticated = True
                for pct,msg in [
                    (20,"Initializing AI modules..."),
                    (40,"Setting up workspace..."),
                    (60,"Loading analytics..."),
                    (80,"Almost ready..."),
                    (100,f"Welcome, {st.session_state.user}!")
                ]:
                    st.progress(pct); st.info(msg); time.sleep(0.3)
                st.experimental_rerun()
            else:
                st.error("Please enter your name!")
    with col2:
        if st.button("👀 Quick Demo"):
            st.session_state.user = "Demo User"
            st.session_state.authenticated = True
            today = datetime.date.today()
            st.session_state.mood_entries = [
                {"timestamp": datetime.datetime.now()-datetime.timedelta(days=1),"mood":"😊 Happy","reason":"Great progress!","intensity":8,"energy":7,"date":today}
            ]
            st.session_state.journal_entries = [
                {"timestamp": datetime.datetime.now(),"title":"Demo Entry","content":"This is a demo journal entry.","category":"Demo","sentiment":"Positive","word_count":5,"date":today}
            ]
            st.session_state.goals = [{"name":"Learn Python","done":False}]
            st.session_state.habits = [{"name":"Daily Reading","count":3}]
            st.session_state.tasks = [{"task":"Finish report","done":False}]
            st.session_state.chat_history = [("AI","Hello Demo User!","10:00")]
            st.experimental_rerun()
    st.stop()

# Sidebar
with st.sidebar:
    st.markdown(f"### 👋 Hello, **{st.session_state.user}**")
    st.markdown("---")
    st.markdown("#### 📊 Stats")
    st.markdown(f"- 😊 Moods: {len(st.session_state.mood_entries)}")
    st.markdown(f"- 📝 Journals: {len(st.session_state.journal_entries)}")
    st.markdown(f"- 🎯 Goals: {len(st.session_state.goals)}")
    st.markdown(f"- 💪 Habits: {len(st.session_state.habits)}")
    st.markdown(f"- 📋 Tasks: {len(st.session_state.tasks)}")
    st.markdown("---")
    if st.button("🔄 Logout"):
        init_state()
        st.session_state.authenticated = False
        st.experimental_rerun()

# Main Tabs
tabs = st.tabs(["🏠 Dashboard","😊 Mood","📝 Journal","🎯 Goals","💪 Habits","📋 Tasks","🤖 Chat"])

# 1. Dashboard
with tabs[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 🏠 Dashboard")
    st.markdown("Your quick overview")
    if len(st.session_state.mood_entries) >= 2:
        df = pd.DataFrame(st.session_state.mood_entries)
        df["day"] = df["timestamp"].dt.strftime("%d %b")
        fig = px.line(df, x="day", y=["intensity","energy"],
                      labels={"value":"Level","day":"Date"},
                      title="Mood & Energy Trends")
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#fff")
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 2. Mood Tracker
with tabs[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 😊 Mood Tracker")
    mood = st.selectbox("How are you feeling?", ["😊 Happy","😢 Sad","😐 Neutral"])
    reason = st.text_input("Reason (optional)")
    intensity = st.slider("Intensity",1,10,5)
    energy = st.slider("Energy",1,10,5)
    if st.button("Save Mood"):
        st.session_state.mood_entries.append({
            "timestamp": datetime.datetime.now(),
            "mood": mood, "reason": reason,
            "intensity": intensity, "energy": energy,
            "date": datetime.date.today()
        })
        st.success("Mood saved!")
    st.markdown("### Recent Moods")
    for e in reversed(st.session_state.mood_entries[-5:]):
        t = e["timestamp"].strftime("%d %b %H:%M")
        st.write(f"{t} — {e['mood']} ({e['intensity']}/10)")
    st.markdown("</div>", unsafe_allow_html=True)

# 3. Journal
with tabs[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 📝 Journal")
    title = st.text_input("Title")
    content = st.text_area("Content")
    cat = st.selectbox("Category", ["Personal","Work","Learning"])
    if st.button("Save Entry"):
        wc = len(content.split())
        st.session_state.journal_entries.append({
            "timestamp": datetime.datetime.now(),
            "title": title, "content": content,
            "category": cat, "sentiment": "Neutral",
            "word_count": wc, "date": datetime.date.today()
        })
        st.success("Journal saved!")
    st.markdown("### Recent Entries")
    for j in reversed(st.session_state.journal_entries[-5:]):
        t = j["timestamp"].strftime("%d %b %H:%M")
        st.write(f"{t} — **{j['title']}** ({j['word_count']} words)")
    st.markdown("</div>", unsafe_allow_html=True)

# 4. Goals
with tabs[3]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 🎯 Goals")
    g = st.text_input("New Goal")
    if st.button("Add Goal"):
        st.session_state.goals.append({"name":g,"done":False})
        st.success("Goal added!")
    st.markdown("### Your Goals")
    for idx, goal in enumerate(st.session_state.goals):
        col1,col2 = st.columns([5,1])
        with col1: st.write(goal["name"])
        with col2:
            if st.button("✔️", key=f"g{idx}"):
                goal["done"] = True
                st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Habits
with tabs[4]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 💪 Habits")
    h = st.text_input("New Habit")
    if st.button("Add Habit"):
        st.session_state.habits.append({"name":h,"count":0})
        st.success("Habit added!")
    st.markdown("### Track Habits")
    for idx, habit in enumerate(st.session_state.habits):
        col1,col2 = st.columns([5,1])
        with col1: st.write(habit["name"])
        with col2:
            if st.button("+1", key=f"h{idx}"):
                habit["count"] += 1
                st.experimental_rerun()
        st.caption(f"Streak: {habit['count']} days")
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Tasks
with tabs[5]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 📋 Tasks")
    t = st.text_input("New Task")
    if st.button("Add Task"):
        st.session_state.tasks.append({"task":t,"done":False})
        st.success("Task added!")
    st.markdown("### Task List")
    for idx, task in enumerate(st.session_state.tasks):
        col1,col2 = st.columns([5,1])
        with col1: st.write(task["task"])
        with col2:
            if st.button("✔️", key=f"t{idx}"):
                task["done"] = True
                st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 7. AI Chat
with tabs[6]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## 🤖 AI Companion")
    prompt = st.text_input("Ask me anything:")
    if st.button("Send"):
        reply = ai_chat(prompt)
        st.session_state.chat_history.append(("You", prompt, datetime.datetime.now().strftime("%H:%M")))
        st.session_state.chat_history.append(("AI", reply, datetime.datetime.now().strftime("%H:%M")))
    st.markdown("### Conversation")
    for speaker, msg, t in st.session_state.chat_history[-10:]:
        if speaker == "You":
            st.write(f"👤 {t} — {msg}")
        else:
            st.write(f"🤖 {t} — {msg}")
    st.markdown("</div>", unsafe_allow_html=True)
