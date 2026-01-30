import streamlit as st

st.set_page_config(
    page_title="MAAG Updates | Mines AI/ML",
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
    
    .hero-banner {
        background: linear-gradient(135deg, #21314d 0%, #09396C 100%);
        padding: 2.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .hero-banner h1, .hero-banner p {
        color: #FFFFFF !important;
    }
    
    .stat-card {
        background: #21314d;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .stat-card h2, .stat-card p {
        color: #FFFFFF !important;
        margin: 0;
    }
    
    .stat-number {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #CC4628 !important;
    }
    
    .mentor-area-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #CFDCE9 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.75rem 0;
        border-left: 5px solid #CC4628;
        box-shadow: 0 4px 6px rgba(33, 49, 77, 0.1);
        transition: transform 0.2s ease;
    }
    
    .mentor-area-card:hover {
        transform: translateX(5px);
    }
    
    .icon-circle {
        background: #CC4628;
        color: #FFFFFF;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 30px;
        padding-bottom: 1.5rem;
        border-left: 3px solid #879EC3;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 16px;
        height: 16px;
        background: #CC4628;
        border-radius: 50%;
    }
    
    .highlight-stat {
        background: #CFDCE9;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    
    a { color: #CC4628 !important; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://brand.mines.edu/wp-content/uploads/sites/425/2023/03/Mines-Logo-triangle-blue.png", width=80)
    st.markdown("### MAAG")
    st.markdown("Mines AI/ML Affinity Group")
    st.divider()
    st.markdown("#### About MAAG")
    st.markdown("""
    The Mines AI/ML Affinity Group connects 
    alumni working in artificial intelligence 
    and machine learning with current students.
    """)

# Hero Banner
st.markdown("""
<div class="hero-banner">
    <h1 style="margin-bottom: 0.5rem;">🤖 Mines AI/ML Affinity Group</h1>
    <p style="font-size: 1.2rem; margin-bottom: 0;">Student Mentoring Initiative | Spring 2026</p>
</div>
""", unsafe_allow_html=True)

# Key Statistics
st.markdown("## Program Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-number">10+</p>
        <p style="font-size: 1.1rem;">Alumni Mentors</p>
        <p style="font-size: 0.9rem; color: #879EC3 !important;">Working in AI/ML</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-number">5</p>
        <p style="font-size: 1.1rem;">Mentoring Areas</p>
        <p style="font-size: 0.9rem; color: #879EC3 !important;">Career to Technical</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <p class="stat-number">Spring '26</p>
        <p style="font-size: 1.1rem;">Launch Date</p>
        <p style="font-size: 0.9rem; color: #879EC3 !important;">Now Recruiting</p>
    </div>
    """, unsafe_allow_html=True)

# Program Description
st.markdown("## About the Mentoring Program")

st.markdown("""
<div style="background: linear-gradient(135deg, #FFFFFF 0%, #CFDCE9 100%); 
            padding: 2rem; border-radius: 12px; margin: 1rem 0;
            border-left: 5px solid #CC4628;">
    <p style="font-size: 1.1rem; margin: 0;">
    The Mines AI/ML Affinity Group (MAAG) has invited <strong>10+ alumni</strong> currently working in the AI/ML field 
    to serve as mentors for Mines students starting <strong>Spring 2026</strong>.
    </p>
    <p style="margin: 1rem 0 0 0; color: #75757D;">
    This initiative connects students with industry professionals who can provide guidance, 
    share real-world experience, and help shape the next generation of AI/ML practitioners.
    </p>
</div>
""", unsafe_allow_html=True)

# Mentoring Areas
st.markdown("## Mentoring Areas")
st.markdown("Alumni mentors can help students in the following areas:")

mentoring_areas = [
    {
        "icon": "🎯",
        "title": "Career Paths & Industry Perspective",
        "description": "Navigate the AI/ML job market, understand different career trajectories, and learn what companies are looking for in candidates.",
        "examples": ["Data Scientist vs ML Engineer roles", "Startup vs Enterprise paths", "Industry trends and opportunities"]
    },
    {
        "icon": "💻",
        "title": "AI/ML Technical Skills & Project Guidance",
        "description": "Get hands-on help with technical concepts, frameworks, and real-world project implementation.",
        "examples": ["Model selection and training", "MLOps and deployment", "Code reviews and best practices"]
    },
    {
        "icon": "📝",
        "title": "Resume, Interviewing & Job Search",
        "description": "Prepare compelling applications and ace technical interviews at top companies.",
        "examples": ["Resume optimization", "Technical interview prep", "Behavioral question strategies"]
    },
    {
        "icon": "🎓",
        "title": "Graduate School & Research Advice",
        "description": "Explore advanced degree options, research opportunities, and academic career paths.",
        "examples": ["MS vs PhD decisions", "Research lab selection", "Application strategies"]
    },
    {
        "icon": "📈",
        "title": "Leadership, Communication & Career Growth",
        "description": "Develop soft skills essential for advancing from individual contributor to leadership roles.",
        "examples": ["Technical communication", "Team leadership", "Stakeholder management"]
    }
]

col1, col2 = st.columns(2)

for i, area in enumerate(mentoring_areas):
    with col1 if i % 2 == 0 else col2:
        with st.expander(f"{area['icon']} **{area['title']}**", expanded=i < 2):
            st.markdown(area['description'])
            st.markdown("**Example topics:**")
            for ex in area['examples']:
                st.markdown(f"- {ex}")

# How It Works
st.markdown("## How the Program Works")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="timeline-item">
        <h4 style="margin-top: 0;">1. Mentor Recruitment</h4>
        <p style="color: #75757D;">MAAG identifies and invites alumni working in AI/ML to participate as mentors.</p>
    </div>
    
    <div class="timeline-item">
        <h4 style="margin-top: 0;">2. Student Sign-Up</h4>
        <p style="color: #75757D;">Students express interest and indicate which mentoring areas they need help with.</p>
    </div>
    
    <div class="timeline-item">
        <h4 style="margin-top: 0;">3. Matching</h4>
        <p style="color: #75757D;">MAAG facilitates introductions between students and mentors based on interests and goals.</p>
    </div>
    
    <div class="timeline-item">
        <h4 style="margin-top: 0;">4. Mentoring Sessions</h4>
        <p style="color: #75757D;">Mentors and students connect for guidance, advice, and professional development.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: #21314d; padding: 1.5rem; border-radius: 12px; height: 100%;">
        <h4 style="color: #FFFFFF !important; margin-top: 0;">🗓️ Timeline</h4>
        <p style="color: #CFDCE9 !important; font-size: 0.9rem;">
        <strong style="color: #CC4628;">Now:</strong> Recruiting mentors<br><br>
        <strong style="color: #CC4628;">Feb 2026:</strong> Mentor onboarding<br><br>
        <strong style="color: #CC4628;">Spring 2026:</strong> Program launch
        </p>
    </div>
    """, unsafe_allow_html=True)

# Get Involved
st.markdown("## Get Involved")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: #CFDCE9; padding: 2rem; border-radius: 12px; text-align: center;">
        <h3 style="margin-top: 0;">🧑‍🏫 Alumni: Become a Mentor</h3>
        <p>Share your AI/ML expertise with the next generation of Mines engineers and scientists.</p>
        <p style="margin-bottom: 0; font-size: 0.9rem; color: #75757D;">
        Time commitment: Flexible, typically 1-2 hours/month
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Volunteer as Mentor", use_container_width=True, key="mentor_btn"):
        st.info("Contact the MAAG leadership to express your interest in becoming a mentor.")

with col2:
    st.markdown("""
    <div style="background: #CFDCE9; padding: 2rem; border-radius: 12px; text-align: center;">
        <h3 style="margin-top: 0;">🎓 Students: Find a Mentor</h3>
        <p>Connect with alumni who can help guide your AI/ML career journey.</p>
        <p style="margin-bottom: 0; font-size: 0.9rem; color: #75757D;">
        Available to all Mines students interested in AI/ML
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Request a Mentor", use_container_width=True, key="student_btn"):
        st.info("Program launching Spring 2026. Stay tuned for sign-up details!")

# Impact Section
st.markdown("## Why Mentorship Matters")

impact_stats = [
    ("87%", "of mentees report increased confidence in career decisions"),
    ("3x", "more likely to receive a job offer with mentor guidance"),
    ("92%", "of mentors find the experience personally rewarding")
]

cols = st.columns(3)
for col, (stat, desc) in zip(cols, impact_stats):
    with col:
        st.markdown(f"""
        <div class="highlight-stat">
            <p style="font-size: 2rem; font-weight: 700; color: #CC4628 !important; margin: 0;">{stat}</p>
            <p style="font-size: 0.85rem; color: #75757D; margin: 0.5rem 0 0 0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #75757D; padding: 1rem;">
    <p><strong>Mines AI/ML Affinity Group (MAAG)</strong><br>
    Connecting alumni and students in the field of artificial intelligence and machine learning<br>
    <small>Part of the Colorado School of Mines Alumni Association</small></p>
</div>
""", unsafe_allow_html=True)
