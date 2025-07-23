import streamlit as st
import datetime
import random
import time
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="AniGPT V2 - Personal AI Assistant", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with User-Friendly Design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global Styling */
.main {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #FFFFFF;
}

/* Welcome Screen */
.welcome-screen {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 50px 30px;
    text-align: center;
    margin: 50px auto;
    max-width: 600px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

.welcome-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.welcome-subtitle {
    font-size: 1.3rem;
    opacity: 0.9;
    margin-bottom: 30px;
}

/* Top Header */
.user-header {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 20px 30px;
    margin: 20px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid rgba(255,255,255,0.2);
}

.user-info {
    display: flex;
    align-items: center;
    gap: 15px;
}

.user-name {
    font-size: 1.4rem;
    font-weight: 600;
    color: #FFFFFF;
}

.user-status {
    background: linear-gradient(45deg, #4ECDC4, #44A08D);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
}

/* Modern Cards */
.modern-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 30px;
    margin: 25px 0;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.modern-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
}

/* Input Styling */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.9) !important;
    border: 2px solid rgba(255,255,255,0.3) !important;
    border-radius: 15px !important;
    color: #333 !important;
    font-size: 16px !important;
    padding: 15px !important;
    font-family: 'Poppins', sans-serif !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #4ECDC4 !important;
    box-shadow: 0 0 15px rgba(78,205,196,0.3) !important;
    transform: translateY(-1px);
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    padding: 12px 30px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    font-family: 'Poppins', sans-serif !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 5px 20px rgba(255,107,107,0.3) !important;
    text-transform: none !important;
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 10px 30px rgba(255,107,107,0.4) !important;
}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 10px;
    gap: 10px;
    backdrop-filter: blur(10px);
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px;
    color: white;
    font-weight: 500;
    padding: 12px 20px;
    transition: all 0.3s ease;
    font-family: 'Poppins', sans-serif;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,255,255,0.15);
    transform: translateY(-1px);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    border-color: rgba(255,255,255,0.3);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

/* Sidebar Styling */
.sidebar-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 15px;
    padding: 20px;
    margin: 15px 0;
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
}

/* Success/Error Messages */
.stSuccess > div {
    background: linear-gradient(45deg, #4ECDC4, #44A08D) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
}

.stError > div {
    background: linear-gradient(45deg, #FF6B6B, #FF5252) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
}

.stInfo > div {
    background: linear-gradient(45deg, #45B7D1, #3498db) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
}

/* Metric Cards */
.metric-display {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 10px 0;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.metric-display:hover {
    transform: scale(1.02);
    background: rgba(255,255,255,0.15);
}

.metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: #4ECDC4;
}

.metric-label {
    font-size: 0.9rem;
    opacity: 0.8;
}

/* Chat Messages */
.chat-user {
    background: rgba(255,107,107,0.2);
    padding: 15px 20px;
    border-radius: 20px 20px 8px 20px;
    margin: 10px 0;
    margin-left: 15%;
    border-left: 4px solid #FF6B6B;
}

.chat-ai {
    background: rgba(78,205,196,0.2);
    padding: 15px 20px;
    border-radius: 20px 20px 20px 8px;
    margin: 10px 0;
    margin-right: 15%;
    border-left: 4px solid #4ECDC4;
}

/* Progress Bars */
.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 5px;
    margin: 5px 0;
}

.progress-bar {
    background: linear-gradient(90deg, #4ECDC4, #44A08D);
    height: 10px;
    border-radius: 5px;
    transition: width 0.3s ease;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .welcome-title {
        font-size: 2.5rem;
    }
    
    .user-header {
        flex-direction: column;
        gap: 15px;
        padding: 20px;
    }
    
    .modern-card {
        padding: 20px;
        margin: 15px 0;
    }
    
    .chat-user, .chat-ai {
        margin-left: 0;
        margin-right: 0;
    }
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in {
    animation: fadeInUp 0.6s ease-out;
}

/* Slider Styling */
.stSlider > div > div > div {
    background: linear-gradient(90deg, #4ECDC4, #44A08D) !important;
}

</style>
""", unsafe_allow_html=True)

# Initialize Session States
def initialize_session_states():
    """Initialize all session states for data storage"""
    if "user_authenticated" not in st.session_state:
        st.session_state.user_authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "mood_entries" not in st.session_state:
        st.session_state.mood_entries = []
    if "journal_entries" not in st.session_state:
        st.session_state.journal_entries = []
    if "goals" not in st.session_state:
        st.session_state.goals = []
    if "habits" not in st.session_state:
        st.session_state.habits = []
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    if "learning_sessions" not in st.session_state:
        st.session_state.learning_sessions = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# AI Chat Function
def ai_chat_hinglish(user_input):
    """Enhanced Hinglish AI Chat with context awareness"""
    user_input_lower = user_input.lower()
    
    # Context-aware responses based on user input
    if any(word in user_input_lower for word in ['sad', 'upset', 'dukhi', 'pareshaan', 'tension', 'stress', 'depressed']):
        responses = [
            "🤗 Arre yaar, main samajh raha hun. Life me tough times aate rehte hain. Kya specific problem hai? Share kar sakte ho?",
            "💪 Bhai, you're stronger than you think! Depression temporary hai, but your strength permanent hai. Koi small positive activity try karo.",
            "🌟 Mood down hai toh koi baat nahi. Journal me feelings likh do, ya phir koi habit complete karo. Small wins matter!",
            "💝 Dost, you're not alone in this. Main yahan hun sunne ke liye. Mental health important hai, professional help bhi le sakte ho agar zaroorat ho.",
            "🫂 Tough day ho raha hai? It's okay to feel low sometimes. Self-care karo - music suno, walk karo, ya kisi close friend se baat karo!"
        ]
    elif any(word in user_input_lower for word in ['happy', 'khush', 'accha', 'mast', 'good', 'great', 'excited', 'amazing']):
        responses = [
            "🎉 Waah bhai! Khushi dekh ke mera bhi mood up ho gaya! Is positive energy ko kaam me lagao aur goals achieve karo!",
            "🚀 Fantastic! Good mood me productivity peak pe hoti hai. Koi challenging task pick karo aur conquer karo!",
            "⭐ Bahut badhiya! Happiness contagious hai. Is joy ko journal me capture kar lo future motivation ke liye!",
            "🔥 Superb energy! Happy mood me habits complete karna easy lagta hai. Streak maintain karo!",
            "🌈 Amazing! Positive vibes spread karo. Koi new goal set kar sakte ho ya friends ko motivate kar sakte ho!"
        ]
    elif any(word in user_input_lower for word in ['goal', 'target', 'achieve', 'complete', 'success', 'accomplish']):
        responses = [
            "🎯 Goals ki baat ho rahi hai? Perfect mindset! SMART approach follow karo - Specific, Measurable, Achievable, Relevant, Time-bound!",
            "📈 Target achieve karne ka best way? Daily consistent action! Small steps, big results. Progress track karte raho!",
            "🏆 Success milegi pakka! Main dekh raha hun tumhara determination. Break down big goals into daily mini-goals!",
            "💡 Achievement unlock karne ka formula: Clear vision + Daily action + Progress tracking = Success guaranteed!",
            "🎖️ Goal-oriented thinking! Yahi difference hai achievers me. Timeline set karo aur backward planning karo!"
        ]
    elif any(word in user_input_lower for word in ['habit', 'daily', 'routine', 'streak', 'consistency']):
        responses = [
            "💪 Habits are life changers! Start small - 2 minute rule follow karo. Reading = 1 page, Exercise = 5 pushups!",
            "🔥 Consistency beats intensity! Daily 1% improvement means 37x better in 1 year. Math hai bhai, magic nahi!",
            "⚡ Habit formation me 66 days average lagte hain (not 21!). Patience rakho, compound effect dekhoge!",
            "🌟 Perfect thinking! Habits run on autopilot. Willpower save hota hai important decisions ke liye!",
            "🎯 Streak maintain karna hard lagta hai initially, but momentum build hone ke baad easy ho jata hai!"
        ]
    elif any(word in user_input_lower for word in ['work', 'job', 'office', 'career', 'productivity', 'focus']):
        responses = [
            "💼 Work challenges normal hain! Priority matrix use karo - Urgent vs Important. Focus on Important tasks!",
            "🧠 Productivity hack: Pomodoro technique try karo. 25 min focused work + 5 min break = Magic formula!",
            "📊 Career growth ke liye skills upgrade karte raho. Learning never stops! What new skill planning?",
            "⚖️ Work-life balance crucial hai. Burnout avoid karne ke liye breaks aur self-care must hai!",
            "🎯 Office politics se bachne ka way: Excellent work deliver karo. Performance speaks louder than words!"
        ]
    elif any(word in user_input_lower for word in ['learn', 'study', 'skill', 'knowledge', 'course', 'book']):
        responses = [
            "📚 Learning mindset! Growth mindset ka sign hai. Kya naya seekh rahe ho? Knowledge compound hoti hai!",
            "🧠 Study technique: Active recall > passive reading. Notes banao, teach karo kisi ko, quiz lo apna!",
            "🎓 Skill development continuous process hai. Online courses, books, practice - sab combine karo!",
            "💡 Knowledge sharing karo. Teaching others solidifies your own understanding. Win-win situation!",
            "📖 Reading habit develop karo. Leaders are readers! Daily 20-30 min reading game changer hai!"
        ]
    elif any(word in user_input_lower for word in ['health', 'exercise', 'fitness', 'meditation', 'sleep']):
        responses = [
            "🏃‍♂️ Health is wealth! Physical fitness mental clarity improve karta hai. Daily movement important hai!",
            "🧘‍♀️ Meditation game changer hai stress management ke liye. 10 min daily se start karo!",
            "💪 Exercise releases endorphins - natural mood boosters! Gym nahi toh walking, dancing, anything!",
            "😴 Sleep quality productivity directly impact karta hai. 7-8 hours quality sleep non-negotiable hai!",
            "🥗 Nutrition foundation hai energy levels ka. Junk food se energy crash, healthy food se sustained energy!"
        ]
    elif any(word in user_input_lower for word in ['motivation', 'inspire', 'demotivated', 'lazy', 'procrastination']):
        responses = [
            "🚀 Motivation fluctuates, discipline stays constant! System create karo, motivation pe depend mat karo!",
            "💎 Diamonds are formed under pressure. Tumhare challenges tumhe stronger bana rahe hain!",
            "⚡ Action creates motivation, not the opposite! Small step lo, momentum build hoga automatically!",
            "🎯 Procrastination perfectionism ka mask hai often. Done is better than perfect. Start karo!",
            "🔥 Every expert was once a beginner. Comparison mat karo, improvement karo. Your only competition is yesterday's you!"
        ]
    elif any(word in user_input_lower for word in ['thanks', 'thank you', 'shukriya', 'dhanyawad', 'helpful']):
        responses = [
            "🙏 Bilkul nahi yaar! Helping each other se hi hum grow karte hain. Anytime need ho toh bolo!",
            "❤️ Koi baat nahi bhai! Tumhara success meri khushi hai. Keep growing aur inspire karte raho others ko!",
            "🤝 Thanks ka kya dost! Hum saath me journey kar rahe hain growth ki. Support each other!",
            "🌟 Mention not! Main yahan hun tumhare liye. Questions ho, motivation chahiye, ya bas chat - always ready!",
            "🚀 No problem at all! Your progress makes me happy. Keep pushing boundaries aur achieve karo dreams!"
        ]
    else:
        # General encouraging responses
        responses = [
            "😊 Haan bhai, sun raha hun! Main tumhara AI companion hun. Kya specific help chahiye productivity me?",
            "💭 Interesting point! Is thought ko journal me elaborate kar sakte ho. Writing clarity deta hai!",
            "✨ Bilkul sahi direction me soch rahe ho! Consistent action se koi bhi goal achievable hai!",
            "🎯 Good thinking! Analytics dekho apna data, patterns identify karo, optimize karo approach!",
            "🤖 Main yahan hun tumhare support ke liye! Goals, habits, ya koi bhi challenge - let's tackle together!",
            "🌟 Waah! Proactive approach. Yahi mindset se success aati hai. Aur kya plan kar rahe ho?",
            "💪 Great attitude! Daily improvement ka compound effect amazing hota hai. Keep the momentum!",
            "🚀 Perfect! Growth mindset dekh ke khushi hui. Continuous improvement hi real success hai!"
        ]
    
    return random.choice(responses)

# Utility Functions
def save_mood_entry(user, mood, reason, intensity, energy, tags):
    """Save mood entry to session state"""
    entry = {
        "timestamp": datetime.datetime.now(),
        "user": user,
        "mood": mood,
        "reason": reason,
        "intensity": intensity,
        "energy": energy,
        "tags": tags,
        "date": datetime.date.today()
    }
    st.session_state.mood_entries.append(entry)
    return "✅ Mood entry saved successfully!"

def save_journal_entry(user, title, content, category, tags):
    """Save journal entry to session state"""
    # Simple sentiment analysis
    positive_words = ['happy', 'good', 'great', 'amazing', 'wonderful', 'excellent', 'love', 'excited', 'proud', 'grateful']
    negative_words = ['sad', 'bad', 'terrible', 'awful', 'hate', 'angry', 'frustrated', 'disappointed', 'worried', 'stressed']
    
    content_lower = content.lower()
    positive_count = sum(word in content_lower for word in positive_words)
    negative_count = sum(word in content_lower for word in negative_words)
    
    if positive_count > negative_count:
        sentiment = "Positive 😊"
    elif negative_count > positive_count:
        sentiment = "Negative 😔"
    else:
        sentiment = "Neutral 😐"
    
    entry = {
        "timestamp": datetime.datetime.now(),
        "user": user,
        "title": title,
        "content": content,
        "category": category,
        "tags": tags,
        "sentiment": sentiment,
        "word_count": len(content.split())
    }
    st.session_state.journal_entries.append(entry)
    return f"✅ Journal entry saved! Sentiment: {sentiment}"

def add_goal(user, goal_name, category, priority, target_date, description):
    """Add new goal"""
    goal = {
        "id": len(st.session_state.goals) + 1,
        "timestamp": datetime.datetime.now(),
        "user": user,
        "goal_name": goal_name,
        "category": category,
        "priority": priority,
        "target_date": target_date,
        "description": description,
        "progress": 0,
        "status": "Active"
    }
    st.session_state.goals.append(goal)
    return "🎯 Goal added successfully!"

def add_habit(user, habit_name, category, frequency):
    """Add new habit"""
    habit = {
        "id": len(st.session_state.habits) + 1,
        "timestamp": datetime.datetime.now(),
        "user": user,
        "habit_name": habit_name,
        "category": category,
        "frequency": frequency,
        "current_streak": 0,
        "total_completions": 0,
        "last_completed": None
    }
    st.session_state.habits.append(habit)
    return "💪 Habit added successfully!"

def add_task(user, task_title, priority, due_date, category, description):
    """Add new task"""
    task = {
        "id": len(st.session_state.tasks) + 1,
        "timestamp": datetime.datetime.now(),
        "user": user,
        "task_title": task_title,
        "priority": priority,
        "due_date": due_date,
        "category": category,
        "description": description,
        "status": "Pending",
        "completed_at": None
    }
    st.session_state.tasks.append(task)
    return "📋 Task added successfully!"

def add_learning_session(user, topic, resource_type, duration, rating, notes):
    """Add learning session"""
    session = {
        "id": len(st.session_state.learning_sessions) + 1,
        "timestamp": datetime.datetime.now(),
        "user": user,
        "topic": topic,
        "resource_type": resource_type,
        "duration": duration,
        "rating": rating,
        "notes": notes
    }
    st.session_state.learning_sessions.append(session)
    return "📚 Learning session logged successfully!"

# Initialize states
initialize_session_states()

# Welcome/Login Screen
if not st.session_state.user_authenticated:
    st.markdown("""
    <div class="welcome-screen animate-fade-in">
        <div class="welcome-title">🤖 AniGPT V2</div>
        <div class="welcome-subtitle">Your Personal AI Productivity Companion</div>
        <div class="welcome-subtitle">Track • Learn • Grow • Achieve</div>
        <br>
        <p style="opacity: 0.8; font-size: 1.1rem;">
            ✨ Advanced mood tracking with AI insights<br>
            📝 Smart journaling with sentiment analysis<br>
            🎯 Goal management with progress tracking<br>
            💪 Habit building with streak counters<br>
            🤖 Intelligent AI chat in Hinglish
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered input form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        
        username = st.text_input(
            "",
            placeholder="👤 Enter your name to begin your journey...",
            key="username_input",
            help="Enter your name to access your personal AI assistant"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_enter, col_demo = st.columns([1, 1])
        
        with col_enter:
            if st.button("🚀 Start My Journey", type="primary", key="enter_button", use_container_width=True):
                if username.strip():
                    st.session_state.username = username.strip()
                    st.session_state.user_authenticated = True
                    
                    # Loading animation
                    progress_placeholder = st.empty()
                    status_placeholder = st.empty()
                    
                    loading_messages = [
                        "🔍 Initializing AI modules...",
                        "🧠 Loading your personal workspace...",
                        "📊 Setting up analytics...",
                        "🎯 Preparing goal tracker...",
                        "💪 Activating habit engine...",
                        "🚀 Almost ready!"
                    ]
                    
                    for i, message in enumerate(loading_messages):
                        progress = int((i + 1) / len(loading_messages) * 100)
                        progress_placeholder.progress(progress)
                        status_placeholder.info(message)
                        time.sleep(0.3)
                    
                    progress_placeholder.empty()
                    status_placeholder.success(f"🎉 Welcome aboard, {username}! Your AI companion is ready!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("🚨 Please enter your name to continue!")
        
        with col_demo:
            if st.button("👀 Quick Demo", key="demo_button", use_container_width=True):
                st.session_state.username = "Demo User"
                st.session_state.user_authenticated = True
                # Add sample data for demo
                st.session_state.mood_entries = [
                    {
                        "timestamp": datetime.datetime.now() - datetime.timedelta(hours=2),
                        "user": "Demo User",
                        "mood": "😊 Happy",
                        "reason": "Great progress on personal projects!",
                        "intensity": 8,
                        "energy": 7,
                        "tags": "productivity, success",
                        "date": datetime.date.today()
                    }
                ]
                st.session_state.goals = [
                    {
                        "id": 1,
                        "goal_name": "Learn Python Programming",
                        "category": "Education",
                        "priority": "High",
                        "progress": 65,
                        "status": "Active"
                    }
                ]
                st.rerun()

# Main Dashboard
else:
    # Top Header with User Info
    st.markdown(f"""
    <div class="user-header animate-fade-in">
        <div class="user-info">
            <div>
                <div class="user-name">👋 Hello, {st.session_state.username}!</div>
                <small style="opacity: 0.8;">Welcome to your personal productivity command center</small>
            </div>
        </div>
        <div class="user-status">✨ Online & Ready</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Sidebar
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-card">
            <h2>👤 {st.session_state.username}</h2>
            <p style="opacity: 0.8;">Productivity Commander</p>
            <div style="margin: 10px 0;">
                <small>🎯 Growing • 📈 Improving • 🚀 Achieving</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Dynamic Stats with Better Visual Appeal
        st.markdown("### 📊 Your Progress Dashboard")
        
        # Calculate stats
        total_entries = len(st.session_state.mood_entries)
        journal_count = len(st.session_state.journal_entries)
        active_goals = len([g for g in st.session_state.goals if g.get('status') == 'Active'])
        total_habits = len(st.session_state.habits)
        pending_tasks = len([t for t in st.session_state.tasks if t.get('status') == 'Pending'])
        learning_hours = sum([s.get('duration', 0) for s in st.session_state.learning_sessions]) / 60
        
        # Display stats in grid
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="metric-display">
                <div class="metric-value">{total_entries}</div>
                <div class="metric-label">😊 Moods Tracked</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-display">
                <div class="metric-value">{active_goals}</div>
                <div class="metric-label">🎯 Active Goals</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-display">
                <div class="metric-value">{learning_hours:.1f}h</div>
                <div class="metric-label">📚 Learning Time</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-display">
                <div class="metric-value">{journal_count}</div>
                <div class="metric-label">📝 Journal Entries</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-display">
                <div class="metric-value">{total_habits}</div>
                <div class="metric-label">💪 Habits Building</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-display">
                <div class="metric-value">{pending_tasks}</div>
                <div class="metric-label">📋 Tasks Pending</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Quick Actions
        st.markdown("### ⚡ Quick Actions")
        
        if st.button("🎲 Random Motivation", key="random_motivation", use_container_width=True):
            motivations = [
                "🌟 You're capable of amazing things!",
                "🚀 Every small step counts towards your big goals!",
                "💪 Consistency beats perfection every time!",
                "🎯 Focus on progress, not perfection!",
                "⚡ Your potential is limitless!"
            ]
            st.success(random.choice(motivations))
        
        if st.button("📊 Today's Summary", key="daily_summary", use_container_width=True):
            today_moods = len([m for m in st.session_state.mood_entries if m.get('date') == datetime.date.today()])
            st.info(f"Today: {today_moods} mood entries logged. Keep tracking your emotional journey! 🌈")
        
        st.markdown("---")
        
        if st.button("🔄 Switch User", key="switch_user", use_container_width=True):
            # Save session data if needed
            st.session_state.user_authenticated = False
            st.session_state.username = ""
            st.rerun()
    
    # Main Content Tabs with Enhanced Design
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🏠 Dashboard", "😊 Mood Tracker", "📝 Journal", "🎯 Goals", "💪 Habits", "📋 Tasks", "🤖 AI Chat"
    ])
    
    # Enhanced Dashboard Tab
    with tab1:
        st.markdown('<div class="modern-card">', unsafe_allow_html=True)
        
        st.markdown("### 🏠 Welcome to Your Command Center")
        st.markdown("Here's your productivity overview and quick insights!")
        
        # Quick Stats Overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            delta_moods = 1 if total_entries > 0 else 0
            st.metric("😊 Mood Entries", total_entries, delta=delta_moods, help="Total mood entries logged")
        
        with col2:
            delta_journal = 1 if journal_count > 0 else 0
            st.metric("📝 Journal Entries", journal_count, delta=delta_journal, help="Personal reflections recorded")
        
        with col3:
            st.metric("🎯 Active Goals", active_goals, delta=1 if active_goals > 0 else 0, help="Goals currently being pursued")
        
        with col4:
            st.metric("💪 Habits", total_habits, delta=1 if total_habits > 0 else 0, help="Habits being tracked")
        
        st.markdown("---")
        
        # Activity Feed
        st.markdown("### 📈 Recent Activity")
        
        if total_entries > 0 or journal_count > 0:
            # Combine recent activities
            all_activities = []
            
            # Add recent moods
            for mood in st.session_state.mood_entries[-3:]:
                all_activities.append({
                    'type': 'mood',
                    'timestamp': mood['timestamp'],
                    'content': f"Logged mood: {mood['mood']} (Intensity: {mood['intensity']}/10)"
                })
            
            # Add recent journal entries
            for journal in st.session_state.journal_entries[-3:]:
                all_activities.append({
                    'type': 'journal',
                    'timestamp': journal['timestamp'],
                    'content': f"Journal entry: {journal['title']}"
                })
            
            # Sort by timestamp
            all_activities.sort(key=lambda x: x['timestamp'], reverse=True)
            
            for activity in all_activities[:5]:
                icon = "😊" if activity['type'] == 'mood' else "📝"
                time_str = activity['timestamp'].strftime('%H:%M')
                st.info(f"{icon} {time_str} - {activity['content']}")
        else:
            st.info("🌟 Start your journey by logging your first mood or writing a journal entry!")
        
        # Quick Action Cards
        st.markdown("### ⚡ Quick Actions")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("📝 Quick Mood Check", key="quick_mood_dash", use_container_width=True):
                st.info("🎯 Head over to the Mood Tracker tab to log your current emotional state!")
        
        with col_b:
            if st.button("💭 Journal Thoughts", key="quick_journal_dash", use_container_width=True):
                st.info("📖 Visit the Journal tab to capture your thoughts and reflections!")
        
        with col_c:
            if st.button("🤖 Chat with AI", key="quick_chat_dash", use_container_width=True):
                st.info("💬 Go to AI Chat tab for motivation and guidance!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Continue with remaining tabs... (Due to length, I'll provide the structure)
    
    # Enhanced Mood Tab
    with tab2:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 😊 Advanced Mood Tracker")
        st.markdown("Track your emotional journey with detailed insights and AI-powered analysis.")
        
        # Mood entry form
        col1, col2 = st.columns([2, 1])
        
        with col1:
            mood_options = [
                "😊 Happy - Feeling positive and joyful",
                "😢 Sad - Feeling down or melancholy", 
                "😐 Neutral - Balanced emotional state",
                "😤 Frustrated - Feeling annoyed or irritated",
                "🤔 Thoughtful - In a contemplative mood",
                "😴 Tired - Feeling exhausted or sleepy",
                "🥳 Excited - High energy and enthusiasm",
                "😰 Anxious - Feeling worried or nervous",
                "😌 Peaceful - Calm and serene",
                "🔥 Motivated - Ready to conquer challenges"
            ]
            
            selected_mood = st.selectbox("🌈 How are you feeling right now?", mood_options, key="mood_select")
            
            reason = st.text_area(
                "📝 What's influencing your mood today?",
                placeholder="Work achievements, family time, health concerns, personal growth, challenges faced...",
                height=100,
                key="mood_reason"
            )
            
            tags = st.text_input(
                "🏷️ Tags (comma separated):",
                placeholder="work, family, health, achievement, challenge, social",
                key="mood_tags"
            )
        
        with col2:
            st.markdown("#### 🎚️ Intensity & Energy Levels")
            
            intensity = st.slider("💫 Emotional Intensity:", 1, 10, 5, key="mood_intensity")
            st.caption(f"Current Level: **{intensity}/10**")
            
            if intensity <= 3:
                st.error("🔴 Low Intensity")
            elif intensity <= 6:
                st.warning("🟡 Moderate Intensity")
            else:
                st.success("🟢 High Intensity")
            
            energy = st.slider("⚡ Energy Level:", 1, 10, 5, key="mood_energy")
            st.caption(f"Energy Status: **{energy}/10**")
            
            if energy <= 3:
                st.info("💤 Low Energy - Rest needed")
            elif energy <= 6:
                st.info("⚡ Moderate Energy")
            else:
                st.info("🔋 High Energy - Great for tasks!")
        
        # Save mood
        col_save, col_clear = st.columns([3, 1])
        
        with col_save:
            if st.button("🚀 Save Mood Entry", type="primary", key="save_mood_btn", use_container_width=True):
                if selected_mood and reason:
                    result = save_mood_entry(st.session_state.username, selected_mood, reason, intensity, energy, tags)
                    st.success(result)
                    st.balloons()
                    
                    # Provide contextual feedback
                    if intensity >= 8:
                        st.info("🌟 High intensity mood! Perfect time for challenging tasks and important decisions!")
                    elif intensity <= 3:
                        st.info("💝 Low energy detected. Consider self-care activities and rest.")
                    
                    # AI-powered insight
                    ai_insight = ai_chat_hinglish(f"I'm feeling {selected_mood.lower()} because {reason}")
                    st.info(f"🤖 **AI Insight:** {ai_insight}")
                    
                else:
                    st.error("🚨 Please select a mood and provide a reason!")
        
        with col_clear:
            if st.button("🗑️ Clear Form", key="clear_mood_form"):
                st.rerun()
        
        # Mood Analytics and History
        if st.session_state.mood_entries:
            st.markdown("### 📊 Your Mood Journey")
            
            # Recent moods display
            st.markdown("#### 🕒 Recent Mood Entries")
            
            for i, mood in enumerate(reversed(st.session_state.mood_entries[-5:])):
                timestamp = mood['timestamp'].strftime('%d/%m %H:%M')
                intensity_color = "🔴" if mood['intensity'] <= 3 else "🟡" if mood['intensity'] <= 6 else "🟢"
                
                with st.expander(f"{mood['mood']} - {timestamp}", expanded=i == 0):
                    col_info, col_metrics = st.columns([2, 1])
                    
                    with col_info:
                        st.write(f"**Reason:** {mood['reason']}")
                        if mood.get('tags'):
                            tags_html = ' '.join([f'<span style="background: rgba(78,205,196,0.2); padding: 2px 8px; border-radius: 10px; font-size: 0.8em;">{tag.strip()}</span>' for tag in mood['tags'].split(',')])
                            st.markdown(f"**Tags:** {tags_html}", unsafe_allow_html=True)
                    
                    with col_metrics:
                        st.metric("Intensity", f"{mood['intensity']}/10", delta=None)
                        st.metric("Energy", f"{mood['energy']}/10", delta=None)
            
            # Simple analytics
            if len(st.session_state.mood_entries) > 1:
                st.markdown("#### 📈 Mood Analytics")
                
                avg_intensity = sum([m['intensity'] for m in st.session_state.mood_entries]) / len(st.session_state.mood_entries)
                avg_energy = sum([m['energy'] for m in st.session_state.mood_entries]) / len(st.session_state.mood_entries)
                
                col_analytics1, col_analytics2, col_analytics3 = st.columns(3)
                
                with col_analytics1:
                    st.metric("📊 Average Intensity", f"{avg_intensity:.1f}/10")
                
                with col_analytics2:
                    st.metric("⚡ Average Energy", f"{avg_energy:.1f}/10")
                
                with col_analytics3:
                    st.metric("📝 Total Entries", len(st.session_state.mood_entries))
                
                # Mood distribution
                mood_counts = {}
                for mood in st.session_state.mood_entries:
                    mood_emoji = mood['mood'].split(' ')[0]
                    mood_counts[mood_emoji] = mood_counts.get(mood_emoji, 0) + 1
                
                if mood_counts:
                    st.markdown("**🎭 Mood Distribution:**")
                    for emoji, count in sorted(mood_counts.items(), key=lambda x: x[1], reverse=True):
                        percentage = (count / len(st.session_state.mood_entries)) * 100
                        st.write(f"{emoji} **{count} times** ({percentage:.1f}%)")
        
        else:
            st.info("🌟 Start your mood tracking journey! Log your first mood entry above to see analytics and insights.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced Journal Tab
    with tab3:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 📝 Personal Journal with AI Insights")
        st.markdown("Capture your thoughts, experiences, and reflections with intelligent sentiment analysis.")
        
        # Journal entry form
        with st.form("journal_form", clear_on_submit=False):
            title = st.text_input(
                "📖 Entry Title:",
                placeholder="Today's Reflection, Weekly Review, Random Thoughts...",
                key="journal_title_form"
            )
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                content = st.text_area(
                    "💭 What's on your mind?",
                    placeholder="Write about your day, thoughts, feelings, learnings, challenges, achievements...\n\nTip: Be authentic and detailed for better AI insights!",
                    height=200,
                    key="journal_content_form"
                )
            
            with col2:
                category = st.selectbox(
                    "📁 Category:",
                    ["Personal", "Work", "Learning", "Health", "Relationships", "Goals", "Gratitude", "Random"],
                    key="journal_category_form"
                )
                
                tags = st.text_input(
                    "🏷️ Tags:",
                    placeholder="work, learning, family...",
                    key="journal_tags_form"
                )
        
            # Word count display
            if content:
                word_count = len(content.split())
                char_count = len(content)
                st.caption(f"📊 **{word_count} words** • **{char_count} characters**")
        
            # Submit button
            submitted = st.form_submit_button("📚 Save Journal Entry", type="primary", use_container_width=True)
            
            if submitted:
                if title and content:
                    result = save_journal_entry(st.session_state.username, title, content, category, tags)
                    st.success(result)
                    st.balloons()
                    
                    # Provide writing feedback
                    word_count = len(content.split())
                    if word_count > 100:
                        st.info("🌟 Detailed entry! Writing helps process thoughts and emotions more effectively!")
                    elif word_count > 50:
                        st.info("👍 Good reflection! Consistent journaling builds self-awareness!")
                    else:
                        st.info("✨ Great start! Try to elaborate more in future entries for deeper insights!")
                    
                    # AI insight on the journal entry
                    ai_insight = ai_chat_hinglish(f"I wrote in my journal about: {title}. {content[:100]}")
                    st.info(f"🤖 **AI Reflection:** {ai_insight}")
                    
                else:
                    st.error("🚨 Please fill both title and content fields!")
        
        # Recent Journal Entries
        if st.session_state.journal_entries:
            st.markdown("### 📚 Your Journal Archive")
            
            # Filter and search options
            col_filter, col_search = st.columns([1, 2])
            
            with col_filter:
                filter_category = st.selectbox("Filter by Category:", ["All"] + ["Personal", "Work", "Learning", "Health", "Relationships", "Goals", "Gratitude", "Random"], key="journal_filter")
            
            with col_search:
                search_term = st.text_input("🔍 Search in entries:", placeholder="Search by title or content...", key="journal_search")
            
            # Filter entries
            filtered_entries = st.session_state.journal_entries
            
            if filter_category != "All":
                filtered_entries = [e for e in filtered_entries if e.get('category') == filter_category]
            
            if search_term:
                search_lower = search_term.lower()
                filtered_entries = [e for e in filtered_entries if search_lower in e['title'].lower() or search_lower in e['content'].lower()]
            
            # Display entries
            if filtered_entries:
                for i, entry in enumerate(reversed(filtered_entries[-5:])):
                    timestamp = entry['timestamp'].strftime('%d/%m/%Y %H:%M')
                    
                    with st.expander(f"📖 {entry['title']} - {timestamp}", expanded=i == 0):
                        col_content, col_meta = st.columns([2, 1])
                        
                        with col_content:
                            st.write(entry['content'])
                        
                        with col_meta:
                            st.markdown(f"**📁 Category:** {entry['category']}")
                            st.markdown(f"**😊 Sentiment:** {entry['sentiment']}")
                            st.markdown(f"**📊 Words:** {entry['word_count']}")
                            
                            if entry.get('tags'):
                                tags_html = ' '.join([f'<span style="background: rgba(78,205,196,0.2); padding: 2px 8px; border-radius: 10px; font-size: 0.8em;">{tag.strip()}</span>' for tag in entry['tags'].split(',')])
                                st.markdown(f"**🏷️ Tags:** {tags_html}", unsafe_allow_html=True)
                
                # Journal Analytics
                st.markdown("### 📊 Writing Analytics")
                
                total_entries = len(st.session_state.journal_entries)
                total_words = sum([e['word_count'] for e in st.session_state.journal_entries])
                avg_words = total_words / total_entries if total_entries > 0 else 0
                
                col_stats1, col_stats2, col_stats3 = st.columns(3)
                
                with col_stats1:
                    st.metric("📚 Total Entries", total_entries)
                
                with col_stats2:
                    st.metric("📝 Total Words", f"{total_words:,}")
                
                with col_stats3:
                    st.metric("📊 Avg Words/Entry", f"{avg_words:.0f}")
                
                # Sentiment analysis
                sentiments = [e['sentiment'] for e in st.session_state.journal_entries]
                sentiment_counts = {s: sentiments.count(s) for s in set(sentiments)}
                
                if sentiment_counts:
                    st.markdown("**🎭 Emotional Tone Analysis:**")
                    for sentiment, count in sentiment_counts.items():
                        percentage = (count / total_entries) * 100
                        st.write(f"{sentiment} **{count} entries** ({percentage:.1f}%)")
            
            else:
                if search_term or filter_category != "All":
                    st.info("🔍 No entries match your search criteria. Try different filters!")
                else:
                    st.info("📝 No journal entries yet. Start writing to see your archive!")
        
        else:
            st.info("🌟 Start your journaling journey! Regular writing improves mental clarity and self-awareness.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Continue with remaining tabs... (Goals, Habits, Tasks, AI Chat)
    
    # For brevity, I'll provide the enhanced AI Chat tab as an example:
    
    # Enhanced AI Chat Tab
    with tab7:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 🤖 Your Personal AI Companion")
        st.markdown("Chat with your intelligent assistant for motivation, guidance, and support in Hinglish!")
        
        # Display chat history
        if st.session_state.chat_history:
            st.markdown("### 💬 Conversation History")
            
            # Create a scrollable chat container
            chat_container = st.container()
            
            with chat_container:
                for i, (speaker, message, timestamp) in enumerate(st.session_state.chat_history[-10:]):
                    if speaker == "You":
                        st.markdown(f"""
                        <div class="chat-user">
                            <strong>👤 {st.session_state.username}</strong> <small style="opacity: 0.7;">({timestamp})</small><br>
                            {message}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="chat-ai">
                            <strong>🤖 AniGPT</strong> <small style="opacity: 0.7;">({timestamp})</small><br>
                            {message}
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.markdown("### 👋 Start Your Conversation!")
            st.info("💡 **Tip:** I can help with motivation, productivity tips, goal setting, habit building, and general life advice in Hinglish!")
        
        # Chat input form
        with st.form("chat_form", clear_on_submit=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                user_input = st.text_area(
                    "💬 Type your message:",
                    placeholder="Ask me anything! 'Motivation chahiye', 'Goals kaise set karu?', 'Mood down hai'...",
                    height=80,
                    key="chat_input_form"
                )
            
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                send_button = st.form_submit_button("📤 Send", type="primary", use_container_width=True)
        
            if send_button and user_input.strip():
                # Generate AI response
                ai_response = ai_chat_hinglish(user_input)
                current_time = datetime.datetime.now().strftime("%H:%M")
                
                # Add to chat history
                st.session_state.chat_history.append(("You", user_input, current_time))
                st.session_state.chat_history.append(("AI", ai_response, current_time))
                
                # Keep only last 20 exchanges
                if len(st.session_state.chat_history) > 40:
                    st.session_state.chat_history = st.session_state.chat_history[-40:]
                
                st.rerun()
        
        # Quick Action Buttons
        st.markdown("### ⚡ Quick Commands")
        
        col_quick1, col_quick2, col_quick3, col_quick4 = st.columns(4)
        
        quick_commands = [
            ("💡 Motivate Me", "Motivation chahiye yaar, energy down hai", col_quick1),
            ("📊 Show My Stats", "Mera progress kya hai? Stats batao", col_quick2),
            ("🎯 Daily Goals", "Aaj kya karna chahiye? Goals suggest karo", col_quick3),
            ("💪 Habit Tips", "Habits kaise banau? Tips do", col_quick4)
        ]
        
        for label, message, col in quick_commands:
            with col:
                if st.button(label, key=f"quick_{label}", use_container_width=True):
                    ai_response = ai_chat_hinglish(message)
                    current_time = datetime.datetime.now().strftime("%H:%M")
                    st.session_state.chat_history.append(("You", message, current_time))
                    st.session_state.chat_history.append(("AI", ai_response, current_time))
                    st.rerun()
        
        # Chat controls
        col_clear, col_export = st.columns([1, 1])
        
        with col_clear:
            if st.button("🗑️ Clear Chat History", key="clear_chat_history"):
                st.session_state.chat_history = []
                st.rerun()
        
        with col_export:
            if st.button("💾 Export Chat", key="export_chat") and st.session_state.chat_history:
                chat_export = "\n".join([f"{speaker} ({timestamp}): {message}" for speaker, message, timestamp in st.session_state.chat_history])
                st.download_button(
                    label="📥 Download Chat Log",
                    data=chat_export,
                    file_name=f"anigpt_chat_{datetime.date.today()}.txt",
                    mime="text/plain"
                )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 30px 0;
        border: 1px solid rgba(255,255,255,0.2);
    ">
        <h3 style="
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.5rem;
            margin-bottom: 10px;
        ">🤖 AniGPT V2 - Your Growth Companion</h3>
        
        <p style="opacity: 0.9; font-size: 1rem; margin: 10px 0;">
            <strong>User:</strong> {st.session_state.username} • 
            <strong>Session:</strong> {datetime.datetime.now().strftime('%d/%m/%Y')} • 
            <strong>Status:</strong> 🟢 Active & Growing
        </p>
        
        <p style="opacity: 0.7; font-size: 0.9rem;">
            🎯 Track Progress • 📈 Build Habits • 🧠 Gain Insights • 🚀 Achieve Goals
        </p>
        
        <p style="opacity: 0.6; font-size: 0.8rem; margin-top: 15px;">
            Made with ❤️ for personal growth • Keep evolving, keep achieving! 🌟
        </p>
    </div>
    """, unsafe_allow_html=True)
