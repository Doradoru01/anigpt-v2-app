import streamlit as st
import pandas as pd
import datetime
import random
import time

# Page config
st.set_page_config(
    page_title="🚀 AniGPT V2 - Future AI", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)

# Ultra-Advanced CSS with Futuristic Design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&display=swap');

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global Styling */
.main {
    background: 
        radial-gradient(circle at 20% 50%, #120458 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, #8B2635 0%, transparent 50%),
        radial-gradient(circle at 40% 80%, #0F4C75 0%, transparent 50%),
        radial-gradient(circle at 0% 0%, #2E3440 0%, transparent 50%),
        linear-gradient(135deg, #0F0F23 0%, #1A1A2E 50%, #16213E 100%);
    min-height: 100vh;
    font-family: 'Rajdhani', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
}

/* Animated Background Particles */
.main::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, rgba(255,255,255,0.3), transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(100,200,255,0.4), transparent),
        radial-gradient(1px 1px at 90px 40px, rgba(255,100,200,0.3), transparent),
        radial-gradient(1px 1px at 130px 80px, rgba(100,255,100,0.3), transparent);
    background-repeat: repeat;
    background-size: 200px 100px;
    animation: twinkle 4s linear infinite;
    pointer-events: none;
    z-index: -1;
}

@keyframes twinkle {
    0% { transform: translateY(0px) translateX(0px); opacity: 0.3; }
    50% { opacity: 0.8; }
    100% { transform: translateY(-100px) translateX(50px); opacity: 0.3; }
}

/* Welcome Screen Styling */
.welcome-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    text-align: center;
    background: rgba(255,255,255,0.02);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 30px;
    margin: 20px;
    position: relative;
    overflow: hidden;
    box-shadow: 
        0 25px 50px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.2);
}

.welcome-container::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(45deg, #ff00ff, #00ffff, #ff00ff, #00ffff);
    border-radius: 30px;
    z-index: -1;
    animation: gradient-border 3s linear infinite;
}

@keyframes gradient-border {
    0% { filter: hue-rotate(0deg); }
    100% { filter: hue-rotate(360deg); }
}

.welcome-title {
    font-family: 'Orbitron', monospace;
    font-size: 4rem;
    font-weight: 900;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient-text 3s ease-in-out infinite;
    text-shadow: 0 0 30px rgba(255,255,255,0.5);
    margin-bottom: 20px;
}

@keyframes gradient-text {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.welcome-subtitle {
    font-size: 1.5rem;
    color: rgba(255,255,255,0.8);
    margin-bottom: 40px;
    font-weight: 300;
}

.hologram-effect {
    position: relative;
    display: inline-block;
}

.hologram-effect::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(255,255,255,0.1) 50%,
        transparent 100%
    );
    animation: hologram-scan 2s linear infinite;
}

@keyframes hologram-scan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Futuristic Input Styling */
.futuristic-input {
    background: rgba(255,255,255,0.05);
    border: 2px solid rgba(100,200,255,0.3);
    border-radius: 15px;
    padding: 15px 25px;
    font-size: 18px;
    color: #FFFFFF;
    font-family: 'Orbitron', monospace;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 
        0 10px 30px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.1);
    transition: all 0.3s ease;
    margin: 20px;
    min-width: 300px;
}

.futuristic-input:focus {
    border-color: #00FFFF;
    box-shadow: 
        0 0 30px rgba(0,255,255,0.5),
        0 10px 30px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.2);
    transform: translateY(-2px);
}

/* Futuristic Button */
.cyber-button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    border: none;
    border-radius: 25px;
    padding: 15px 40px;
    font-size: 18px;
    font-weight: 700;
    font-family: 'Orbitron', monospace;
    color: #FFFFFF;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 
        0 10px 30px rgba(255,107,107,0.3),
        0 0 0 1px rgba(255,255,255,0.2);
    text-transform: uppercase;
    letter-spacing: 2px;
}

.cyber-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    transition: all 0.5s ease;
}

.cyber-button:hover::before {
    left: 100%;
}

.cyber-button:hover {
    transform: translateY(-3px);
    box-shadow: 
        0 15px 40px rgba(255,107,107,0.5),
        0 0 20px rgba(78,205,196,0.3);
}

/* Dashboard Header */
.dashboard-header {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 30px;
    margin: 20px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.dashboard-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
    animation: loading-bar 2s linear infinite;
}

@keyframes loading-bar {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.dashboard-title {
    font-family: 'Orbitron', monospace;
    font-size: 2.5rem;
    font-weight: 700;
    color: #FFFFFF;
    text-shadow: 0 0 20px rgba(255,255,255,0.3);
    margin-bottom: 10px;
}

.user-welcome {
    font-size: 1.2rem;
    color: rgba(255,255,255,0.7);
    font-weight: 300;
}

/* Futuristic Cards */
.feature-card {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 
        0 15px 35px rgba(0,0,0,0.2),
        inset 0 1px 0 rgba(255,255,255,0.1);
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #4ECDC4, transparent);
    animation: card-glow 3s ease-in-out infinite;
}

@keyframes card-glow {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
}

.feature-card:hover {
    transform: translateY(-5px) scale(1.02);
    border-color: rgba(78,205,196,0.5);
    box-shadow: 
        0 25px 50px rgba(0,0,0,0.3),
        0 0 30px rgba(78,205,196,0.2),
        inset 0 1px 0 rgba(255,255,255,0.2);
}

/* Futuristic Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.03);
    border-radius: 20px;
    padding: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 15px;
    color: #FFFFFF;
    font-family: 'Orbitron', monospace;
    font-weight: 600;
    padding: 12px 20px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,255,255,0.1);
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    border-color: rgba(255,255,255,0.3);
    box-shadow: 
        0 10px 30px rgba(255,107,107,0.3),
        0 0 20px rgba(78,205,196,0.2);
    transform: translateY(-2px);
}

/* Futuristic Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 2px solid rgba(100,200,255,0.3) !important;
    border-radius: 12px !important;
    color: #FFFFFF !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 16px !important;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #00FFFF !important;
    box-shadow: 0 0 20px rgba(0,255,255,0.3) !important;
    transform: translateY(-1px);
}

/* Futuristic Buttons */
.stButton > button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 20px !important;
    padding: 12px 30px !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    transition: all 0.3s ease !important;
    box-shadow: 
        0 8px 25px rgba(255,107,107,0.3),
        0 0 0 1px rgba(255,255,255,0.1) !important;
    position: relative;
    overflow: hidden;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 
        0 15px 40px rgba(255,107,107,0.4),
        0 0 30px rgba(78,205,196,0.3) !important;
}

/* Futuristic Metrics */
.metric-card {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.metric-card:hover {
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
}

/* Success/Error Messages */
.stSuccess > div {
    background: linear-gradient(45deg, #4ECDC4, #44A08D) !important;
    border-radius: 15px !important;
    border: none !important;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(78,205,196,0.3);
}

.stError > div {
    background: linear-gradient(45deg, #FF6B6B, #FF5252) !important;
    border-radius: 15px !important;
    border: none !important;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(255,107,107,0.3);
}

/* Sidebar Futuristic */
.css-1d391kg {
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* Loading Animation */
.loading-text {
    font-family: 'Orbitron', monospace;
    font-size: 1.2rem;
    color: #4ECDC4;
    text-align: center;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.6; }
    50% { opacity: 1; }
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
}

/* Chat Messages */
.chat-message {
    padding: 15px 20px;
    margin: 10px 0;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    position: relative;
    overflow: hidden;
}

.user-message {
    background: rgba(255,107,107,0.1);
    margin-left: 20%;
    border-left: 3px solid #FF6B6B;
}

.ai-message {
    background: rgba(78,205,196,0.1);
    margin-right: 20%;
    border-left: 3px solid #4ECDC4;
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #4ECDC4, #44A08D) !important;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(78,205,196,0.3);
}

/* Responsive */
@media (max-width: 768px) {
    .welcome-title {
        font-size: 2.5rem;
    }
    
    .welcome-container {
        margin: 10px;
        border-radius: 20px;
    }
    
    .futuristic-input {
        min-width: 250px;
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

initialize_session_states()

# AI Chat Function
def ai_chat_hinglish(user_input):
    user_input_lower = user_input.lower()
    
    if any(word in user_input_lower for word in ['sad', 'upset', 'dukhi', 'pareshaan']):
        responses = [
            "🤗 Arre yaar, tension mat lo! Sab theek ho jayega. Kya specific problem hai?",
            "💪 Bhai, life me ups-downs aate rehte hain. Analytics dekho, kitna progress kiya hai!",
            "🌟 Mood down hai? Koi habit complete karo, instantly better feel karoge!",
            "💝 Dost, journal me feelings likh do. Sharing se halka ho jayega!"
        ]
    elif any(word in user_input_lower for word in ['happy', 'khush', 'accha', 'mast']):
        responses = [
            "🎉 Waah bhai! Khushi ki baat hai. Is positive energy me naya goal set karo!",
            "🚀 Mast hai yaar! Good mood me productivity double hoti hai!",
            "⭐ Bahut badhiya! Is happiness ko journal me capture kar lo!",
            "🔥 Superb! Happy mood me habits complete karna easy hota hai!"
        ]
    elif any(word in user_input_lower for word in ['goal', 'target', 'achieve']):
        responses = [
            "🎯 Goals ki baat? Fantastic! SMART goals banao - specific, measurable!",
            "📈 Target achieve karna hai? Daily progress track karo!",
            "🏆 Success pakki milegi! Consistency maintain karo!",
            "💡 Big goals ko small steps me break karo!"
        ]
    else:
        responses = [
            "🤖 Haan bhai, samajh gaya! Main tumhara AI companion hun!",
            "✨ Interesting point! Analytics dekho patterns ke liye!",
            "🎯 Bilkul sahi direction me ja rahe ho!",
            "🚀 Keep growing! Main yahin hun support ke liye!"
        ]
    
    return random.choice(responses)

# Welcome/Login Screen
if not st.session_state.user_authenticated:
    st.markdown("""
    <div class="welcome-container">
        <div class="hologram-effect">
            <div class="welcome-title">AniGPT V2</div>
        </div>
        <div class="welcome-subtitle">🚀 Your Futuristic AI Companion</div>
        <div class="welcome-subtitle">Enter the Future of Personal Productivity</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered input form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        username = st.text_input(
            "",
            placeholder="🚀 Enter your name to begin your journey...",
            key="username_input",
            help="Type your name and press Enter to access AniGPT V2"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        
        with col_b:
            if st.button("🌟 Enter the Future", type="primary", key="enter_button"):
                if username.strip():
                    st.session_state.username = username.strip()
                    st.session_state.user_authenticated = True
                    
                    # Loading animation
                    progress_placeholder = st.empty()
                    status_placeholder = st.empty()
                    
                    for i in range(101):
                        progress_placeholder.progress(i)
                        if i < 33:
                            status_placeholder.markdown('<p class="loading-text">🔍 Scanning biometrics...</p>', unsafe_allow_html=True)
                        elif i < 66:
                            status_placeholder.markdown('<p class="loading-text">🧠 Loading AI modules...</p>', unsafe_allow_html=True)
                        else:
                            status_placeholder.markdown('<p class="loading-text">🚀 Initializing workspace...</p>', unsafe_allow_html=True)
                        time.sleep(0.02)
                    
                    progress_placeholder.empty()
                    status_placeholder.success(f"Welcome aboard, {username}! 🎉")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("🚨 Please enter your name to continue!")

# Main Dashboard
else:
    # Header
    st.markdown(f"""
    <div class="dashboard-header">
        <div class="dashboard-title">🚀 AniGPT V2 COMMAND CENTER</div>
        <div class="user-welcome">Welcome back, Commander {st.session_state.username}! Ready to conquer your goals? 💪</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Sidebar
    with st.sidebar:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        ">
            <h2>👤 {st.session_state.username}</h2>
            <p>Productivity Commander</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Live stats
        st.markdown("### 📊 Mission Status")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>😊</h3>
                <h2>{len(st.session_state.mood_entries)}</h2>
                <p>Moods</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <h3>🎯</h3>
                <h2>{len(st.session_state.goals)}</h2>
                <p>Goals</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>💪</h3>
                <h2>{len(st.session_state.habits)}</h2>
                <p>Habits</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <h3>🤖</h3>
                <h2>{len(st.session_state.chat_history)}</h2>
                <p>AI Chats</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("🔄 Switch User", key="switch_user"):
            st.session_state.user_authenticated = False
            st.session_state.username = ""
            st.rerun()
        
        # Random motivation
        motivations = [
            "🌟 You're doing amazing!",
            "🚀 Next level awaits!",
            "💪 Consistency is key!",
            "🎯 Focus on your goals!",
            "⚡ Energy high rakho!"
        ]
        
        if st.button("💡 Daily Motivation"):
            st.success(random.choice(motivations))
    
    # Main Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Mission Control", "😊 Mood Matrix", "📖 Mind Vault", "💪 Habit Engine", "🤖 AI Companion"
    ])
    
    # Mission Control Tab
    with tab1:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Mission Control Center")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🚀 Quick Launch")
            
            if st.button("⚡ Log Mood Now", key="quick_mood"):
                st.success("Mood tracker activated! Go to Mood Matrix 😊")
            
            if st.button("📝 Quick Note", key="quick_note"):
                st.success("Mind Vault opened! Ready for input 📖")
            
            if st.button("💪 Mark Habit", key="quick_habit"):
                st.success("Habit Engine powered up! 🔥")
        
        with col2:
            st.markdown("#### 📊 System Status")
            
            # Progress bars
            total_entries = len(st.session_state.mood_entries) + len(st.session_state.chat_history)
            productivity_score = min(total_entries * 10, 100)
            
            st.markdown(f"**Productivity Score:** {productivity_score}%")
            st.progress(productivity_score / 100)
            
            engagement_score = len(st.session_state.chat_history) * 15
            engagement_score = min(engagement_score, 100)
            
            st.markdown(f"**AI Engagement:** {engagement_score}%")
            st.progress(engagement_score / 100)
        
        # Today's summary
        st.markdown("#### 📅 Today's Mission Summary")
        today = datetime.date.today()
        
        today_moods = [m for m in st.session_state.mood_entries if m.get('date', today) == today]
        today_chats = [c for c in st.session_state.chat_history[-10:] if True]  # Recent chats
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.metric("😊 Moods Today", len(today_moods), delta=1 if today_moods else 0)
        
        with col_b:
            st.metric("🤖 AI Interactions", len(today_chats), delta=2 if today_chats else 0)
        
        with col_c:
            productivity_level = "🔥 HIGH" if productivity_score > 70 else "⚡ MEDIUM" if productivity_score > 30 else "🌱 GROWING"
            st.metric("🎯 Productivity", productivity_level)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Mood Tab
    with tab2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 😊 Mood Matrix Interface")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            mood_options = [
                "😊 Happy - Positive energy flowing",
                "😢 Sad - Feeling down today", 
                "😐 Neutral - Balanced state",
                "😤 Frustrated - Things not going well",
                "🤔 Thoughtful - Deep in contemplation",
                "😴 Tired - Energy levels low",
                "🥳 Excited - High enthusiasm",
                "😰 Anxious - Feeling worried",
                "😌 Peaceful - Calm and serene",
                "🔥 Motivated - Ready to conquer"
            ]
            
            selected_mood = st.selectbox("🌈 Current Mood State:", mood_options)
            
            reason = st.text_area(
                "📝 Mission Report:",
                placeholder="What's happening in your world today? Work challenges, personal wins, random thoughts...",
                height=100
            )
            
            tags = st.text_input(
                "🏷️ Classification Tags:",
                placeholder="work, family, health, achievement, challenge"
            )
        
        with col2:
            st.markdown("#### ⚡ Intensity Levels")
            
            intensity = st.slider("🎚️ Emotional Intensity:", 1, 10, 5)
            st.caption(f"**Current Level:** {intensity}/10")
            
            energy = st.slider("⚡ Energy Level:", 1, 10, 5)
            st.caption(f"**Energy Status:** {energy}/10")
            
            # Visual feedback
            if intensity >= 8:
                st.success("🔥 HIGH INTENSITY")
            elif intensity >= 5:
                st.warning("⚡ MODERATE")
            else:
                st.info("🌱 LOW INTENSITY")
        
        # Save mood
        col_save, col_clear = st.columns([3, 1])
        
        with col_save:
            if st.button("🚀 Log to Mood Matrix", type="primary", key="log_mood"):
                if selected_mood and reason:
                    entry = {
                        "timestamp": datetime.datetime.now(),
                        "user": st.session_state.username,
                        "mood": selected_mood,
                        "reason": reason,
                        "intensity": intensity,
                        "energy": energy,
                        "tags": tags,
                        "date": datetime.date.today()
                    }
                    st.session_state.mood_entries.append(entry)
                    
                    st.success("✅ Mood successfully logged to the Matrix!")
                    st.balloons()
                    
                    # AI response based on mood
                    if intensity >= 8:
                        st.info("🌟 High intensity detected! Perfect time for challenging tasks!")
                    elif intensity <= 3:
                        st.info("💝 Low energy mode. Self-care is important today!")
                    
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("🚨 Please complete all fields!")
        
        with col_clear:
            if st.button("🗑️ Reset", key="clear_mood_form"):
                st.rerun()
        
        # Mood Analytics
        if st.session_state.mood_entries:
            st.markdown("### 📊 Mood Analytics Dashboard")
            
            # Recent moods
            recent_moods = st.session_state.mood_entries[-5:]
            
            for mood in recent_moods:
                timestamp = mood['timestamp'].strftime('%H:%M')
                st.info(f"⏰ {timestamp} | {mood['mood']} | Intensity: {mood['intensity']}/10 | Energy: {mood['energy']}/10")
            
            # Simple trend
            if len(st.session_state.mood_entries) > 1:
                avg_intensity = sum([m['intensity'] for m in st.session_state.mood_entries]) / len(st.session_state.mood_entries)
                avg_energy = sum([m['energy'] for m in st.session_state.mood_entries]) / len(st.session_state.mood_entries)
                
                col_trend1, col_trend2 = st.columns(2)
                with col_trend1:
                    st.metric("📈 Avg Intensity", f"{avg_intensity:.1f}/10")
                with col_trend2:
                    st.metric("⚡ Avg Energy", f"{avg_energy:.1f}/10")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mind Vault Tab (Journal)
    with tab3:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 📖 Mind Vault - Digital Memory Bank")
        
        # Quick note feature
        st.markdown("#### ⚡ Quick Thought Capture")
        
        quick_thought = st.text_area(
            "💭 What's on your mind?",
            placeholder="Random thoughts, ideas, reflections, learnings, goals, dreams...",
            height=150
        )
        
        col_save_thought, col_clear_thought = st.columns([2, 1])
        
        with col_save_thought:
            if st.button("💾 Save to Vault", type="primary", key="save_thought"):
                if quick_thought:
                    # Simple storage
                    if "thoughts" not in st.session_state:
                        st.session_state.thoughts = []
                    
                    thought_entry = {
                        "timestamp": datetime.datetime.now(),
                        "user": st.session_state.username,
                        "content": quick_thought,
                        "word_count": len(quick_thought.split())
                    }
                    
                    st.session_state.thoughts.append(thought_entry)
                    st.success("💾 Thought successfully archived in Mind Vault!")
                    st.balloons()
                else:
                    st.error("🚨 Please enter your thoughts!")
        
        with col_clear_thought:
            if st.button("🗑️ Clear", key="clear_thought"):
                st.rerun()
        
        # Show recent thoughts
        if "thoughts" in st.session_state and st.session_state.thoughts:
            st.markdown("### 🧠 Recent Mind Archives")
            
            for thought in st.session_state.thoughts[-3:]:
                timestamp = thought['timestamp'].strftime('%d/%m %H:%M')
                st.markdown(f"""
                **⏰ {timestamp}**  
                💭 {thought['content']}  
                📊 Words: {thought['word_count']}
                """)
                st.markdown("---")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Habit Engine Tab
    with tab4:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 💪 Habit Engine - Success Automation")
        
        # Add habit
        st.markdown("#### ⚡ Deploy New Habit")
        
        col1, col2 = st.columns(2)
        
        with col1:
            habit_name = st.text_input("💪 Habit Name:", placeholder="Daily Exercise, Reading, Meditation...")
            habit_type = st.selectbox("🎯 Category:", ["🏃 Health", "📚 Learning", "💼 Work", "🧘 Wellness"])
        
        with col2:
            frequency = st.selectbox("🔄 Target:", ["Daily", "5x/week", "3x/week"])
            
            if st.button("🚀 Activate Habit", type="primary", key="add_habit"):
                if habit_name:
                    habit = {
                        "id": len(st.session_state.habits) + 1,
                        "name": habit_name,
                        "type": habit_type,
                        "frequency": frequency,
                        "streak": 0,
                        "total": 0,
                        "last_done": None
                    }
                    st.session_state.habits.append(habit)
                    st.success(f"💪 {habit_name} activated in Habit Engine!")
                    st.balloons()
                else:
                    st.error("🚨 Please enter habit name!")
        
        # Show active habits
        if st.session_state.habits:
            st.markdown("### 🔥 Active Habit Protocols")
            
            for habit in st.session_state.habits:
                col_habit1, col_habit2, col_habit3 = st.columns([2, 1, 1])
                
                with col_habit1:
                    st.markdown(f"**💪 {habit['name']}**")
                    st.caption(f"{habit['type']} | {habit['frequency']}")
                
                with col_habit2:
                    st.metric("🔥 Streak", f"{habit['streak']} days")
                    st.metric("✅ Total", habit['total'])
                
                with col_habit3:
                    if st.button(f"✅ Complete", key=f"complete_habit_{habit['id']}"):
                        habit['total'] += 1
                        habit['streak'] += 1
                        habit['last_done'] = datetime.date.today()
                        st.success(f"🔥 {habit['name']} completed! Streak: {habit['streak']}")
                        st.rerun()
                
                # Streak visualization
                streak_visual = "🔥" * min(habit['streak'], 10)
                if habit['streak'] > 10:
                    streak_visual += f" (+{habit['streak'] - 10})"
                
                if habit['streak'] > 0:
                    st.caption(f"Streak: {streak_visual}")
                
                st.markdown("---")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # AI Companion Tab
    with tab5:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI Companion - Your Digital Mentor")
        
        # Chat interface
        if st.session_state.chat_history:
            st.markdown("### 💬 Conversation History")
            
            for i, (speaker, message, timestamp) in enumerate(st.session_state.chat_history[-6:]):
                if speaker == "You":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>👨‍🚀 {st.session_state.username}</strong> <small>({timestamp})</small><br>
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message ai-message">
                        <strong>🤖 AniGPT</strong> <small>({timestamp})</small><br>
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Chat input
        user_input = st.text_input(
            "💬 Message to AI Companion:",
            placeholder="Ask me anything! Motivation, tips, guidance, casual chat..."
        )
        
        col_send, col_clear_chat = st.columns([3, 1])
        
        with col_send:
            if st.button("🚀 Send Message", type="primary", key="send_chat"):
                if user_input:
                    ai_response = ai_chat_hinglish(user_input)
                    current_time = datetime.datetime.now().strftime("%H:%M")
                    
                    st.session_state.chat_history.append(("You", user_input, current_time))
                    st.session_state.chat_history.append(("AI", ai_response, current_time))
                    
                    # Keep last 20 messages
                    if len(st.session_state.chat_history) > 20:
                        st.session_state.chat_history = st.session_state.chat_history[-20:]
                    
                    st.rerun()
        
        with col_clear_chat:
            if st.button("🗑️ Clear Chat", key="clear_all_chat"):
                st.session_state.chat_history = []
                st.rerun()
        
        # Quick AI buttons
        st.markdown("### ⚡ Quick AI Commands")
        
        col_ai1, col_ai2, col_ai3 = st.columns(3)
        
        with col_ai1:
            if st.button("💡 Get Motivation", key="ai_motivation"):
                motivational_msg = "🌟 Aaj tumhara din amazing hoga! Har challenge ek opportunity hai growth ki. Keep pushing forward! 🚀"
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", motivational_msg, current_time))
                st.rerun()
        
        with col_ai2:
            if st.button("📊 Show Stats", key="ai_stats"):
                stats_msg = f"""
                🎯 Mission Status Report:
                • Mood Logs: {len(st.session_state.mood_entries)}
                • Active Habits: {len(st.session_state.habits)}
                • Mind Vault Entries: {len(st.session_state.get('thoughts', []))}
                • AI Conversations: {len(st.session_state.chat_history)}
                
                Performance: Excellent! Keep growing! 🚀
                """
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", stats_msg, current_time))
                st.rerun()
        
        with col_ai3:
            if st.button("🎯 Daily Goal", key="ai_goal"):
                goal_msg = "🎯 Today's Mission: Complete one habit, log your mood, and write one meaningful thought in Mind Vault. Small actions, big results! 💪"
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", goal_msg, current_time))
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Futuristic Footer
    st.markdown("---")
    st.markdown("""
    <div style="
        text-align: center;
        padding: 30px;
        background: rgba(255,255,255,0.02);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 30px 0;
        backdrop-filter: blur(15px);
    ">
        <h3 style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🚀 AniGPT V2 - COMMAND CENTER ACTIVE
        </h3>
        <p style="color: rgba(255,255,255,0.8); font-family: 'Orbitron', monospace;">
            PRODUCTIVITY • GROWTH • ACHIEVEMENT • SUCCESS
        </p>
        <p style="color: rgba(255,255,255,0.6); font-size: 14px;">
            Mission Commander: {st.session_state.username} | Status: OPERATIONAL 🟢
        </p>
        <p style="color: rgba(255,255,255,0.5); font-size: 12px;">
            Made with 🤖 AI Technology | Keep Conquering! 🎯
        </p>
    </div>
    """, unsafe_allow_html=True)
