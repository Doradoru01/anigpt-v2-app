import streamlit as st
import pandas as pd
import datetime
import random
import time

# Page config
st.set_page_config(
    page_title="AniGPT V2 - Personal AI Assistant", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)

# Clean Modern CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global Styling */
.main {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #FFFFFF;
}

/* Welcome Screen */
.welcome-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
    text-align: center;
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    margin: 40px 20px;
    padding: 40px 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
}

.welcome-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 20px;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.welcome-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: 40px;
    font-weight: 400;
}

/* Top Header */
.top-header {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    padding: 15px 30px;
    border-radius: 15px;
    margin: 20px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.user-info {
    display: flex;
    align-items: center;
    gap: 15px;
}

.user-name {
    font-size: 1.3rem;
    font-weight: 600;
    color: #FFFFFF;
}

.user-status {
    background: linear-gradient(45deg, #4ECDC4, #44A08D);
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 15px;
    padding: 25px;
    margin: 20px 0;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: translateY(-2px);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 25px !important;
    font-weight: 500 !important;
    font-size: 16px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 15px rgba(255,107,107,0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(255,107,107,0.4) !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    background: rgba(255,255,255,0.9) !important;
    border: 2px solid rgba(255,255,255,0.3) !important;
    border-radius: 8px !important;
    color: #333 !important;
    font-size: 16px !important;
    padding: 12px !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #4ECDC4 !important;
    box-shadow: 0 0 10px rgba(78,205,196,0.3) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 8px;
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.1);
    border-radius: 8px;
    color: white;
    font-weight: 500;
    padding: 10px 20px;
    border: 1px solid rgba(255,255,255,0.2);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    border-color: rgba(255,255,255,0.3);
}

/* Sidebar */
.sidebar-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 12px;
    padding: 20px;
    margin: 15px 0;
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
}

/* Success/Error Messages */
.stSuccess > div {
    background: linear-gradient(45deg, #4ECDC4, #44A08D) !important;
    border-radius: 10px !important;
    border: none !important;
}

.stError > div {
    background: linear-gradient(45deg, #FF6B6B, #FF5252) !important;
    border-radius: 10px !important;
    border: none !important;
}

/* Metrics */
.metric-card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 10px 0;
}

/* Chat Messages */
.chat-user {
    background: rgba(255,107,107,0.2);
    padding: 15px;
    border-radius: 15px 15px 5px 15px;
    margin: 10px 0;
    margin-left: 20%;
}

.chat-ai {
    background: rgba(78,205,196,0.2);
    padding: 15px;
    border-radius: 15px 15px 15px 5px;
    margin: 10px 0;
    margin-right: 20%;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .welcome-title {
        font-size: 2.5rem;
    }
    
    .top-header {
        padding: 15px;
        margin: 10px 0;
        flex-direction: column;
        gap: 10px;
    }
    
    .user-info {
        flex-direction: column;
        gap: 10px;
    }
    
    .card {
        padding: 20px 15px;
        margin: 10px 0;
    }
    
    .chat-user, .chat-ai {
        margin-left: 0;
        margin-right: 0;
    }
}

@media (max-width: 480px) {
    .welcome-container {
        margin: 20px 10px;
        padding: 30px 15px;
    }
    
    .welcome-title {
        font-size: 2rem;
    }
}

</style>
""", unsafe_allow_html=True)

# Initialize session states
def initialize_session_states():
    if "user_authenticated" not in st.session_state:
        st.session_state.user_authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "mood_entries" not in st.session_state:
        st.session_state.mood_entries = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "goals" not in st.session_state:
        st.session_state.goals = []
    if "habits" not in st.session_state:
        st.session_state.habits = []
    if "thoughts" not in st.session_state:
        st.session_state.thoughts = []

initialize_session_states()

# AI Chat Function
def ai_chat_hinglish(user_input):
    user_input_lower = user_input.lower()
    
    if any(word in user_input_lower for word in ['sad', 'upset', 'dukhi', 'pareshaan', 'tension']):
        responses = [
            "🤗 Arre yaar, tension mat lo! Sab theek ho jayega. Kya specific problem hai?",
            "💪 Bhai, life me ups-downs aate rehte hain. Focus rakho positive things par!",
            "🌟 Mood down hai? Koi small achievement celebrate karo, better feel karoge!",
            "💝 Dost, sharing se halka lagta hai. Main yahan hun sunne ke liye!"
        ]
    elif any(word in user_input_lower for word in ['happy', 'khush', 'accha', 'mast', 'good']):
        responses = [
            "🎉 Waah bhai! Khushi ki baat hai. Is positive energy ko productive kaam me lagao!",
            "🚀 Mast hai yaar! Good mood me goals set karne ka perfect time hai!",
            "⭐ Bahut badhiya! Is happiness ko journal me capture kar lo!",
            "🔥 Superb! Happy mood me habits complete karna easy hota hai!"
        ]
    elif any(word in user_input_lower for word in ['goal', 'target', 'achieve', 'complete']):
        responses = [
            "🎯 Goals ki baat? Fantastic! Small steps me divide karo, achieve karna easy hoga!",
            "📈 Target achieve karna hai? Daily progress track karte raho!",
            "🏆 Success pakki milegi! Consistency maintain karo bas!",
            "💡 Big goals scary lagte hain, but small tasks me break karo!"
        ]
    elif any(word in user_input_lower for word in ['habit', 'daily', 'routine']):
        responses = [
            "💪 Habits? Yahi toh real game-changer hai! Small start karo!",
            "🔥 Daily consistency se kuch bhi possible hai bhai!",
            "⚡ 1% daily improvement = 37x better in 1 year!",
            "🌟 Habit formation me 21 days lagte hain, patience rakho!"
        ]
    else:
        responses = [
            "😊 Haan bhai, samajh gaya! Main tumhara AI buddy hun, kya aur help chahiye?",
            "💭 Interesting point! Aur detail me batao kya chal raha hai?",
            "✨ Bilkul sahi direction me ja rahe ho! Keep it up!",
            "🎯 Focus rakho apne goals par, main support kar raha hun!",
            "🚀 Great! Aur kuch discuss karna hai?"
        ]
    
    return random.choice(responses)

# Welcome/Login Screen
if not st.session_state.user_authenticated:
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-title">🤖 AniGPT V2</div>
        <div class="welcome-subtitle">Your Personal AI Assistant</div>
        <div class="welcome-subtitle">Track • Learn • Grow • Achieve</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered input form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        
        username = st.text_input(
            "👤 Enter your name to continue:",
            placeholder="Your name here...",
            key="username_input"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Get Started", type="primary", key="enter_button", use_container_width=True):
            if username.strip():
                st.session_state.username = username.strip()
                st.session_state.user_authenticated = True
                
                # Simple loading
                with st.spinner("Setting up your workspace..."):
                    time.sleep(1)
                
                st.success(f"Welcome {username}! 🎉")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Please enter your name!")

# Main Dashboard
else:
    # Top Header with User Info
    st.markdown(f"""
    <div class="top-header">
        <div class="user-info">
            <div>
                <div class="user-name">👋 Hello, {st.session_state.username}!</div>
                <small style="opacity: 0.8;">Welcome to your personal AI workspace</small>
            </div>
        </div>
        <div class="user-status">✨ Online</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-card">
            <h3>👤 {st.session_state.username}</h3>
            <p style="opacity: 0.8;">Personal AI Assistant</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Stats
        st.markdown("### 📊 Quick Stats")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>😊 {len(st.session_state.mood_entries)}</h3>
                <p>Moods</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>💪 {len(st.session_state.habits)}</h3>
                <p>Habits</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("🔄 Switch User", key="switch_user"):
            st.session_state.user_authenticated = False
            st.session_state.username = ""
            st.rerun()
    
    # Main Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Dashboard", "😊 Mood", "📝 Notes", "💪 Habits", "🤖 AI Chat"
    ])
    
    # Dashboard Tab
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🏠 Dashboard Overview")
        
        # Quick stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("😊 Mood Entries", len(st.session_state.mood_entries), delta=1 if st.session_state.mood_entries else 0)
        
        with col2:
            st.metric("📝 Notes", len(st.session_state.thoughts), delta=1 if st.session_state.thoughts else 0)
        
        with col3:
            st.metric("💪 Habits", len(st.session_state.habits), delta=1 if st.session_state.habits else 0)
        
        with col4:
            st.metric("🤖 AI Chats", len(st.session_state.chat_history), delta=1 if st.session_state.chat_history else 0)
        
        st.markdown("---")
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("📝 Quick Mood Log", key="quick_mood"):
                st.info("Go to Mood tab to log your current mood! 😊")
        
        with col_b:
            if st.button("💭 Quick Note", key="quick_note"):
                st.info("Visit Notes tab to capture your thoughts! 📝")
        
        with col_c:
            if st.button("💪 Check Habits", key="quick_habits"):
                st.info("Habits tab me jao to track your progress! 🔥")
        
        # Recent activity
        if st.session_state.mood_entries or st.session_state.thoughts:
            st.markdown("### 📈 Recent Activity")
            
            if st.session_state.mood_entries:
                latest_mood = st.session_state.mood_entries[-1]
                st.info(f"Latest Mood: {latest_mood['mood']} (Intensity: {latest_mood['intensity']}/10)")
            
            if st.session_state.thoughts:
                latest_thought = st.session_state.thoughts[-1]
                st.info(f"Latest Note: {latest_thought['content'][:50]}...")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mood Tab
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 😊 Mood Tracker")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            mood_options = [
                "😊 Happy",
                "😢 Sad", 
                "😐 Neutral",
                "😤 Frustrated",
                "🤔 Thoughtful",
                "😴 Tired",
                "🥳 Excited",
                "😰 Anxious",
                "😌 Peaceful"
            ]
            
            selected_mood = st.selectbox("🌈 How are you feeling?", mood_options)
            
            reason = st.text_area(
                "📝 What's happening?",
                placeholder="Work, family, health, achievements, challenges...",
                height=100
            )
        
        with col2:
            intensity = st.slider("🎚️ Intensity Level:", 1, 10, 5)
            st.caption(f"Level: {intensity}/10")
            
            energy = st.slider("⚡ Energy Level:", 1, 10, 5)
            st.caption(f"Energy: {energy}/10")
        
        # Save mood
        if st.button("💾 Save Mood", type="primary", key="save_mood"):
            if selected_mood and reason:
                entry = {
                    "timestamp": datetime.datetime.now(),
                    "user": st.session_state.username,
                    "mood": selected_mood,
                    "reason": reason,
                    "intensity": intensity,
                    "energy": energy
                }
                st.session_state.mood_entries.append(entry)
                
                st.success("✅ Mood saved successfully!")
                st.balloons()
            else:
                st.error("Please fill all fields!")
        
        # Recent moods
        if st.session_state.mood_entries:
            st.markdown("### 📊 Recent Moods")
            
            for mood in st.session_state.mood_entries[-3:]:
                timestamp = mood['timestamp'].strftime('%H:%M')
                st.info(f"⏰ {timestamp} | {mood['mood']} | Intensity: {mood['intensity']}/10")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Notes Tab
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📝 Quick Notes")
        
        note_content = st.text_area(
            "💭 What's on your mind?",
            placeholder="Ideas, thoughts, reflections, learnings...",
            height=150
        )
        
        if st.button("💾 Save Note", type="primary", key="save_note"):
            if note_content:
                note = {
                    "timestamp": datetime.datetime.now(),
                    "user": st.session_state.username,
                    "content": note_content,
                    "word_count": len(note_content.split())
                }
                st.session_state.thoughts.append(note)
                st.success("✅ Note saved!")
                st.balloons()
            else:
                st.error("Please write something!")
        
        # Recent notes
        if st.session_state.thoughts:
            st.markdown("### 📚 Recent Notes")
            
            for thought in st.session_state.thoughts[-3:]:
                timestamp = thought['timestamp'].strftime('%d/%m %H:%M')
                st.markdown(f"""
                **⏰ {timestamp}**  
                💭 {thought['content']}  
                📊 Words: {thought['word_count']}
                """)
                st.markdown("---")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Habits Tab
    with tab4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 💪 Habit Tracker")
        
        # Add habit
        col1, col2 = st.columns(2)
        
        with col1:
            habit_name = st.text_input("💪 New Habit:", placeholder="Exercise, Reading, Meditation...")
        
        with col2:
            habit_category = st.selectbox("📁 Category:", ["🏃 Health", "📚 Learning", "💼 Work", "🧘 Wellness"])
        
        if st.button("✅ Add Habit", type="primary", key="add_habit"):
            if habit_name:
                habit = {
                    "id": len(st.session_state.habits) + 1,
                    "name": habit_name,
                    "category": habit_category,
                    "streak": 0,
                    "total": 0
                }
                st.session_state.habits.append(habit)
                st.success(f"💪 {habit_name} added!")
                st.balloons()
            else:
                st.error("Please enter habit name!")
        
        # Show habits
        if st.session_state.habits:
            st.markdown("### 🔥 Your Habits")
            
            for habit in st.session_state.habits:
                col_habit1, col_habit2, col_habit3 = st.columns([2, 1, 1])
                
                with col_habit1:
                    st.markdown(f"**💪 {habit['name']}**")
                    st.caption(f"{habit['category']}")
                
                with col_habit2:
                    st.metric("🔥 Streak", f"{habit['streak']} days")
                
                with col_habit3:
                    if st.button(f"✅ Done", key=f"complete_{habit['id']}"):
                        habit['total'] += 1
                        habit['streak'] += 1
                        st.success(f"🔥 Streak: {habit['streak']} days!")
                        st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # AI Chat Tab
    with tab5:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI Assistant")
        
        # Chat history
        if st.session_state.chat_history:
            for i, (speaker, message, timestamp) in enumerate(st.session_state.chat_history[-6:]):
                if speaker == "You":
                    st.markdown(f"""
                    <div class="chat-user">
                        <strong>👤 You</strong> <small>({timestamp})</small><br>
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-ai">
                        <strong>🤖 AniGPT</strong> <small>({timestamp})</small><br>
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Chat input
        user_input = st.text_input(
            "💬 Message:",
            placeholder="Ask me anything! Motivation, guidance, casual chat..."
        )
        
        col_send, col_clear = st.columns([3, 1])
        
        with col_send:
            if st.button("📤 Send", type="primary", key="send_message"):
                if user_input:
                    ai_response = ai_chat_hinglish(user_input)
                    current_time = datetime.datetime.now().strftime("%H:%M")
                    
                    st.session_state.chat_history.append(("You", user_input, current_time))
                    st.session_state.chat_history.append(("AI", ai_response, current_time))
                    
                    if len(st.session_state.chat_history) > 20:
                        st.session_state.chat_history = st.session_state.chat_history[-20:]
                    
                    st.rerun()
        
        with col_clear:
            if st.button("🗑️ Clear", key="clear_chat"):
                st.session_state.chat_history = []
                st.rerun()
        
        # Quick buttons
        st.markdown("### ⚡ Quick Commands")
        
        col_q1, col_q2, col_q3 = st.columns(3)
        
        with col_q1:
            if st.button("💡 Motivate Me", key="motivate"):
                motivation = "🌟 You're doing great! Every small step counts. Keep moving forward! 🚀"
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", motivation, current_time))
                st.rerun()
        
        with col_q2:
            if st.button("📊 My Stats", key="show_stats"):
                stats = f"""
                📊 Your Progress:
                • Mood Entries: {len(st.session_state.mood_entries)}
                • Notes Written: {len(st.session_state.thoughts)}
                • Habits Tracked: {len(st.session_state.habits)}
                
                Keep going! 💪
                """
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", stats, current_time))
                st.rerun()
        
        with col_q3:
            if st.button("🎯 Daily Tip", key="daily_tip"):
                tips = [
                    "🎯 Set one small goal for today and achieve it!",
                    "💪 Consistency beats intensity every time!",
                    "😊 Track your mood to understand patterns better!",
                    "📝 Write down your thoughts - it helps clarity!",
                    "🌟 Celebrate small wins - they add up!"
                ]
                tip = random.choice(tips)
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", tip, current_time))
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; opacity: 0.8;">
        <h4>🤖 AniGPT V2 - Your Personal AI Assistant</h4>
        <p>User: {st.session_state.username} | Made with ❤️ for productivity</p>
    </div>
    """, unsafe_allow_html=True)
