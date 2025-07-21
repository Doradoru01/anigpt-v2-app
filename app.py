import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime
import random
import time

# Page Configuration
st.set_page_config(
    page_title="🚀 AniGPT V2 - Your AI Companion", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Custom CSS for Attractive Design
st.markdown("""
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

/* Main App Styling */
.main {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

/* Header with Animation */
.main-header {
    background: linear-gradient(-45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Card Styling */
.feature-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin: 1rem 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

/* Enhanced Button Styling */
.stButton > button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    color: white !important;
    border: none;
    border-radius: 25px;
    padding: 0.7rem 2rem;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
}

/* Input Styling */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input,
.stSlider > div > div > div {
    background: rgba(255, 255, 255, 0.9) !important;
    border: 2px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 12px !important;
    color: #333 !important;
    font-size: 16px !important;
    padding: 10px !important;
    backdrop-filter: blur(10px);
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #4ECDC4 !important;
    box-shadow: 0 0 15px rgba(78, 205, 196, 0.3) !important;
}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    background: rgba(255, 255, 255, 0.1);
    padding: 8px;
    border-radius: 15px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: white;
    font-weight: 600;
    padding: 12px 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    transition: all 0.3s ease;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transform: translateY(-2px);
}

/* Sidebar Styling */
.css-1d391kg {
    background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
}

/* Metric Cards */
.metric-card {
    background: rgba(255, 255, 255, 0.15);
    padding: 1rem;
    border-radius: 12px;
    text-align: center;
    margin: 0.5rem 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
}

/* Success/Error Messages */
.stSuccess > div {
    background: linear-gradient(45deg, #4ECDC4, #44A08D);
    border-radius: 12px;
    border: none;
}

.stError > div {
    background: linear-gradient(45deg, #FF6B6B, #FF5252);
    border-radius: 12px;
    border: none;
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #4ECDC4, #44A08D);
    border-radius: 10px;
}

/* Chat Bubble Styling */
.chat-message {
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 15px;
    max-width: 80%;
}

.user-message {
    background: linear-gradient(45deg, #667eea, #764ba2);
    margin-left: auto;
    text-align: right;
}

.ai-message {
    background: linear-gradient(45deg, #4ECDC4, #44A08D);
    margin-right: auto;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 0.6s ease-out;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.pulse {
    animation: pulse 2s infinite;
}

</style>
""", unsafe_allow_html=True)

# Initialize Session States
def initialize_session_states():
    """Initialize all session states for data storage"""
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
    """Enhanced Hinglish AI Chat"""
    user_input_lower = user_input.lower()
    
    # Mood-based responses
    if any(word in user_input_lower for word in ['sad', 'upset', 'dukhi', 'pareshaan', 'tension', 'stress']):
        responses = [
            "🤗 Arre yaar, tension mat lo! Life me ups-downs aate rehte hain. Kya specific problem hai?",
            "💪 Bhai, har mushkil ka solution hota hai. Apne goals dekho, kitna achieve kiya hai!",
            "🌟 Mood down hai? Koi small task complete karo, instantly better feel karoge!",
            "💝 Dost, journal me feelings likh do. Sharing se halka ho jayega mind!"
        ]
    elif any(word in user_input_lower for word in ['happy', 'khush', 'accha', 'mast', 'great', 'awesome']):
        responses = [
            "🎉 Waah bhai! Khushi ki baat hai. Is positive energy me koi naya goal set karo!",
            "🚀 Mast hai yaar! Good mood me productivity double ho jati hai, use karo!",
            "⭐ Bahut badhiya! Is happiness ko journal me capture kar lo memories ke liye!",
            "🔥 Superb! Happy mood me habits complete karna easy hota hai, try karo!"
        ]
    elif any(word in user_input_lower for word in ['goal', 'achieve', 'target', 'complete', 'success']):
        responses = [
            "🎯 Goals ki baat? Fantastic! SMART goals banao - Specific, Measurable, Achievable!",
            "📈 Target achieve karna hai? Daily small progress track karo, motivation banay rahegi!",
            "🏆 Success milegi pakka! Consistency maintain karo aur progress celebrate karte raho!",
            "💡 Tip: Big goals ko small milestones me break karo, achieve karna asaan ho jayega!"
        ]
    elif any(word in user_input_lower for word in ['habit', 'daily', 'routine', 'streak']):
        responses = [
            "🔥 Habits? Yahi toh real game-changer hai! Small steps, big changes!",
            "⚡ Streak maintain karna mushkil lagta hai initially, but 21 days me automatic ho jaata!",
            "💪 Daily 1% improvement = 37x better in 1 year. Mathematics hai bhai!",
            "🌟 Start small - 2 minute rule follow karo. Reading = 1 page, Exercise = 2 minutes!"
        ]
    elif any(word in user_input_lower for word in ['learn', 'study', 'skill', 'knowledge']):
        responses = [
            "📚 Learning? Best investment ever! Kya naya skill develop kar rahe ho?",
            "🧠 Padhai consistent rakho, 25-minute Pomodoro technique try karo!",
            "🎓 Knowledge compound hoti hai. Daily thoda-thoda, but consistently!",
            "💡 Active learning karo - notes banao, teach karo kisi ko, practice karo!"
        ]
    else:
        responses = [
            "🤖 Haan bhai, samajh gaya! Main tumhara AI assistant hun, aur help chahiye?",
            "💭 Interesting point! Is thought ko journal me elaborate kar sakte ho!",
            "✨ Bilkul sahi direction me ja rahe ho! Consistency maintain karte raho!",
            "📊 Analytics dekho kabhi, patterns samjh me aa jayenge life ke!",
            "🎯 Focus rakho goals par, main yahin hun support ke liye!"
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
        "tags": tags
    }
    st.session_state.mood_entries.append(entry)
    return "✅ Mood entry saved successfully!"

def save_journal_entry(user, title, content, mood_tag, tags, category):
    """Save journal entry to session state"""
    entry = {
        "timestamp": datetime.datetime.now(),
        "user": user,
        "title": title,
        "content": content,
        "mood_tag": mood_tag,
        "tags": tags,
        "category": category,
        "word_count": len(content.split())
    }
    st.session_state.journal_entries.append(entry)
    return "✅ Journal entry saved successfully!"

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

def add_habit(user, habit_name, habit_type, target_frequency):
    """Add new habit"""
    habit = {
        "id": len(st.session_state.habits) + 1,
        "timestamp": datetime.datetime.now(),
        "user": user,
        "habit_name": habit_name,
        "habit_type": habit_type,
        "target_frequency": target_frequency,
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

def add_learning_session(user, topic, resource_type, duration, rating, notes, skills_learned):
    """Add learning session"""
    session = {
        "id": len(st.session_state.learning_sessions) + 1,
        "timestamp": datetime.datetime.now(),
        "user": user,
        "topic": topic,
        "resource_type": resource_type,
        "duration": duration,
        "rating": rating,
        "notes": notes,
        "skills_learned": skills_learned
    }
    st.session_state.learning_sessions.append(session)
    return "📚 Learning session logged successfully!"

# Initialize states
initialize_session_states()

# Animated Header
st.markdown("""
<div class="main-header fade-in">
    <h1>🚀 AniGPT V2 - Your Personal AI Companion</h1>
    <p style="font-size: 18px; margin: 10px 0;">Track • Learn • Grow • Achieve</p>
    <p style="font-size: 14px; opacity: 0.9;">Sab kuch ek jagah, Hinglish me! 🇮🇳</p>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    # User Profile Section
    st.markdown("""
    <div style="
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    ">
        <h2>👤 User Profile</h2>
    </div>
    """, unsafe_allow_html=True)
    
    user = st.text_input("🙋‍♂️ Your Name:", value="AniUser", key="user_name")
    
    # Dynamic Stats
    st.markdown("### 📊 Live Statistics")
    
    # Real stats from session data
    mood_count = len(st.session_state.mood_entries)
    journal_count = len(st.session_state.journal_entries)
    goals_count = len([g for g in st.session_state.goals if g['status'] == 'Active'])
    habits_count = len(st.session_state.habits)
    tasks_pending = len([t for t in st.session_state.tasks if t['status'] == 'Pending'])
    learning_hours = sum([s['duration'] for s in st.session_state.learning_sessions]) / 60
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("😊 Moods", mood_count, delta=1 if mood_count > 0 else 0)
        st.metric("🎯 Goals", goals_count, delta=1 if goals_count > 0 else 0)
        st.metric("📚 Learning", f"{learning_hours:.1f}h", delta=0.5 if learning_hours > 0 else 0)
    
    with col2:
        st.metric("📖 Journal", journal_count, delta=1 if journal_count > 0 else 0)
        st.metric("💪 Habits", habits_count, delta=1 if habits_count > 0 else 0)
        st.metric("📋 Tasks", tasks_pending, delta=-1 if tasks_pending > 0 else 0)
    
    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    if st.button("🎲 Random Motivation", key="random_motivation"):
        motivations = [
            "🌟 Aaj ka din special banao!",
            "💪 Consistency se sab kuch possible!",
            "🚀 Dreams ko goals me convert karo!",
            "🔥 Every small step counts!",
            "⭐ You're doing amazing!"
        ]
        st.success(random.choice(motivations))
    
    if st.button("📊 Show Summary", key="show_summary"):
        st.info(f"Total Entries: {mood_count + journal_count + len(st.session_state.tasks) + len(st.session_state.learning_sessions)}")

# Main Tabs with Enhanced Design
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "😊 Mood", "📖 Journal", "🎯 Goals", "💪 Habits", "📋 Tasks", "📚 Learning", "🤖 Chat"
])

# Enhanced Mood Tab
with tab1:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 😊 Daily Mood Tracker")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Enhanced mood selection
        mood_options = [
            "😊 Happy - Khush & Positive",
            "😢 Sad - Udaas & Down", 
            "😐 Neutral - Normal feeling",
            "😤 Angry - Gussa & Frustrated",
            "🤔 Thoughtful - Soch me hai",
            "😴 Tired - Thak gaya hu",
            "🥳 Excited - Bahut excited!",
            "😰 Anxious - Pareshaan & Worried",
            "😌 Peaceful - Shant & Calm",
            "🤩 Amazed - Surprised & Wonder"
        ]
        
        selected_mood = st.selectbox("🌈 Today's Mood:", mood_options, key="mood_select")
        
        reason = st.text_area(
            "📝 What's happening today?", 
            placeholder="Work stress, family time, achievement, health issue, celebration...",
            height=100,
            key="mood_reason"
        )
        
        tags = st.text_input(
            "🏷️ Tags (comma separated):",
            placeholder="work, family, health, achievement, social",
            key="mood_tags"
        )
    
    with col2:
        st.markdown("#### 📊 Intensity & Energy")
        
        intensity = st.slider("🎚️ Emotional Intensity:", 1, 10, 5, key="mood_intensity")
        st.caption(f"**Level:** {intensity}/10")
        
        energy = st.slider("⚡ Energy Level:", 1, 10, 5, key="mood_energy")
        st.caption(f"**Energy:** {energy}/10")
        
        # Visual indicators
        if intensity <= 3:
            st.error("🔴 Low Intensity")
        elif intensity <= 6:
            st.warning("🟡 Moderate Intensity") 
        else:
            st.success("🟢 High Intensity")
    
    # Save mood with enhanced feedback
    col_save, col_clear = st.columns([2, 1])
    
    with col_save:
        if st.button("💾 Save Mood Entry", type="primary", key="save_mood_btn"):
            if selected_mood and reason:
                result = save_mood_entry(user, selected_mood, reason, intensity, energy, tags)
                st.success(result)
                st.balloons()
                
                # Show encouragement message
                if intensity >= 7:
                    st.info("🌟 Great mood! Perfect time for productive work!")
                elif intensity <= 4:
                    st.info("💝 It's okay to have low days. Self-care important hai!")
                
            else:
                st.error("Please fill mood and reason fields!")
    
    with col_clear:
        if st.button("🗑️ Clear Form", key="clear_mood"):
            st.rerun()
    
    # Mood Analytics
    if st.session_state.mood_entries:
        st.markdown("### 📈 Your Mood Analytics")
        
        # Create mood trend chart
        df_moods = pd.DataFrame([
            {
                'Date': entry['timestamp'].strftime('%m/%d'),
                'Intensity': entry['intensity'],
                'Energy': entry['energy'],
                'Mood': entry['mood'].split(' ')[1] if len(entry['mood'].split(' ')) > 1 else entry['mood']
            }
            for entry in st.session_state.mood_entries[-7:]  # Last 7 entries
        ])
        
        if len(df_moods) > 1:
            # Line chart for trends
            fig = px.line(df_moods, x='Date', y=['Intensity', 'Energy'], 
                         title="📊 Mood & Energy Trend (Last 7 entries)",
                         markers=True)
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Mood distribution
            mood_dist = pd.DataFrame([entry['mood'].split(' ')[0] for entry in st.session_state.mood_entries])
            fig2 = px.histogram(mood_dist, x=0, title="😊 Mood Distribution")
            fig2.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    else:
        st.info("🌟 Start tracking your moods to see beautiful analytics!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Journal Tab
with tab2:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 📖 Personal Digital Diary")
    
    # Journal entry form
    with st.form("journal_form", clear_on_submit=False):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            title = st.text_input(
                "📝 Entry Title:",
                placeholder="Today's Reflection, Weekly Review, Random Thoughts...",
                key="journal_title"
            )
            
            content = st.text_area(
                "💭 What's on your mind?",
                placeholder="Apne thoughts, experiences, learnings, feelings detail me likho...\n\nAaj kya hua? Kya socha? Kya seekha?",
                height=200,
                key="journal_content"
            )
            
        with col2:
            mood_tag = st.selectbox(
                "😊 Mood Tag:",
                ["😊 Happy", "😢 Sad", "😐 Neutral", "😤 Frustrated", 
                 "🤔 Reflective", "😌 Peaceful", "🥳 Excited"],
                key="journal_mood"
            )
            
            category = st.selectbox(
                "📁 Category:",
                ["Personal", "Work", "Family", "Learning", "Health", 
                 "Travel", "Goals", "Random", "Gratitude"],
                key="journal_category"
            )
            
            tags = st.text_input(
                "🏷️ Tags:",
                placeholder="learning, work, family",
                key="journal_tags"
            )
        
        # Word count display
        if content:
            word_count = len(content.split())
            st.caption(f"📊 Word Count: {word_count} words")
        
        # Submit buttons
        col_submit, col_clear = st.columns([2, 1])
        
        with col_submit:
            submitted = st.form_submit_button("📚 Save Journal Entry", type="primary")
            
        with col_clear:
            clear_journal = st.form_submit_button("🗑️ Clear")
        
        if submitted:
            if title and content:
                result = save_journal_entry(user, title, content, mood_tag, tags, category)
                st.success(result)
                st.balloons()
                
                # Motivational message based on word count
                word_count = len(content.split())
                if word_count > 100:
                    st.info("🌟 Detailed entry! Writing helps process thoughts better!")
                elif word_count > 50:
                    st.info("👍 Good reflection! Keep journaling regularly!")
                else:
                    st.info("✨ Great start! Try to elaborate more next time!")
                    
            else:
                st.error("Please fill both title and content!")
    
    # Recent Journal Entries
    if st.session_state.journal_entries:
        st.markdown("### 📚 Recent Journal Entries")
        
        # Show last 3 entries
        for i, entry in enumerate(st.session_state.journal_entries[-3:]):
            with st.expander(f"📖 {entry['title']} - {entry['timestamp'].strftime('%d/%m/%Y %H:%M')}"):
                st.markdown(f"**Category:** {entry['category']} | **Mood:** {entry['mood_tag']}")
                st.markdown(f"**Content:** {entry['content']}")
                st.markdown(f"**Tags:** {entry['tags']}")
                st.caption(f"Word Count: {entry['word_count']} words")
        
        # Journal Analytics
        st.markdown("### 📊 Journal Analytics")
        
        total_entries = len(st.session_state.journal_entries)
        total_words = sum([entry['word_count'] for entry in st.session_state.journal_entries])
        avg_words = total_words / total_entries if total_entries > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📚 Total Entries", total_entries)
        with col2:
            st.metric("📝 Total Words", f"{total_words:,}")
        with col3:
            st.metric("📊 Avg Words/Entry", f"{avg_words:.0f}")
        
        # Category distribution
        if total_entries > 0:
            categories = [entry['category'] for entry in st.session_state.journal_entries]
            category_counts = pd.Series(categories).value_counts()
            
            fig = px.pie(values=category_counts.values, names=category_counts.index,
                        title="📊 Journal Entries by Category")
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.info("🌟 Start journaling! Writing helps organize thoughts and track personal growth!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Goals Tab
with tab3:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 🎯 Goal Setting & Achievement Tracker")
    
    # Add new goal form
    with st.expander("➕ Add New Goal", expanded=True):
        with st.form("goal_form"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                goal_name = st.text_input(
                    "🎯 Goal Title:",
                    placeholder="Complete Python Course, Lose 10kg, Read 12 Books...",
                    key="goal_name"
                )
                
                description = st.text_area(
                    "📝 Goal Description:",
                    placeholder="Kaise achieve karoge? Steps kya hain? Timeline kya hai?",
                    height=100,
                    key="goal_description"
                )
            
            with col2:
                category = st.selectbox(
                    "📁 Category:",
                    ["🏢 Work", "💪 Health", "📚 Learning", "💰 Finance", 
                     "👥 Relationships", "🎨 Hobbies", "🌍 Travel"],
                    key="goal_category"
                )
                
                priority = st.selectbox(
                    "⭐ Priority:",
                    ["🔴 High", "🟡 Medium", "🟢 Low"],
                    key="goal_priority"
                )
                
                target_date = st.date_input(
                    "📅 Target Date:",
                    min_value=datetime.date.today(),
                    key="goal_target"
                )
            
            if st.form_submit_button("🎯 Add Goal", type="primary"):
                if goal_name and description:
                    result = add_goal(user, goal_name, category, priority, target_date, description)
                    st.success(result)
                    st.balloons()
                else:
                    st.error("Please fill goal name and description!")
    
    # Display Active Goals
    if st.session_state.goals:
        active_goals = [goal for goal in st.session_state.goals if goal['status'] == 'Active']
        
        if active_goals:
            st.markdown("### 🎯 Active Goals")
            
            for goal in active_goals:
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.markdown(f"**🎯 {goal['goal_name']}**")
                        st.caption(f"{goal['category']} | {goal['priority']}")
                        st.caption(f"Target: {goal['target_date']}")
                        
                        # Progress bar
                        progress = st.slider(
                            f"Progress for {goal['goal_name']}",
                            0, 100, goal['progress'],
                            key=f"progress_{goal['id']}"
                        )
                        
                        # Update progress in session state
                        for g in st.session_state.goals:
                            if g['id'] == goal['id']:
                                g['progress'] = progress
                                if progress >= 100:
                                    g['status'] = 'Completed'
                    
                    with col2:
                        days_left = (goal['target_date'] - datetime.date.today()).days
                        if days_left > 0:
                            st.metric("📅 Days Left", days_left)
                        else:
                            st.error("⏰ Overdue")
                    
                    with col3:
                        st.metric("📊 Progress", f"{progress}%")
                        
                        if progress >= 100:
                            st.success("🎉 Completed!")
                        elif progress >= 75:
                            st.info("🔥 Almost There!")
                        elif progress >= 50:
                            st.warning("📈 Good Progress")
                        else:
                            st.info("🚀 Just Started")
                    
                    st.markdown("---")
        
        # Goals Analytics
        st.markdown("### 📊 Goals Analytics")
        
        total_goals = len(st.session_state.goals)
        completed_goals = len([g for g in st.session_state.goals if g['status'] == 'Completed'])
        avg_progress = sum([g['progress'] for g in st.session_state.goals]) / total_goals if total_goals > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🎯 Total Goals", total_goals)
        with col2:
            st.metric("✅ Completed", completed_goals)
        with col3:
            st.metric("📊 Avg Progress", f"{avg_progress:.1f}%")
        
        # Goal categories chart
        if total_goals > 0:
            categories = [goal['category'] for goal in st.session_state.goals]
            category_counts = pd.Series(categories).value_counts()
            
            fig = px.bar(x=category_counts.index, y=category_counts.values,
                        title="📊 Goals by Category")
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.info("🎯 Set your first goal! Goals give direction and purpose to life!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Habits Tab
with tab4:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 💪 Daily Habit Tracker & Streak Builder")
    
    # Add new habit
    with st.expander("➕ Add New Habit", expanded=True):
        with st.form("habit_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                habit_name = st.text_input(
                    "💪 Habit Name:",
                    placeholder="Exercise, Reading, Meditation, Water Intake...",
                    key="habit_name"
                )
                
                habit_type = st.selectbox(
                    "🎯 Habit Type:",
                    ["🏃 Health", "📚 Learning", "💼 Productivity", "🧘 Wellness", 
                     "🎨 Creative", "💰 Financial", "👥 Social"],
                    key="habit_type"
                )
            
            with col2:
                target_frequency = st.selectbox(
                    "🔄 Target Frequency:",
                    ["Daily", "5x per week", "3x per week", "Weekly"],
                    key="habit_frequency"
                )
            
            if st.form_submit_button("💪 Add Habit", type="primary"):
                if habit_name:
                    result = add_habit(user, habit_name, habit_type, target_frequency)
                    st.success(result)
                    st.balloons()
                else:
                    st.error("Please enter habit name!")
    
    # Display and track habits
    if st.session_state.habits:
        st.markdown("### 🔥 Your Habit Tracker")
        
        for habit in st.session_state.habits:
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                
                with col1:
                    st.markdown(f"**💪 {habit['habit_name']}**")
                    st.caption(f"{habit['habit_type']} | {habit['target_frequency']}")
                
                with col2:
                    st.metric("🔥 Current Streak", habit['current_streak'])
                
                with col3:
                    st.metric("✅ Total Done", habit['total_completions'])
                
                with col4:
                    # Mark as complete for today
                    today = datetime.date.today()
                    if habit['last_completed'] != today:
                        if st.button(f"✅ Done Today", key=f"habit_complete_{habit['id']}"):
                            # Update habit
                            for h in st.session_state.habits:
                                if h['id'] == habit['id']:
                                    h['last_completed'] = today
                                    h['total_completions'] += 1
                                    
                                    # Calculate streak
                                    if h['last_completed'] and (today - h['last_completed']).days <= 1:
                                        h['current_streak'] += 1
                                    else:
                                        h['current_streak'] = 1
                                    
                            st.success(f"🔥 Streak: {habit['current_streak']} days!")
                            st.rerun()
                    else:
                        st.success("✅ Done!")
                
                # Streak visualization
                if habit['current_streak'] > 0:
                    streak_bar = "🔥" * min(habit['current_streak'], 10)
                    if habit['current_streak'] > 10:
                        streak_bar += f" (+{habit['current_streak'] - 10})"
                    st.caption(f"Streak: {streak_bar}")
                
                st.markdown("---")
        
        # Habits Analytics
        st.markdown("### 📊 Habits Analytics")
        
        total_habits = len(st.session_state.habits)
        total_completions = sum([h['total_completions'] for h in st.session_state.habits])
        max_streak = max([h['current_streak'] for h in st.session_state.habits]) if st.session_state.habits else 0
        active_streaks = len([h for h in st.session_state.habits if h['current_streak'] > 0])
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("💪 Total Habits", total_habits)
        with col2:
            st.metric("✅ Completions", total_completions)
        with col3:
            st.metric("🔥 Max Streak", max_streak)
        with col4:
            st.metric("🎯 Active Streaks", active_streaks)
        
        # Habit completion chart
        if total_habits > 0:
            habit_data = pd.DataFrame([
                {'Habit': h['habit_name'], 'Completions': h['total_completions'], 
                 'Streak': h['current_streak']} 
                for h in st.session_state.habits
            ])
            
            fig = px.bar(habit_data, x='Habit', y='Completions',
                        title="📊 Habit Completion Count")
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.info("💪 Add your first habit! Small daily actions create big life changes!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Tasks Tab
with tab5:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 📋 Smart Task Management System")
    
    # Add new task
    with st.expander("➕ Add New Task", expanded=True):
        with st.form("task_form"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                task_title = st.text_input(
                    "📋 Task Title:",
                    placeholder="Complete presentation, Call dentist, Buy groceries...",
                    key="task_title"
                )
                
                description = st.text_area(
                    "📝 Task Details:",
                    placeholder="Task ke details, requirements, steps...",
                    height=80,
                    key="task_description"
                )
            
            with col2:
                priority = st.selectbox(
                    "🚨 Priority:",
                    ["🔴 Urgent", "🟡 Important", "🟢 Normal"],
                    key="task_priority"
                )
                
                due_date = st.date_input(
                    "📅 Due Date:",
                    min_value=datetime.date.today(),
                    key="task_due"
                )
                
                category = st.selectbox(
                    "📁 Category:",
                    ["💼 Work", "🏠 Personal", "🛒 Shopping", "💊 Health", 
                     "📚 Learning", "👥 Social", "💰 Finance"],
                    key="task_category"
                )
            
            if st.form_submit_button("📋 Add Task", type="primary"):
                if task_title:
                    result = add_task(user, task_title, priority, due_date, category, description)
                    st.success(result)
                    st.balloons()
                else:
                    st.error("Please enter task title!")
    
    # Display Tasks
    if st.session_state.tasks:
        # Filter tasks
        pending_tasks = [task for task in st.session_state.tasks if task['status'] == 'Pending']
        completed_tasks = [task for task in st.session_state.tasks if task['status'] == 'Completed']
        
        # Pending Tasks
        if pending_tasks:
            st.markdown("### ⏳ Pending Tasks")
            
            # Sort by priority and due date
            priority_order = {"🔴 Urgent": 1, "🟡 Important": 2, "🟢 Normal": 3}
            pending_tasks.sort(key=lambda x: (priority_order[x['priority']], x['due_date']))
            
            for task in pending_tasks:
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.markdown(f"**{task['priority']} {task['task_title']}**")
                        st.caption(f"{task['category']} | Due: {task['due_date']}")
                        if task['description']:
                            st.caption(f"📝 {task['description'][:100]}...")
                    
                    with col2:
                        days_until_due = (task['due_date'] - datetime.date.today()).days
                        if days_until_due < 0:
                            st.error(f"⏰ {abs(days_until_due)} days overdue")
                        elif days_until_due == 0:
                            st.warning("⚡ Due Today")
                        else:
                            st.info(f"📅 {days_until_due} days left")
                    
                    with col3:
                        if st.button("✅ Complete", key=f"complete_task_{task['id']}"):
                            # Mark task as completed
                            for t in st.session_state.tasks:
                                if t['id'] == task['id']:
                                    t['status'] = 'Completed'
                                    t['completed_at'] = datetime.datetime.now()
                            
                            st.success("Task completed! 🎉")
                            st.rerun()
                    
                    st.markdown("---")
        
        # Completed Tasks
        if completed_tasks:
            with st.expander("✅ Recently Completed Tasks"):
                for task in completed_tasks[-5:]:  # Show last 5 completed
                    st.markdown(f"✅ **{task['task_title']}** - Completed on {task['completed_at'].strftime('%d/%m/%Y')}")
        
        # Task Analytics
        st.markdown("### 📊 Task Analytics")
        
        total_tasks = len(st.session_state.tasks)
        completed_count = len(completed_tasks)
        pending_count = len(pending_tasks)
        completion_rate = (completed_count / total_tasks * 100) if total_tasks > 0 else 0
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📋 Total Tasks", total_tasks)
        with col2:
            st.metric("✅ Completed", completed_count)
        with col3:
            st.metric("⏳ Pending", pending_count)
        with col4:
            st.metric("📊 Completion Rate", f"{completion_rate:.1f}%")
        
        # Task distribution charts
        if total_tasks > 0:
            # Priority distribution
            priorities = [task['priority'] for task in st.session_state.tasks]
            priority_counts = pd.Series(priorities).value_counts()
            
            fig1 = px.pie(values=priority_counts.values, names=priority_counts.index,
                         title="📊 Tasks by Priority")
            fig1.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig1, use_container_width=True)
            
            # Category distribution
            categories = [task['category'] for task in st.session_state.tasks]
            category_counts = pd.Series(categories).value_counts()
            
            fig2 = px.bar(x=category_counts.index, y=category_counts.values,
                         title="📊 Tasks by Category")
            fig2.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    else:
        st.info("📋 Add your first task! Good task management is key to productivity!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Learning Tab
with tab6:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 📚 Learning Journey Tracker")
    
    # Add learning session
    with st.expander("➕ Log Learning Session", expanded=True):
        with st.form("learning_form"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                topic = st.text_input(
                    "📖 Topic/Subject:",
                    placeholder="Python Functions, Digital Marketing, Guitar Chords...",
                    key="learning_topic"
                )
                
                notes = st.text_area(
                    "📝 Key Learnings & Notes:",
                    placeholder="Kya naya seekha? Important points, insights, questions...",
                    height=120,
                    key="learning_notes"
                )
                
                skills_learned = st.text_input(
                    "🎯 Skills Acquired:",
                    placeholder="Loop concepts, Chord transitions, Marketing strategies...",
                    key="learning_skills"
                )
            
            with col2:
                resource_type = st.selectbox(
                    "📺 Learning Resource:",
                    ["📚 Book", "🎥 Video", "💻 Course", "📰 Article", 
                     "🎧 Podcast", "👨‍🏫 Workshop", "💪 Practice"],
                    key="learning_resource"
                )
                
                duration = st.number_input(
                    "⏱️ Duration (minutes):",
                    min_value=0, max_value=480, value=30,
                    key="learning_duration"
                )
                
                rating = st.slider(
                    "⭐ Experience Rating:",
                    1, 10, 7,
                    key="learning_rating"
                )
                st.caption("1=Poor, 5=Average, 10=Excellent")
            
            if st.form_submit_button("📚 Log Learning Session", type="primary"):
                if topic and notes:
                    result = add_learning_session(user, topic, resource_type, duration, rating, notes, skills_learned)
                    st.success(result)
                    st.balloons()
                    
                    # Motivational messages
                    if duration >= 60:
                        st.info("🌟 Great dedication! Long learning sessions build expertise!")
                    elif duration >= 30:
                        st.info("👍 Good session! Consistent learning pays off!")
                    else:
                        st.info("✨ Every minute counts! Keep the momentum going!")
                        
                else:
                    st.error("Please fill topic and notes!")
    
    # Display Learning Sessions
    if st.session_state.learning_sessions:
        st.markdown("### 📖 Recent Learning Sessions")
        
        # Show last 5 sessions
        for session in st.session_state.learning_sessions[-5:]:
            with st.expander(f"📚 {session['topic']} - {session['timestamp'].strftime('%d/%m/%Y')}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**📝 Notes:** {session['notes']}")
                    st.markdown(f"**🎯 Skills:** {session['skills_learned']}")
                
                with col2:
                    st.metric("⏱️ Duration", f"{session['duration']} min")
                    st.metric("⭐ Rating", f"{session['rating']}/10")
                    st.caption(f"Resource: {session['resource_type']}")
        
        # Learning Analytics
        st.markdown("### 📊 Learning Analytics")
        
        total_sessions = len(st.session_state.learning_sessions)
        total_time = sum([s['duration'] for s in st.session_state.learning_sessions])
        total_hours = total_time / 60
        avg_rating = sum([s['rating'] for s in st.session_state.learning_sessions]) / total_sessions
        avg_duration = total_time / total_sessions if total_sessions > 0 else 0
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📚 Sessions", total_sessions)
        with col2:
            st.metric("⏱️ Total Time", f"{total_hours:.1f}h")
        with col3:
            st.metric("⭐ Avg Rating", f"{avg_rating:.1f}/10")
        with col4:
            st.metric("📊 Avg Duration", f"{avg_duration:.0f}min")
        
        # Learning trends
        if total_sessions > 1:
            # Daily learning time
            df_learning = pd.DataFrame([
                {
                    'Date': session['timestamp'].strftime('%m/%d'),
                    'Duration': session['duration'],
                    'Rating': session['rating'],
                    'Topic': session['topic']
                }
                for session in st.session_state.learning_sessions[-7:]
            ])
            
            fig1 = px.bar(df_learning, x='Date', y='Duration',
                         title="📊 Daily Learning Time (Last 7 sessions)")
            fig1.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig1, use_container_width=True)
            
            # Resource type distribution
            resources = [s['resource_type'] for s in st.session_state.learning_sessions]
            resource_counts = pd.Series(resources).value_counts()
            
            fig2 = px.pie(values=resource_counts.values, names=resource_counts.index,
                         title="📊 Learning Resources Used")
            fig2.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Learning goals suggestion
        if total_hours >= 10:
            st.success("🎓 Amazing! 10+ hours of learning logged. You're building serious expertise!")
        elif total_hours >= 5:
            st.info("📈 Good progress! 5+ hours logged. Keep the momentum going!")
        else:
            st.info("🌟 Great start! Consistency in learning leads to mastery!")
    
    else:
        st.info("📚 Log your first learning session! Track your knowledge journey!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Chat Tab
with tab7:
    st.markdown('<div class="feature-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 🤖 AniGPT AI Chat - Your Hinglish Companion")
    
    # Chat interface
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        if st.session_state.chat_history:
            st.markdown("### 💬 Chat History")
            
            for i, (speaker, message, timestamp) in enumerate(st.session_state.chat_history):
                if speaker == "You":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>🧑 You</strong> <span style="font-size: 12px; opacity: 0.7;">({timestamp})</span><br>
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message ai-message">
                        <strong>🤖 AniGPT</strong> <span style="font-size: 12px; opacity: 0.7;">({timestamp})</span><br>
                        {message}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("🌟 Start chatting with AniGPT! Ask about productivity, motivation, goals, or just casual baat-cheet!")
    
    # Chat input
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_input(
                "💬 Type your message (Hinglish me):",
                placeholder="Hello, kaise ho? Motivation chahiye? Goal set karna hai?",
                key="chat_input"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Spacing
            send_button = st.form_submit_button("📤 Send", type="primary")
        
        if send_button and user_input:
            # Get AI response
            ai_response = ai_chat_hinglish(user_input)
            current_time = datetime.datetime.now().strftime("%H:%M")
            
            # Add to chat history
            st.session_state.chat_history.append(("You", user_input, current_time))
            st.session_state.chat_history.append(("AI", ai_response, current_time))
            
            # Keep only last 10 exchanges
            if len(st.session_state.chat_history) > 20:
                st.session_state.chat_history = st.session_state.chat_history[-20:]
            
            st.rerun()
    
    # Chat controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💡 Get Motivation", key="get_motivation"):
            motivational_quotes = [
                "🌟 Har din ek naya chance hai better banne ka!",
                "💪 Consistency beats perfection har baar!",
                "🚀 Dreams ko goals me convert karo, goals ko action me!",
                "🔥 Small progress is still progress!",
                "⭐ Aaj ka 1% improvement = 37x better in 1 year!"
            ]
            motivation = random.choice(motivational_quotes)
            current_time = datetime.datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append(("AI", motivation, current_time))
            st.rerun()
    
    with col2:
        if st.button("📊 Quick Stats", key="quick_stats"):
            stats_msg = f"""
            📊 Your AniGPT Stats:
            😊 Mood Entries: {len(st.session_state.mood_entries)}
            📖 Journal Entries: {len(st.session_state.journal_entries)}
            🎯 Active Goals: {len([g for g in st.session_state.goals if g['status'] == 'Active'])}
            💪 Habits Tracked: {len(st.session_state.habits)}
            📋 Pending Tasks: {len([t for t in st.session_state.tasks if t['status'] == 'Pending'])}
            📚 Learning Sessions: {len(st.session_state.learning_sessions)}
            
            Keep growing! 🚀
            """
            current_time = datetime.datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append(("AI", stats_msg, current_time))
            st.rerun()
    
    with col3:
        if st.button("🗑️ Clear Chat", key="clear_chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Suggested questions
    st.markdown("### 💡 Suggested Questions")
    suggestions = [
        "Motivation chahiye yaar",
        "Goals kaise set karu?",
        "Habits kaise banau?", 
        "Productivity tips do",
        "Mood down hai, help karo",
        "Learning kaise improve karu?"
    ]
    
    for suggestion in suggestions:
        if st.button(f"💬 {suggestion}", key=f"suggest_{suggestion}"):
            ai_response = ai_chat_hinglish(suggestion)
            current_time = datetime.datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append(("You", suggestion, current_time))
            st.session_state.chat_history.append(("AI", ai_response, current_time))
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px; margin-top: 2rem;">
    <h3>🚀 AniGPT V2 - Your Complete Life Management System</h3>
    <p>Made with ❤️ for productivity enthusiasts | Keep Growing! 📈</p>
    <p style="font-size: 14px; opacity: 0.8;">
        Track • Analyze • Improve • Achieve 🎯<br>
        Sab kuch ek jagah, Hinglish mein! 🇮🇳
    </p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh for real-time updates
if st.button("🔄 Refresh Data", key="refresh_all"):
    st.rerun()
