"""
Mines Alumni Board (MAB) Initiatives Page
Updates on Lifelong Learning & Development initiatives.
"""
import streamlit as st
from pathlib import Path
import sys
import json
from datetime import datetime
import pandas as pd

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import FOCUS_AREAS, SME_APPLICATION_LINK


def load_sme_recommendations():
    """Load SME recommendations from JSON file."""
    data_path = Path(__file__).parent.parent / "data"
    submissions_file = data_path / "sme_recommendations.json"
    
    if submissions_file.exists():
        try:
            with open(submissions_file, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

st.set_page_config(
    page_title="MAB Initiatives | Mines",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Mines Alumni Board Initiatives")
st.markdown("*Lifelong Learning & Development (ProEd Focus)*")

st.divider()

# Overview
st.markdown("""
The **Mines Alumni Board (MAB)** is actively supporting the growth of Professional Education 
through targeted initiatives. Below are the key focus areas and how you can contribute.
""")

# Tabs for different initiatives
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 SME Search",
    "📣 ProEd Promotion", 
    "🤖 AI for ProEd",
    "📝 Alumni Feedback"
])

# Tab 1: SME Search
with tab1:
    st.header("🔍 SME Recruitment Initiative")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **MAB Initiative:** Create a focused recruitment plan and begin making 
        targeted alumni introductions for Subject Matter Expert roles.
        
        We're seeking alumni experts in the following domains:
        """)
        
        for i, area in enumerate(FOCUS_AREAS):
            icons = ["🔋", "🤖", "📈", "⛏️", "🚀", "🏗️"]
            st.markdown(f"- {icons[i]} {area}")
        
        st.divider()
        
        st.link_button(
            "📝 Official SME Application",
            SME_APPLICATION_LINK,
            type="primary"
        )
    
    with col2:
        st.subheader("📤 Recommend an Alumni SME")
        st.markdown("*Know a Mines alum who would be a great SME? Submit their info below!*")
        
        with st.form("sme_recommendation_form"):
            st.markdown("#### Recommended Alumni Information")
            
            alumni_name = st.text_input(
                "Alumni Name *",
                placeholder="John Smith"
            )
            
            linkedin_url = st.text_input(
                "LinkedIn Profile URL *",
                placeholder="https://www.linkedin.com/in/..."
            )
            
            domain = st.selectbox(
                "Primary Domain Expertise *",
                options=[
                    "Select a domain...",
                    "Energy - Traditional Sources",
                    "Energy - Nuclear",
                    "Energy - Geothermal",
                    "AI Use in Industry",
                    "Executive Education in STEM",
                    "Mining & Minerals",
                    "Aerospace",
                    "Construction Engineering",
                    "Other"
                ]
            )
            
            other_domain = st.text_input(
                "If 'Other', please specify:",
                placeholder="Specify domain area"
            )
            
            email = st.text_input(
                "Alumni's Email (if known)",
                placeholder="email@example.com"
            )
            
            notes = st.text_area(
                "Additional Notes",
                placeholder="Why would this person be a great SME? Any relevant experience?",
                height=100
            )
            
            st.divider()
            
            st.markdown("#### Your Contact Information")
            
            your_name = st.text_input(
                "Your Name *",
                placeholder="Your full name"
            )
            
            your_email = st.text_input(
                "Your Email *",
                placeholder="your.email@example.com"
            )
            
            submitted = st.form_submit_button(
                "Submit Recommendation",
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                # Validate required fields
                if not alumni_name:
                    st.error("Please enter the alumni's name.")
                elif not linkedin_url:
                    st.error("Please enter the LinkedIn profile URL.")
                elif domain == "Select a domain...":
                    st.error("Please select a domain expertise.")
                elif not your_name:
                    st.error("Please enter your name.")
                elif not your_email:
                    st.error("Please enter your email.")
                else:
                    # Store submission (in production, this would go to a database)
                    submission = {
                        "timestamp": datetime.now().isoformat(),
                        "alumni_name": alumni_name,
                        "linkedin_url": linkedin_url,
                        "domain": other_domain if domain == "Other" else domain,
                        "alumni_email": email,
                        "notes": notes,
                        "submitted_by": your_name,
                        "submitter_email": your_email
                    }
                    
                    # Save to a local JSON file (for demo purposes)
                    data_path = Path(__file__).parent.parent / "data"
                    submissions_file = data_path / "sme_recommendations.json"
                    
                    try:
                        if submissions_file.exists():
                            with open(submissions_file, "r") as f:
                                submissions = json.load(f)
                        else:
                            submissions = []
                        
                        submissions.append(submission)
                        
                        with open(submissions_file, "w") as f:
                            json.dump(submissions, f, indent=2)
                        
                        st.success(f"""
                        ✅ **Thank you for your recommendation!**
                        
                        You've recommended **{alumni_name}** as a potential SME in **{submission['domain']}**.
                        
                        The MAB team will review this recommendation and reach out if appropriate.
                        """)
                        
                    except Exception as e:
                        st.warning(f"Recommendation recorded (note: {str(e)})")
                        st.success(f"Thank you for recommending {alumni_name}!")
    
    # Display existing recommendations in a table
    st.divider()
    st.subheader("📋 Current SME Recommendations")
    
    recommendations = load_sme_recommendations()
    
    if recommendations:
        # Create DataFrame for display
        df = pd.DataFrame(recommendations)
        
        # Format the timestamp
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['Date Submitted'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')
        
        # Create clickable LinkedIn links
        df['LinkedIn'] = df['linkedin_url'].apply(
            lambda x: f'<a href="{x}" target="_blank">View Profile</a>' if x else ''
        )
        
        # Select and rename columns for display
        display_df = df[[
            'alumni_name', 
            'domain', 
            'alumni_email',
            'linkedin_url',
            'notes',
            'submitted_by', 
            'Date Submitted'
        ]].copy()
        
        display_df.columns = [
            'Alumni Name', 
            'Domain Expertise', 
            'Email',
            'LinkedIn URL',
            'Notes',
            'Recommended By', 
            'Date Submitted'
        ]
        
        # Display metrics
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        with metric_col1:
            st.metric("Total Recommendations", len(recommendations))
        with metric_col2:
            domains = df['domain'].nunique()
            st.metric("Unique Domains", domains)
        with metric_col3:
            recommenders = df['submitted_by'].nunique()
            st.metric("Contributors", recommenders)
        
        st.markdown("---")
        
        # Display the table with nice formatting
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Alumni Name": st.column_config.TextColumn(
                    "Alumni Name",
                    width="medium",
                ),
                "Domain Expertise": st.column_config.TextColumn(
                    "Domain Expertise",
                    width="medium",
                ),
                "Email": st.column_config.TextColumn(
                    "Email",
                    width="medium",
                ),
                "LinkedIn URL": st.column_config.LinkColumn(
                    "LinkedIn",
                    width="medium",
                    display_text="View Profile"
                ),
                "Notes": st.column_config.TextColumn(
                    "Notes",
                    width="large",
                ),
                "Recommended By": st.column_config.TextColumn(
                    "Recommended By",
                    width="medium",
                ),
                "Date Submitted": st.column_config.TextColumn(
                    "Date Submitted",
                    width="small",
                ),
            }
        )
        
        # Domain breakdown
        with st.expander("📊 Recommendations by Domain"):
            domain_counts = df['domain'].value_counts().reset_index()
            domain_counts.columns = ['Domain', 'Count']
            
            st.bar_chart(domain_counts.set_index('Domain'))
    else:
        st.info("No SME recommendations have been submitted yet. Be the first to recommend an alumni!")

# Tab 2: ProEd Promotion
with tab2:
    st.header("📣 ProEd Promotion Opportunities")
    
    st.markdown("""
    The MAB is promoting ProEd through various channels to increase awareness and enrollment.
    """)
    
    promo_col1, promo_col2 = st.columns(2)
    
    with promo_col1:
        st.subheader("🎪 Event Promotion")
        
        events = [
            ("🎓 Career Fair", "Connect with students and professionals about ProEd opportunities"),
            ("🏠 Homecoming", "Engage alumni during Homecoming events"),
            ("🌐 Alumni Portal", "Feature ProEd prominently on the alumni portal"),
            ("🎉 idigMines Events", "ProEd highlighted in mid-February events")
        ]
        
        for event, description in events:
            with st.container(border=True):
                st.markdown(f"**{event}**")
                st.caption(description)
    
    with promo_col2:
        st.subheader("📰 Media & Communications")
        
        with st.container(border=True):
            st.markdown("**📖 Mines Magazine**")
            st.markdown("Feature success stories of ProEd students")
            st.caption("Highlight real impact and outcomes")
        
        with st.container(border=True):
            st.markdown("**📧 Email Blast**")
            st.markdown("Share ProEd success stories with alumni network")
            st.caption("Reach thousands of Mines alumni")
        
        with st.container(border=True):
            st.markdown("**📋 Swipe Sheet**")
            st.markdown("Consistent messaging and promotional materials")
            st.caption("Available for all promotional needs")
    
    st.divider()
    
    st.info("""
    **📢 Help Us Spread the Word!**
    
    If you have a success story from ProEd or know someone who does, please reach out! 
    We'd love to feature it in our promotional materials.
    """)

# Tab 3: AI for ProEd
with tab3:
    st.header("🤖 AI Integration for ProEd")
    
    st.markdown("""
    Exploring innovative ways to leverage AI in professional education course development and delivery.
    """)
    
    ai_col1, ai_col2 = st.columns(2)
    
    with ai_col1:
        with st.container(border=True):
            st.markdown("### 🎓 AI Teaching Assistant")
            st.markdown("""
            **Initiative:** Julian will work with Sam Spiegel and course SMEs to develop 
            AI-powered teaching assistants for ProEd courses.
            
            **Benefits:**
            - 24/7 student support
            - Instant answers to common questions
            - Personalized learning assistance
            - Scalable support for growing enrollment
            """)
            st.caption("Development collaboration with ProEd team")
    
    with ai_col2:
        with st.container(border=True):
            st.markdown("### 💰 AI Development Sponsorship")
            st.markdown("""
            **Initiative:** Julian will sponsor the initial overhead cost of using AI 
            for course development and deployment.
            
            **Coverage:**
            - AI model API costs
            - Development infrastructure
            - Initial deployment expenses
            - Pilot program resources
            """)
            st.caption("Reducing barriers to AI adoption")
    
    st.divider()
    
    st.subheader("🔮 Future AI Opportunities")
    
    future_col1, future_col2, future_col3 = st.columns(3)
    
    with future_col1:
        st.markdown("""
        **📝 Content Generation**
        
        AI-assisted creation of course materials, 
        quizzes, and assessments
        """)
    
    with future_col2:
        st.markdown("""
        **🎯 Personalization**
        
        Adaptive learning paths based on 
        student progress and goals
        """)
    
    with future_col3:
        st.markdown("""
        **📊 Analytics**
        
        AI-powered insights on student 
        engagement and outcomes
        """)

# Tab 4: Alumni Feedback
with tab4:
    st.header("📝 Alumni Feedback for Course Development")
    
    st.markdown("""
    Your input helps shape the future of ProEd! Tell us what courses you'd like to see offered.
    """)
    
    with st.form("course_feedback_form"):
        st.subheader("Suggest a Course Topic")
        
        course_topic = st.text_input(
            "Course Topic or Title *",
            placeholder="e.g., 'Advanced Data Analytics for Energy Industry'"
        )
        
        course_domain = st.selectbox(
            "Primary Domain",
            options=[
                "Select a domain...",
                "Energy - Traditional Sources",
                "Energy - Nuclear",
                "Energy - Geothermal",
                "AI Use in Industry",
                "Executive Education in STEM",
                "Mining & Minerals",
                "Aerospace",
                "Construction Engineering",
                "Other"
            ]
        )
        
        course_format = st.multiselect(
            "Preferred Format(s)",
            options=[
                "Online Self-Paced",
                "Online Facilitated",
                "In-Person",
                "Hybrid"
            ],
            default=["Online Self-Paced"]
        )
        
        course_description = st.text_area(
            "Course Description / What You'd Like to Learn",
            placeholder="Describe what topics the course should cover and what you hope to learn...",
            height=150
        )
        
        urgency = st.select_slider(
            "How urgently do you need this course?",
            options=["Not urgent", "Somewhat urgent", "Urgent", "Very urgent"]
        )
        
        st.divider()
        
        feedback_name = st.text_input("Your Name")
        feedback_email = st.text_input("Your Email")
        
        feedback_submitted = st.form_submit_button(
            "Submit Course Suggestion",
            type="primary",
            use_container_width=True
        )
        
        if feedback_submitted:
            if not course_topic:
                st.error("Please enter a course topic.")
            else:
                st.success(f"""
                ✅ **Thank you for your feedback!**
                
                Your suggestion for **"{course_topic}"** has been recorded.
                
                The ProEd team will review all suggestions when planning future course offerings.
                """)

# Sidebar
with st.sidebar:
    st.header("MAB Focus Areas")
    
    st.markdown("""
    **Key Initiatives:**
    
    1. 🔍 SME Recruitment
    2. 📣 ProEd Promotion
    3. 🤖 AI Integration
    4. 📝 Alumni Feedback
    """)
    
    st.divider()
    
    st.info("""
    **Get Involved!**
    
    Contact the MAB to learn how 
    you can contribute to these 
    initiatives.
    """)
