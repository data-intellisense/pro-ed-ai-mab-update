"""
ProEd AI Demo - Mines Professional Education Portal
Main entry point for the Streamlit application.
"""
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Mines ProEd Portal",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main container styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1a365d 0%, #2d5a87 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .main-header h1 {
        color: white !important;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        color: #e2e8f0;
        font-size: 1.2rem;
    }
    
    /* Card styling */
    .info-card {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #1a365d;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Metric styling */
    .metric-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stMetric {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 8px;
    }
    
    /* Link button styling */
    .link-button {
        display: inline-block;
        background-color: #c8a750;
        color: white !important;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 1rem;
    }
    
    .link-button:hover {
        background-color: #b8973f;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>⛏️ Mines Professional Education</h1>
    <p>Lifelong Learning & Development Portal</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
Welcome to the **Colorado School of Mines Professional Education (ProEd)** information portal. 
This application provides comprehensive information about ProEd programs, opportunities for 
Subject Matter Experts (SMEs), and updates from the Mines Alumni Board initiatives.
""")

# Quick Stats
st.subheader("📊 Quick Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Focus Areas",
        value="6",
        help="Energy, AI, Executive Ed, Mining, Aerospace, Construction"
    )

with col2:
    st.metric(
        label="SME Compensation",
        value="$250-750",
        delta="per learning hour",
        help="Self-paced course development"
    )

with col3:
    st.metric(
        label="Teaching Rate",
        value="$2,500",
        delta="per day",
        help="Online facilitated courses"
    )

with col4:
    st.metric(
        label="Revenue Share",
        value="20%",
        help="Net revenue share for SMEs"
    )

st.divider()

# Main content sections
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🎓 About ProEd")
    st.markdown("""
    <div class="info-card">
        <p>ProEd offers professional education short courses designed for working professionals. 
        Courses can be delivered in multiple formats:</p>
        <ul>
            <li><strong>Online Self-Study</strong> - Learn at your own pace</li>
            <li><strong>Online Facilitated</strong> - Instructor-led virtual courses</li>
            <li><strong>In-Person</strong> - Traditional classroom experience</li>
            <li><strong>Hybrid</strong> - Combination of online and in-person</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔬 Focus Areas")
    focus_areas = [
        "🔋 Energy (traditional, nuclear, geothermal)",
        "🤖 AI Use in Industry",
        "📈 Executive Education in STEM",
        "⛏️ Mining & Minerals",
        "🚀 Aerospace",
        "🏗️ Construction Engineering"
    ]
    
    for area in focus_areas:
        st.markdown(f"- {area}")

with col_right:
    st.subheader("👥 Become a Subject Matter Expert")
    st.markdown("""
    <div class="info-card">
        <p>As a <strong>Subject Matter Expert (SME)</strong>, you provide content and materials 
        to develop professional education courses. An Online Learning Experience Designer (OLED) 
        will work with you to build the course components.</p>
        <p><strong>Time Commitment:</strong> Approximately 4 hours of preparation for every 
        hour of learning content.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Ready to Apply?")
    st.link_button(
        "📝 SME Application Form",
        "https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV",
        type="primary"
    )

st.divider()

# Navigation cards
st.subheader("📚 Explore More")

nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    with st.container(border=True):
        st.markdown("### 💰 Financial Models")
        st.markdown("Learn about SME compensation structures for self-paced and facilitated courses.")
        st.page_link("pages/1_ProEd_Program.py", label="View Details →", icon="📄")

with nav_col2:
    with st.container(border=True):
        st.markdown("### 🎯 MAB Initiatives")
        st.markdown("Mines Alumni Board initiatives for Lifelong Learning & Development.")
        st.page_link("pages/2_MAB_Initiatives.py", label="View Details →", icon="🎓")

with nav_col3:
    with st.container(border=True):
        st.markdown("### 🤖 MAAG Updates")
        st.markdown("Mines AI/ML Affinity Group updates and mentoring programs.")
        st.page_link("pages/3_MAAG_Updates.py", label="View Details →", icon="🧠")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 1rem;">
    <p>For questions, contact <strong>Sam Spiegel</strong>, Assistant VP of Online & ProEd at Mines</p>
    <p>© Colorado School of Mines Professional Education</p>
</div>
""", unsafe_allow_html=True)
