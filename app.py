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
                    placeholder="Express your thoughts freely... What happened today? What are you learning? How are you feeling? What are your insights and reflections?",
                    height=200,
                    key="journal_content"
                )
                
            with col2:
                category = st.selectbox(
                    "📁 Category:",
                    ["Personal", "Work", "Family", "Learning", "Health", 
                     "Travel", "Goals", "Random", "Gratitude"],
                    key="journal_category"
                )
                
                tags = st.text_input(
                    "🏷️ Tags:",
                    placeholder="learning, work, family, growth",
                    key="journal_tags"
                )
        
            # Word count display
            if content:
                word_count = len(content.split())
                char_count = len(content)
                st.caption(f"📊 **{word_count}** words • **{char_count}** characters")
            
            # Submit buttons
            col_submit, col_clear = st.columns([2, 1])
            
            with col_submit:
                submitted = st.form_submit_button("📚 Save Journal Entry", type="primary", use_container_width=True)
                
            with col_clear:
                clear_journal = st.form_submit_button("🗑️ Clear Form")
            
            if submitted:
                if title and content:
                    result = save_journal_entry(st.session_state.username, title, content, category, tags)
                    st.success(result)
                    st.balloons()
                    
                    # Provide word count feedback
                    word_count = len(content.split())
                    if word_count > 200:
                        st.info("🌟 Excellent detailed entry! Long-form writing helps process complex thoughts.")
                    elif word_count > 100:
                        st.info("👍 Great reflection! Regular journaling builds self-awareness.")
                    else:
                        st.info("✨ Good start! Try to elaborate more for deeper insights next time.")
                        
                else:
                    st.error("🚨 Please provide both title and content for your journal entry!")
        
        # Recent Journal Entries
        if st.session_state.journal_entries:
            st.markdown("### 📚 Your Journal Archive")
            
            # Show last 5 entries
            for i, entry in enumerate(reversed(st.session_state.journal_entries[-5:])):
                timestamp = entry['timestamp'].strftime('%d/%m/%Y %H:%M')
                
                with st.expander(f"📖 {entry['title']} - {timestamp}", expanded=i == 0):
                    col_content, col_meta = st.columns([3, 1])
                    
                    with col_content:
                        st.markdown(f"**Content:**")
                        st.write(entry['content'])
                    
                    with col_meta:
                        st.markdown(f"**Category:** {entry['category']}")
                        st.markdown(f"**Sentiment:** {entry['sentiment']}")
                        st.markdown(f"**Word Count:** {entry['word_count']}")
                        
                        if entry.get('tags'):
                            tags_display = ', '.join([tag.strip() for tag in entry['tags'].split(',')])
                            st.markdown(f"**Tags:** {tags_display}")
            
            # Journal Analytics
            st.markdown("### 📊 Writing Analytics")
            
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
            
            # Sentiment distribution
            sentiments = [entry['sentiment'] for entry in st.session_state.journal_entries]
            sentiment_counts = {s: sentiments.count(s) for s in set(sentiments)}
            
            if sentiment_counts:
                st.markdown("**😊 Sentiment Trends:**")
                for sentiment, count in sentiment_counts.items():
                    percentage = (count / total_entries) * 100
                    st.write(f"{sentiment}: **{count} entries** ({percentage:.1f}%)")
        
        else:
            st.info("📝 Your journal is empty! Start writing your first entry to begin your personal documentation journey.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Goals Tab
    with tab4:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 🎯 SMART Goals Manager")
        st.markdown("Set, track, and achieve your goals with intelligent progress monitoring.")
        
        # Add new goal form
        with st.expander("➕ Create New Goal", expanded=len(st.session_state.goals) == 0):
            with st.form("goal_form"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    goal_name = st.text_input(
                        "🎯 Goal Title:",
                        placeholder="Complete Python Course, Lose 10kg, Read 12 Books this year...",
                        key="goal_name"
                    )
                    
                    description = st.text_area(
                        "📝 Goal Description & Action Plan:",
                        placeholder="How will you achieve this goal? What are the key steps? What's your strategy?",
                        height=100,
                        key="goal_description"
                    )
                
                with col2:
                    category = st.selectbox(
                        "📁 Category:",
                        ["🏢 Career", "💪 Health", "📚 Learning", "💰 Finance", 
                         "👥 Relationships", "🎨 Hobbies", "🌍 Travel", "🏠 Personal"],
                        key="goal_category"
                    )
                    
                    priority = st.selectbox(
                        "⭐ Priority Level:",
                        ["🔴 High", "🟡 Medium", "🟢 Low"],
                        key="goal_priority"
                    )
                    
                    target_date = st.date_input(
                        "📅 Target Completion Date:",
                        min_value=datetime.date.today(),
                        value=datetime.date.today() + datetime.timedelta(days=90),
                        key="goal_target"
                    )
                
                if st.form_submit_button("🎯 Create Goal", type="primary", use_container_width=True):
                    if goal_name and description:
                        result = add_goal(st.session_state.username, goal_name, category, priority, target_date, description)
                        st.success(result)
                        st.balloons()
                        st.info("💡 **Pro Tip:** Break down your goal into smaller weekly milestones for better success!")
                    else:
                        st.error("🚨 Please provide both goal name and description!")
        
        # Display Active Goals
        if st.session_state.goals:
            active_goals = [goal for goal in st.session_state.goals if goal.get('status') == 'Active']
            completed_goals = [goal for goal in st.session_state.goals if goal.get('status') == 'Completed']
            
            if active_goals:
                st.markdown("### 🎯 Active Goals")
                
                for goal in active_goals:
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        
                        with col1:
                            st.markdown(f"**🎯 {goal['goal_name']}**")
                            st.caption(f"{goal['category']} | {goal['priority']}")
                            st.caption(f"📅 Target: {goal['target_date']}")
                            
                            # Progress bar
                            progress = st.slider(
                                f"Progress for: {goal['goal_name'][:30]}...",
                                0, 100, goal.get('progress', 0),
                                key=f"progress_{goal['id']}",
                                help="Update your progress percentage"
                            )
                            
                            # Update progress in session state
                            for g in st.session_state.goals:
                                if g['id'] == goal['id']:
                                    g['progress'] = progress
                                    if progress >= 100:
                                        g['status'] = 'Completed'
                        
                        with col2:
                            # Days calculation
                            if isinstance(goal['target_date'], str):
                                target = datetime.datetime.strptime(goal['target_date'], '%Y-%m-%d').date()
                            else:
                                target = goal['target_date']
                            
                            days_left = (target - datetime.date.today()).days
                            
                            if days_left > 0:
                                st.metric("📅 Days Left", days_left)
                            elif days_left == 0:
                                st.warning("⏰ Due Today!")
                            else:
                                st.error(f"⏰ {abs(days_left)} days overdue")
                        
                        with col3:
                            st.metric("📊 Progress", f"{progress}%")
                            
                            if progress >= 100:
                                st.success("🎉 Completed!")
                            elif progress >= 75:
                                st.info("🔥 Almost There!")
                            elif progress >= 50:
                                st.warning("📈 Good Progress")
                            else:
                                st.info("🚀 Getting Started")
                        
                        # Goal description
                        if goal.get('description'):
                            with st.expander("📋 View Goal Details"):
                                st.write(goal['description'])
                        
                        st.markdown("---")
            
            # Completed Goals
            if completed_goals:
                with st.expander(f"✅ Completed Goals ({len(completed_goals)})"):
                    for goal in completed_goals:
                        st.success(f"🎉 **{goal['goal_name']}** - {goal['category']}")
            
            # Goals Analytics
            st.markdown("### 📊 Goals Analytics")
            
            total_goals = len(st.session_state.goals)
            completed_count = len(completed_goals)
            avg_progress = sum([g.get('progress', 0) for g in st.session_state.goals]) / total_goals if total_goals > 0 else 0
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🎯 Total Goals", total_goals)
            with col2:
                st.metric("✅ Completed", completed_count)
            with col3:
                st.metric("📊 Avg Progress", f"{avg_progress:.1f}%")
            with col4:
                completion_rate = (completed_count / total_goals * 100) if total_goals > 0 else 0
                st.metric("🏆 Success Rate", f"{completion_rate:.1f}%")
        
        else:
            st.info("🎯 No goals set yet! Create your first goal above to start your achievement journey.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced Habits Tab
    with tab5:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 💪 Habit Builder & Streak Tracker")
        st.markdown("Build powerful habits with streak tracking and progress analytics.")
        
        # Add new habit
        with st.expander("➕ Create New Habit", expanded=len(st.session_state.habits) == 0):
            with st.form("habit_form"):
                col1, col2 = st.columns(2)
                
                with col1:
                    habit_name = st.text_input(
                        "💪 Habit Name:",
                        placeholder="Daily Exercise, Read 20 Pages, Drink 8 Glasses Water...",
                        key="habit_name"
                    )
                    
                    category = st.selectbox(
                        "🎯 Category:",
                        ["🏃 Health & Fitness", "📚 Learning", "💼 Productivity", 
                         "🧘 Wellness", "🎨 Creative", "💰 Financial", "👥 Social"],
                        key="habit_category"
                    )
                
                with col2:
                    frequency = st.selectbox(
                        "🔄 Target Frequency:",
                        ["Daily (7x/week)", "Weekdays (5x/week)", "3x per week", "Weekly"],
                        key="habit_frequency"
                    )
                    
                    st.markdown("**💡 Habit Success Tips:**")
                    st.caption("• Start small (2-minute rule)")
                    st.caption("• Be consistent over perfect")
                    st.caption("• Track your progress daily")
                
                if st.form_submit_button("💪 Create Habit", type="primary", use_container_width=True):
                    if habit_name:
                        result = add_habit(st.session_state.username, habit_name, category, frequency)
                        st.success(result)
                        st.balloons()
                        st.info("🔥 Great! Remember: It takes an average of 66 days to form a new habit. Stay consistent!")
                    else:
                        st.error("🚨 Please enter a habit name!")
        
        # Display and track habits
        if st.session_state.habits:
            st.markdown("### 🔥 Your Habit Dashboard")
            
            for habit in st.session_state.habits:
                with st.container():
                    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                    
                    with col1:
                        st.markdown(f"**💪 {habit['habit_name']}**")
                        st.caption(f"{habit['category']} | {habit['frequency']}")
                    
                    with col2:
                        current_streak = habit.get('current_streak', 0)
                        st.metric("🔥 Current Streak", f"{current_streak} days")
                        
                        # Streak emoji display
                        if current_streak >= 30:
                            st.markdown("🏆 **Habit Master!**")
                        elif current_streak >= 14:
                            st.markdown("🌟 **Great Streak!**")
                        elif current_streak >= 7:
                            st.markdown("🚀 **Building Momentum!**")
                        elif current_streak >= 3:
                            st.markdown("💪 **Getting Started!**")
                    
                    with col3:
                        total_completions = habit.get('total_completions', 0)
                        st.metric("✅ Total Done", total_completions)
                        
                        # Calculate success rate (mock calculation)
                        if total_completions > 0:
                            days_since_created = 7  # Mock data
                            success_rate = min((total_completions / days_since_created) * 100, 100)
                            st.caption(f"📊 {success_rate:.0f}% success rate")
                    
                    with col4:
                        # Mark as complete for today
                        today = datetime.date.today()
                        last_completed = habit.get('last_completed')
                        
                        if last_completed != today:
                            if st.button(f"✅ Done Today!", key=f"habit_complete_{habit['id']}", use_container_width=True):
                                # Update habit
                                for h in st.session_state.habits:
                                    if h['id'] == habit['id']:
                                        h['last_completed'] = today
                                        h['total_completions'] = h.get('total_completions', 0) + 1
                                        
                                        # Calculate streak
                                        if last_completed and (today - last_completed).days == 1:
                                            h['current_streak'] = h.get('current_streak', 0) + 1
                                        else:
                                            h['current_streak'] = 1
                                        
                                st.success(f"🔥 Awesome! Streak: {habit.get('current_streak', 1)} days!")
                                st.rerun()
                        else:
                            st.success("✅ Done Today!")
                    
                    # Visual streak representation
                    streak = habit.get('current_streak', 0)
                    if streak > 0:
                        streak_visual = "🔥" * min(streak, 15)
                        if streak > 15:
                            streak_visual += f" (+{streak - 15})"
                        st.caption(f"Streak: {streak_visual}")
                    
                    st.markdown("---")
            
            # Habits Analytics
            st.markdown("### 📊 Habits Analytics")
            
            total_habits = len(st.session_state.habits)
            total_completions = sum([h.get('total_completions', 0) for h in st.session_state.habits])
            max_streak = max([h.get('current_streak', 0) for h in st.session_state.habits]) if st.session_state.habits else 0
            active_streaks = len([h for h in st.session_state.habits if h.get('current_streak', 0) > 0])
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("💪 Total Habits", total_habits)
            with col2:
                st.metric("✅ Total Completions", total_completions)
            with col3:
                st.metric("🔥 Longest Streak", f"{max_streak} days")
            with col4:
                st.metric("🎯 Active Streaks", active_streaks)
            
            # Habit categories breakdown
            categories = [h['category'] for h in st.session_state.habits]
            category_counts = {cat: categories.count(cat) for cat in set(categories)}
            
            if category_counts:
                st.markdown("**📊 Habits by Category:**")
                for category, count in category_counts.items():
                    percentage = (count / total_habits) * 100
                    st.write(f"{category}: **{count} habits** ({percentage:.1f}%)")
        
        else:
            st.info("💪 No habits created yet! Start building your first positive habit above.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced Tasks Tab
    with tab6:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 📋 Smart Task Management")
        st.markdown("Organize and prioritize your tasks with intelligent workflow management.")
        
        # Add new task
        with st.expander("➕ Add New Task", expanded=len(st.session_state.tasks) == 0):
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
                        placeholder="Additional context, requirements, or notes for this task...",
                        height=80,
                        key="task_description"
                    )
                
                with col2:
                    priority = st.selectbox(
                        "🚨 Priority Level:",
                        ["🔴 Urgent & Important", "🟡 Important", "🟢 Normal", "⚪ Low"],
                        key="task_priority"
                    )
                    
                    due_date = st.date_input(
                        "📅 Due Date:",
                        min_value=datetime.date.today(),
                        value=datetime.date.today() + datetime.timedelta(days=1),
                        key="task_due"
                    )
                    
                    category = st.selectbox(
                        "📁 Category:",
                        ["💼 Work", "🏠 Personal", "🛒 Shopping", "💊 Health", 
                         "📚 Learning", "👥 Social", "💰 Finance", "🎯 Goals"],
                        key="task_category"
                    )
                
                if st.form_submit_button("📋 Add Task", type="primary", use_container_width=True):
                    if task_title:
                        result = add_task(st.session_state.username, task_title, priority, due_date, category, description)
                        st.success(result)
                        st.balloons()
                    else:
                        st.error("🚨 Please enter a task title!")
        
        # Display Tasks
        if st.session_state.tasks:
            pending_tasks = [task for task in st.session_state.tasks if task.get('status') == 'Pending']
            completed_tasks = [task for task in st.session_state.tasks if task.get('status') == 'Completed']
            
            # Pending Tasks
            if pending_tasks:
                st.markdown("### ⏳ Pending Tasks")
                
                # Sort by priority and due date
                priority_order = {"🔴 Urgent & Important": 1, "🟡 Important": 2, "🟢 Normal": 3, "⚪ Low": 4}
                pending_tasks.sort(key=lambda x: (priority_order.get(x.get('priority', '🟢 Normal'), 3), x.get('due_date', datetime.date.today())))
                
                for task in pending_tasks:
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        
                        with col1:
                            st.markdown(f"**{task['priority']} {task['task_title']}**")
                            st.caption(f"{task['category']} | Due: {task['due_date']}")
                            if task.get('description'):
                                st.caption(f"📝 {task['description'][:100]}...")
                        
                        with col2:
                            # Due date status
                            due_date = task['due_date']
                            if isinstance(due_date, str):
                                due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
                            
                            days_until_due = (due_date - datetime.date.today()).days
                            
                            if days_until_due < 0:
                                st.error(f"⏰ {abs(days_until_due)} days overdue")
                            elif days_until_due == 0:
                                st.warning("⚡ Due Today!")
                            elif days_until_due == 1:
                                st.warning("📅 Due Tomorrow")
                            else:
                                st.info(f"📅 {days_until_due} days left")
                        
                        with col3:
                            if st.button("✅ Complete", key=f"complete_task_{task['id']}", use_container_width=True):
                                # Mark task as completed
                                for t in st.session_state.tasks:
                                    if t['id'] == task['id']:
                                        t['status'] = 'Completed'
                                        t['completed_at'] = datetime.datetime.now()
                                
                                st.success("🎉 Task completed! Great job!")
                                st.rerun()
                        
                        st.markdown("---")
            
            # Completed Tasks
            if completed_tasks:
                with st.expander(f"✅ Completed Tasks ({len(completed_tasks)})"):
                    for task in completed_tasks[-5:]:  # Show last 5 completed
                        completed_at = task.get('completed_at')
                        if completed_at:
                            if isinstance(completed_at, str):
                                time_str = completed_at
                            else:
                                time_str = completed_at.strftime('%d/%m/%Y %H:%M')
                        else:
                            time_str = "Recently"
                        
                        st.success(f"✅ **{task['task_title']}** - Completed {time_str}")
            
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
            
            # Priority and category breakdown
            if pending_tasks:
                priorities = [task.get('priority', 'Normal') for task in pending_tasks]
                priority_counts = {p: priorities.count(p) for p in set(priorities)}
                
                st.markdown("**🚨 Pending Tasks by Priority:**")
                for priority, count in sorted(priority_counts.items()):
                    st.write(f"{priority}: **{count} tasks**")
        
        else:
            st.info("📋 No tasks yet! Add your first task above to start organizing your workflow.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced AI Chat Tab
    with tab7:
        st.markdown('<div class="modern-card animate-fade-in">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI Companion - Your Hinglish Productivity Coach")
        st.markdown("Chat with your AI companion for motivation, guidance, and personalized advice!")
        
        # Chat interface
        chat_container = st.container()
        
        with chat_container:
            # Display chat history
            if st.session_state.chat_history:
                st.markdown("### 💬 Conversation History")
                
                for i, (speaker, message, timestamp) in enumerate(st.session_state.chat_history[-10:]):
                    if speaker == "You":
                        st.markdown(f"""
                        <div class="chat-user">
                            <strong>👤 {st.session_state.username}</strong> 
                            <small style="opacity: 0.7;">({timestamp})</small><br>
                            {message}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="chat-ai">
                            <strong>🤖 AniGPT</strong> 
                            <small style="opacity: 0.7;">({timestamp})</small><br>
                            {message}
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("🌟 Start a conversation! Ask me about productivity, motivation, goals, or just chat casually in Hinglish!")
        
        # Chat input
        with st.form("chat_form", clear_on_submit=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                user_input = st.text_input(
                    "💬 Message:",
                    placeholder="Ask me anything! Motivation chahiye? Goals set karne hain? Ya bas casual chat?",
                    key="chat_input"
                )
            
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                send_button = st.form_submit_button("📤 Send", type="primary", use_container_width=True)
        
            if send_button and user_input:
                # Get AI response
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
        st.markdown("### ⚡ Quick AI Commands")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("💡 Daily Motivation", key="ai_motivation", use_container_width=True):
                motivational_quotes = [
                    "🌟 Har din ek naya chance hai apne goals ke kareeb jaane ka!",
                    "💪 Small steps daily taken = Big dreams surely awakened!",
                    "🚀 Consistency is the mother of mastery. Keep going!",
                    "🎯 Focus on progress, not perfection. You're doing amazing!",
                    "⚡ Your potential is unlimited. Believe and achieve!"
                ]
                motivation = random.choice(motivational_quotes)
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", motivation, current_time))
                st.rerun()
        
        with col2:
            if st.button("📊 Progress Review", key="ai_stats", use_container_width=True):
                # Generate personalized stats message
                mood_count = len(st.session_state.mood_entries)
                goal_progress = sum([g.get('progress', 0) for g in st.session_state.goals]) / len(st.session_state.goals) if st.session_state.goals else 0
                
                stats_msg = f"""
📊 **{st.session_state.username} ka Progress Report:**

🎯 **Goals Status:** {len(st.session_state.goals)} active goals, {goal_progress:.1f}% average progress
😊 **Mood Tracking:** {mood_count} entries logged - great self-awareness!
💪 **Habits:** {len(st.session_state.habits)} habits being tracked
📋 **Tasks:** {len([t for t in st.session_state.tasks if t.get('status') == 'Pending'])} pending tasks

**Overall:** You're doing fantastic! Consistency is key. Keep growing! 🚀
                """
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", stats_msg, current_time))
                st.rerun()
        
        with col3:
            if st.button("🎯 Goal Guidance", key="ai_goal_help", use_container_width=True):
                goal_tips = [
                    "🎯 SMART goals banao: Specific, Measurable, Achievable, Relevant, Time-bound!",
                    "📈 Big goals ko small milestones me break karo. Daily progress track karo!",
                    "🎖️ Goal achieve karne ka formula: Clear vision + Consistent action + Progress tracking!",
                    "💡 Visualization technique use karo. Goal achieve hone ke baad kaise feel karoge?",
                    "🚀 Action beats intention. Start small, but start today!"
                ]
                tip = random.choice(goal_tips)
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.chat_history.append(("AI", tip, current_time))
                st.rerun()
        
        # Chat controls
        st.markdown("---")
        col_clear, col_export = st.columns(2)
        
        with col_clear:
            if st.button("🗑️ Clear Chat History", key="clear_all_chat", use_container_width=True):
                st.session_state.chat_history = []
                st.success("Chat history cleared!")
                st.rerun()
        
        with col_export:
            if st.button("💾 Export Chat", key="export_chat", use_container_width=True):
                if st.session_state.chat_history:
                    chat_text = "\n".join([f"{speaker} ({timestamp}): {message}" for speaker, message, timestamp in st.session_state.chat_history])
                    st.text_area("📝 Your Chat History:", chat_text, height=200)
                else:
                    st.info("No chat history to export!")
        
        # Suggested conversation starters
        st.markdown("### 💡 Conversation Starters")
        
        suggestions = [
            "Mood down hai, motivation chahiye",
            "Goals set karne me help karo",
            "Habits kaise banau consistently?", 
            "Time management tips do",
            "Procrastination kaise overcome karu?",
            "Work-life balance kaise maintain karu?"
        ]
        
        cols = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(f"💬 {suggestion}", key=f"suggest_{i}", use_container_width=True):
                    ai_response = ai_chat_hinglish(suggestion)
                    current_time = datetime.datetime.now().strftime("%H:%M")
                    st.session_state.chat_history.append(("You", suggestion, current_time))
                    st.session_state.chat_history.append(("AI", ai_response, current_time))
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="
        text-align: center;
        padding: 30px;
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 30px 0;
        backdrop-filter: blur(15px);
    ">
        <h3 style="
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        ">
            🚀 AniGPT V2 - Personal Productivity Command Center
        </h3>
        <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; margin-bottom: 10px;">
            <strong>Track • Analyze • Improve • Achieve</strong>
        </p>
        <p style="color: rgba(255,255,255,0.7); font-size: 0.9rem; margin-bottom: 15px;">
            User: <strong>{st.session_state.username}</strong> | 
            Session: {len(st.session_state.mood_entries + st.session_state.journal_entries + st.session_state.goals + st.session_state.habits + st.session_state.tasks)} total entries
        </p>
        <p style="color: rgba(255,255,255,0.6); font-size: 0.8rem;">
            Made with ❤️ and AI | Your growth journey continues! 🌟
        </p>
    </div>
    """, unsafe_allow_html=True)
