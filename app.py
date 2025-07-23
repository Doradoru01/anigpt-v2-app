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
.main {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #FFFFFF;
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

.feature-highlight {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 20px;
    margin: 15px 0;
    border-left: 4px solid #4ECDC4;
}

/* User Header */
.user-header {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px 35px;
    margin: 25px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.user-name {
    font-size: 1.5rem;
    font-weight: 600;
    color: #FFFFFF;
}

.user-badge {
    background: linear-gradient(45deg, #4ECDC4, #44A08D);
    padding: 8px 20px;
    border-radius: 25px;
    font-size: 0.9rem;
    font-weight: 500;
    box-shadow: 0 4px 15px rgba(78,205,196,0.3);
}

/* Modern Cards */
.modern-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 35px;
    margin: 30px 0;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.modern-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 25px 50px rgba(0,0,0,0.2);
    border-color: rgba(255,255,255,0.3);
}

/* Input Styling */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.95) !important;
    border: 2px solid rgba(255,255,255,0.3) !important;
    border-radius: 15px !important;
    color: #333 !important;
    font-size: 16px !important;
    padding: 15px 20px !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #4ECDC4 !important;
    box-shadow: 0 0 20px rgba(78,205,196,0.4) !important;
    transform: translateY(-2px);
}

/* Enhanced Button Styling */
.stButton > button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    padding: 15px 30px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 8px 25px rgba(255,107,107,0.3) !important;
    text-transform: none !important;
    min-height: 50px !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 15px 40px rgba(255,107,107,0.4) !important;
    background: linear-gradient(45deg, #4ECDC4, #FF6B6B) !important;
}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 12px;
    gap: 12px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 15px;
    color: white;
    font-weight: 600;
    padding: 15px 25px;
    transition: all 0.3s ease;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,255,255,0.2);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    border-color: rgba(255,255,255,0.4);
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
}

/* Sidebar Enhancements */
.sidebar-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
    transition: all 0.3s ease;
}

.sidebar-card:hover {
    background: rgba(255,255,255,0.15);
    transform: scale(1.02);
}

/* Success/Error Messages */
.stSuccess > div {
    background: linear-gradient(45deg, #4ECDC4, #44A08D) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
    box-shadow: 0 8px 25px rgba(78,205,196,0.3);
}

.stError > div {
    background: linear-gradient(45deg, #FF6B6B, #FF5252) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
    box-shadow: 0 8px 25px rgba(255,107,107,0.3);
}

.stInfo > div {
    background: linear-gradient(45deg, #45B7D1, #3498db) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
    box-shadow: 0 8px 25px rgba(69,183,209,0.3);
}

.stWarning > div {
    background: linear-gradient(45deg, #FFA726, #FF9800) !important;
    border-radius: 15px !important;
    border: none !important;
    font-weight: 500 !important;
    box-shadow: 0 8px 25px rgba(255,167,38,0.3);
}

/* Metric Cards */
.metric-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 15px 0;
    transition: all 0.3s ease;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.metric-card:hover {
    transform: translateY(-5px) scale(1.03);
    background: rgba(255,255,255,0.15);
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 900;
    background: linear-gradient(45deg, #4ECDC4, #45B7D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-label {
    font-size: 1rem;
    opacity: 0.8;
    font-weight: 500;
    margin-top: 5px;
}

/* Chat Messages */
.chat-user {
    background: rgba(255,107,107,0.2);
    backdrop-filter: blur(10px);
    padding: 20px 25px;
    border-radius: 25px 25px 8px 25px;
    margin: 15px 0;
    margin-left: 20%;
    border: 1px solid rgba(255,107,107,0.3);
    box-shadow: 0 8px 25px rgba(255,107,107,0.2);
}

.chat-ai {
    background: rgba(78,205,196,0.2);
    backdrop-filter: blur(10px);
    padding: 20px 25px;
    border-radius: 25px 25px 25px 8px;
    margin: 15px 0;
    margin-right: 20%;
    border: 1px solid rgba(78,205,196,0.3);
    box-shadow: 0 8px 25px rgba(78,205,196,0.2);
}

/* Progress Bars and Sliders */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #4ECDC4, #44A08D) !important;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(78,205,196,0.3);
}

.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #4ECDC4, #44A08D) !important;
}

/* Expander Styling */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.1) !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .welcome-title {
        font-size: 2.5rem;
    }
    
    .welcome-container {
        margin: 20px 10px;
        padding: 40px 25px;
    }
    
    .user-header {
        flex-direction: column;
        gap: 15px;
        padding: 25px 20px;
    }
    
    .modern-card {
        padding: 25px 20px;
        margin: 20px 0;
    }
    
    .chat-user, .chat-ai {
        margin-left: 5%;
        margin-right: 5%;
    }
}

/* Loading Animations */
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
    animation: fadeInUp 0.8s ease-out;
}

@keyframes pulse {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
}

.pulse-animation {
    animation: pulse 2s infinite;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 10px;
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

</style>
""", unsafe_allow_html=True)

# Initialize Session States
def initialize_session_states():
    """Initialize all session states for data storage"""
    states_to_initialize = {
        "user_authenticated": False,
        "username": "",
        "mood_entries": [],
        "journal_entries": [],
        "goals": [],
        "habits": [],
        "tasks": [],
        "learning_sessions": [],
        "chat_history": [],
        "user_preferences": {"theme": "default", "notifications": True}
    }
    
    for state, default_value in states_to_initialize.items():
        if state not in st.session_state:
            st.session_state[state] = default_value

# Enhanced AI Chat Function
def ai_chat_hinglish(user_input, user_context=None):
    """Advanced Hinglish AI Chat with user context awareness"""
    user_input_lower = user_input.lower()
    
    # Get user context for personalized responses
    if user_context is None:
        user_context = {
            'mood_entries': len(st.session_state.mood_entries),
            'goals': len(st.session_state.goals),
            'habits': len(st.session_state.habits),
            'recent_mood': st.session_state.mood_entries[-1] if st.session_state.mood_entries else None
        }
    
    # Context-aware mood responses
    if any(word in user_input_lower for word in ['sad', 'upset', 'dukhi', 'pareshaan', 'tension', 'stress', 'depressed', 'down']):
        responses = [
            f"🤗 {st.session_state.username}, main samajh raha hun. Life me tough phases aate rehte hain. Kya specific baat pareshaan kar rahi hai?",
            "💪 Bhai, you're stronger than you think! Ye temporary phase hai. Koi physical activity try karo - walk, music, ya deep breathing.",
            "🌟 Mood low hai toh koi baat nahi. Journal me feelings pour kar do, ya koi small habit complete karo. Small wins matter!",
            "💝 Dost, mental health important hai. If needed, professional help bhi le sakte ho. Main yahan hun support ke liye!",
            "🫂 Tough day ho raha hai? It's completely normal. Self-care karo - favorite music, good food, ya kisi close friend se baat."
        ]
        
        # Add context-based suggestions
        if user_context['recent_mood'] and user_context['recent_mood']['intensity'] < 5:
            responses.append(f"🔍 Main dekh raha hun recent mood entries me pattern. Kya similar situations me pehle bhi aisa feel kiya hai?")
    
    elif any(word in user_input_lower for word in ['happy', 'khush', 'accha', 'mast', 'good', 'great', 'excited', 'amazing', 'fantastic']):
        responses = [
            f"🎉 Waah {st.session_state.username}! Khushi dekh ke mera bhi mood up ho gaya! Is positive energy ko productive kaam me channel karo!",
            "🚀 Fantastic energy! Good mood me complex tasks tackle karna easy lagta hai. Koi challenging goal pick karo!",
            "⭐ Bahut badhiya! Happiness contagious hai. Is joy ko journal me capture kar lo future motivation ke liye!",
            "🔥 Superb vibes! Happy mood me new habits start karna ya difficult conversations karna easy hota hai!",
            "🌈 Amazing mood! Positive energy spread karo - friends ko motivate karo, ya koi creative project start karo!"
        ]
        
        if user_context['goals']:
            responses.append(f"🎯 Perfect timing! {user_context['goals']} goals hain tumhare, is energy me unpar focus karo!")
    
    elif any(word in user_input_lower for word in ['goal', 'target', 'achieve', 'complete', 'success', 'accomplish', 'objective']):
        responses = [
            "🎯 Goals ki baat? Perfect mindset! SMART framework follow karo - Specific, Measurable, Achievable, Relevant, Time-bound!",
            "📈 Achievement unlock karne ka proven formula: Clear vision + Daily consistent action + Progress tracking = Success guaranteed!",
            "🏆 Success milegi pakka! Big goals ko small daily milestones me break karo. Compound effect dekhoge!",
            "💡 Goal setting masterclass: Write it down, visualize success, create accountability, celebrate small wins!",
            "🎖️ Target achieve karne ka secret: Focus on systems, not just outcomes. Process perfect karo, results automatic
