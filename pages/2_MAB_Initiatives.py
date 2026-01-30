import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="MAB Initiatives | Mines ProEd",
    page_icon="⛏️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap');
    
    .stApp { background-color: #FFFFFF; }
    .main .block-container { padding-top: 2rem; max-width: 1200px; }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif !important;
        color: #21314d !important;
    }
    h1 { font-weight: 700 !important; font-size: 2.5rem !important; }
    h2 {
        font-weight: 600 !important;
        border-bottom: 3px solid #CC4628;
        padding-bottom: 0.5rem;
        margin-top: 2rem !important;
    }
    h3 { font-weight: 600 !important; color: #09396C !important; }
    
    p, li, span, div {
        font-family: 'Open Sans', sans-serif !important;
        color: #21314d;
    }
    
    [data-testid="stSidebar"] { background-color: #21314d; }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; }
    
    .initiative-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #CFDCE9 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #CC4628;
        box-shadow: 0 4px 6px rgba(33, 49, 77, 0.1);
    }
    
    .number-badge {
        background: #CC4628;
        color: #FFFFFF !important;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        margin-right: 0.75rem;
    }
    
    .focus-area-tag {
        display: inline-block;
        background: #09396C;
        color: #FFFFFF !important;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.85rem;
    }
    
    .stButton > button {
        background-color: #CC4628;
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        border: none;
        border-radius: 8px;
    }
    .stButton > button:hover { background-color: #21314d; }
    
    .success-box {
        background: #80C342;
        color: #FFFFFF !important;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    
    a { color: #CC4628 !important; }
    
    /* Form styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        border: 2px solid #CFDCE9 !important;
        border-radius: 8px !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #09396C !important;
        box-shadow: 0 0 0 1px #09396C !important;
    }
</style>
""", unsafe_allow_html=True)

# Data file paths
DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SME_RECOMMENDATIONS_FILE = os.path.join(DATA_DIR, "data", "sme_recommendations.json")
COURSE_FEEDBACK_FILE = os.path.join(DATA_DIR, "data", "course_feedback.json")

def load_json_data(filepath):
    """Load data from JSON file, return empty list if file doesn't exist."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

def save_json_data(filepath, data):
    """Save data to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

# Sidebar
with st.sidebar:
    st.image("https://brand.mines.edu/wp-content/uploads/sites/425/2023/03/Mines-Logo-triangle-blue.png", width=80)
    st.markdown("### Mines ProEd")
    st.markdown("Mines Alumni Board Initiatives")
    st.divider()
    st.markdown("#### Quick Links")
    st.markdown("🔗 [ProEd Homepage](https://proed.mines.edu/)")
    st.markdown("🔗 [SME Application](https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV)")

# Header
st.markdown("# 🎓 Life Long Learning & Development")
st.markdown("### Mines Alumni Board (MAB) Initiatives for ProEd")
st.markdown("The MAB is actively supporting ProEd through targeted initiatives to help grow professional education at Mines.")

# Tabs for different initiatives
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 SME Search", 
    "📢 ProEd Promotion", 
    "🤖 AI for ProEd",
    "💬 Alumni Feedback"
])

# =============================================================================
# TAB 1: SME Search
# =============================================================================
with tab1:
    st.markdown("## 1. SME Search Initiative")
    st.markdown("""
    <div class="initiative-card">
        <p style="margin: 0;">
        <strong>Goal:</strong> MAB will create a focused recruitment plan and begin making targeted alumni introductions 
        to identify Subject Matter Experts for ProEd courses.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Focus Areas
    st.markdown("### Target Expertise Areas")
    focus_areas = [
        "Energy (nuclear, geothermal, traditional)",
        "AI Use in Industry",
        "Executive Education in STEM",
        "Mining & Minerals",
        "Aerospace",
        "Construction Engineering"
    ]
    
    area_html = " ".join([f'<span class="focus-area-tag">{area}</span>' for area in focus_areas])
    st.markdown(f'<div style="margin: 1rem 0;">{area_html}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # SME Recommendation Form
    st.markdown("### 📝 Recommend an Alumni SME")
    st.markdown("Know a Mines alumnus who would make an excellent Subject Matter Expert? Submit your recommendation below.")
    
    with st.form("sme_recommendation_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nominee_name = st.text_input("Nominee's Full Name *", placeholder="John Doe")
            linkedin_url = st.text_input("LinkedIn Profile URL *", placeholder="https://linkedin.com/in/username")
            expertise_area = st.selectbox(
                "Primary Expertise Area *",
                ["Select an area...", "Energy", "AI Use in Industry", "Executive Education in STEM", 
                 "Mining & Minerals", "Aerospace", "Construction Engineering", "Other"]
            )
        
        with col2:
            nominee_email = st.text_input("Nominee's Email (if known)", placeholder="john.doe@company.com")
            company = st.text_input("Current Company/Organization", placeholder="Company Name")
            graduation_year = st.text_input("Mines Graduation Year (if known)", placeholder="2010")
        
        reason = st.text_area(
            "Why would this person be a great SME?",
            placeholder="Describe their expertise, experience, and why you think they'd be a good fit...",
            height=100
        )
        
        recommender_name = st.text_input("Your Name", placeholder="Your full name")
        recommender_email = st.text_input("Your Email", placeholder="your.email@example.com")
        
        submitted = st.form_submit_button("Submit Recommendation", use_container_width=True)
        
        if submitted:
            if not nominee_name or not linkedin_url or expertise_area == "Select an area...":
                st.error("Please fill in all required fields (marked with *).")
            else:
                # Load existing recommendations
                recommendations = load_json_data(SME_RECOMMENDATIONS_FILE)
                
                # Add new recommendation
                new_rec = {
                    "id": len(recommendations) + 1,
                    "nominee_name": nominee_name,
                    "linkedin_url": linkedin_url,
                    "nominee_email": nominee_email,
                    "expertise_area": expertise_area,
                    "company": company,
                    "graduation_year": graduation_year,
                    "reason": reason,
                    "recommender_name": recommender_name,
                    "recommender_email": recommender_email,
                    "submitted_at": datetime.now().isoformat()
                }
                recommendations.append(new_rec)
                
                # Save to file
                save_json_data(SME_RECOMMENDATIONS_FILE, recommendations)
                
                st.success("✅ Thank you! Your recommendation has been submitted successfully.")
                st.balloons()
    
    # Display existing recommendations
    st.markdown("---")
    st.markdown("### 📋 Current SME Recommendations")
    
    recommendations = load_json_data(SME_RECOMMENDATIONS_FILE)
    
    if recommendations:
        # Create a display dataframe
        display_data = []
        for rec in recommendations:
            display_data.append({
                "Name": rec.get("nominee_name", ""),
                "Expertise": rec.get("expertise_area", ""),
                "Company": rec.get("company", ""),
                "LinkedIn": rec.get("linkedin_url", ""),
                "Grad Year": rec.get("graduation_year", ""),
                "Submitted": rec.get("submitted_at", "")[:10] if rec.get("submitted_at") else ""
            })
        
        st.dataframe(
            display_data,
            column_config={
                "Name": st.column_config.TextColumn("Name", width="medium"),
                "Expertise": st.column_config.TextColumn("Expertise Area", width="medium"),
                "Company": st.column_config.TextColumn("Company", width="medium"),
                "LinkedIn": st.column_config.LinkColumn("LinkedIn", width="medium"),
                "Grad Year": st.column_config.TextColumn("Year", width="small"),
                "Submitted": st.column_config.TextColumn("Date", width="small")
            },
            hide_index=True,
            use_container_width=True
        )
    else:
        st.info("No recommendations submitted yet. Be the first to recommend an alumni SME!")

# =============================================================================
# TAB 2: ProEd Promotion
# =============================================================================
with tab2:
    st.markdown("## 2. ProEd Promotion")
    st.markdown("""
    <div class="initiative-card">
        <p><strong>Status:</strong> ProEd is in the awareness-building phase. Word of mouth and opportunities to make 
        alumni aware of the program are greatly appreciated.</p>
        <p style="margin-bottom: 0;"><strong>Upcoming:</strong> ProEd will be one of the highlighted causes during <strong>idigMines events in mid-February</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Promotion Channels")
    
    channels = [
        ("🎪", "Career Fair", "Promote ProEd at Mines career events"),
        ("🏠", "Homecoming", "Engage alumni during homecoming activities"),
        ("📰", "Mines Magazine", "Feature success stories and program highlights"),
        ("🌐", "Alumni Portal", "Leverage the digital alumni network")
    ]
    
    col1, col2 = st.columns(2)
    for i, (icon, title, desc) in enumerate(channels):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style="background: #CFDCE9; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <h4 style="margin: 0;">{icon} {title}</h4>
                <p style="margin: 0.5rem 0 0 0; color: #75757D; font-size: 0.9rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 Success Story Initiative")
    st.markdown("""
    <div class="initiative-card">
        <h4 style="margin-top: 0;">Feature ProEd Student Success Stories</h4>
        <ul>
            <li>Highlight in <strong>Mines Magazine</strong></li>
            <li>Include in email blasts to alumni network</li>
            <li>Share on alumni portal and social media</li>
        </ul>
        <p style="margin-bottom: 0;"><em>Know a ProEd success story? Contact the MAB to share it!</em></p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# TAB 3: AI for ProEd
# =============================================================================
with tab3:
    st.markdown("## 3. AI for ProEd")
    st.markdown("""
    <div class="initiative-card">
        <h4 style="margin-top: 0;">🤖 AI Teaching Assistant Initiative</h4>
        <p><strong>Lead:</strong> Julian Liu (MAB member)</p>
        <p>Working with Sam Spiegel and course SMEs to develop AI-powered teaching assistants for ProEd courses.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #21314d; padding: 1.5rem; border-radius: 12px; color: #FFFFFF;">
            <h4 style="color: #FFFFFF !important; margin-top: 0;">📚 Course Development</h4>
            <p style="color: #CFDCE9 !important;">Julian will work with Sam Spiegel and course SMEs to use AI 
            to develop course AI teaching assistants.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #21314d; padding: 1.5rem; border-radius: 12px; color: #FFFFFF;">
            <h4 style="color: #FFFFFF !important; margin-top: 0;">💰 Sponsorship</h4>
            <p style="color: #CFDCE9 !important;">Julian will sponsor the initial overhead cost of using AI 
            for course development and deployment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Current Status")
    st.markdown("""
    Sam Spiegel is open to conversations about using AI both in courses and in promotion. 
    
    **Note:** The HiTA (Human-in-the-loop Teaching Assistant) program is currently only available for credit-bearing courses, 
    not for ProEd professional education offerings.
    """)

# =============================================================================
# TAB 4: Alumni Feedback
# =============================================================================
with tab4:
    st.markdown("## 4. Alumni Course Feedback")
    st.markdown("""
    <div class="initiative-card">
        <p style="margin: 0;">Help shape the future of ProEd by sharing your ideas for new courses. 
        What skills would help you in your career? What topics should Mines offer?</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("course_feedback_form"):
        st.markdown("### 💡 Submit Course Ideas")
        
        course_topic = st.text_input(
            "Course Topic Suggestion *",
            placeholder="e.g., Machine Learning for Oil & Gas Applications"
        )
        
        course_description = st.text_area(
            "Describe what this course should cover",
            placeholder="What specific skills or knowledge should the course teach? Who would benefit from it?",
            height=100
        )
        
        col1, col2 = st.columns(2)
        with col1:
            format_preference = st.selectbox(
                "Preferred Format",
                ["No preference", "Self-paced online", "Online facilitated", "In-person", "Hybrid"]
            )
        with col2:
            urgency = st.selectbox(
                "How important is this topic?",
                ["Nice to have", "Important", "Critical for my career"]
            )
        
        additional_comments = st.text_area(
            "Additional Comments",
            placeholder="Any other thoughts or suggestions...",
            height=80
        )
        
        feedback_name = st.text_input("Your Name (optional)", placeholder="Your name")
        feedback_email = st.text_input("Your Email (optional)", placeholder="your.email@example.com")
        
        feedback_submitted = st.form_submit_button("Submit Feedback", use_container_width=True)
        
        if feedback_submitted:
            if not course_topic:
                st.error("Please provide a course topic suggestion.")
            else:
                # Load existing feedback
                feedback_data = load_json_data(COURSE_FEEDBACK_FILE)
                
                # Add new feedback
                new_feedback = {
                    "id": len(feedback_data) + 1,
                    "course_topic": course_topic,
                    "course_description": course_description,
                    "format_preference": format_preference,
                    "urgency": urgency,
                    "additional_comments": additional_comments,
                    "name": feedback_name,
                    "email": feedback_email,
                    "submitted_at": datetime.now().isoformat()
                }
                feedback_data.append(new_feedback)
                
                # Save to file
                save_json_data(COURSE_FEEDBACK_FILE, feedback_data)
                
                st.success("✅ Thank you for your feedback! Your suggestion has been recorded.")
    
    # Display summary of feedback
    st.markdown("---")
    st.markdown("### 📊 Course Interest Summary")
    
    feedback_data = load_json_data(COURSE_FEEDBACK_FILE)
    
    if feedback_data:
        # Count submissions by urgency
        urgency_counts = {}
        for fb in feedback_data:
            u = fb.get("urgency", "Nice to have")
            urgency_counts[u] = urgency_counts.get(u, 0) + 1
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Suggestions", len(feedback_data))
        with col2:
            critical = urgency_counts.get("Critical for my career", 0)
            st.metric("Critical Topics", critical)
        with col3:
            important = urgency_counts.get("Important", 0)
            st.metric("Important Topics", important)
        
        # Show recent topics
        st.markdown("#### Recent Course Suggestions")
        recent = feedback_data[-5:][::-1]  # Last 5, reversed
        for fb in recent:
            st.markdown(f"""
            <div style="background: #CFDCE9; padding: 0.75rem 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <strong>{fb.get('course_topic', 'Untitled')}</strong>
                <span style="color: #75757D; font-size: 0.85rem;"> — {fb.get('format_preference', 'No preference')}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No course suggestions yet. Be the first to share your ideas!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #75757D; padding: 1rem;">
    <p>Mines Alumni Board | Life Long Learning & Development Committee<br>
    <small>Supporting professional education for Mines alumni and industry professionals</small></p>
</div>
""", unsafe_allow_html=True)
