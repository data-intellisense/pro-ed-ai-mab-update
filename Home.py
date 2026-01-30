import streamlit as st
import os
import base64

# Page configuration
st.set_page_config(
    page_title="Mines ProEd | Professional Education",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Mines branding - Light theme with high contrast
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap');
    
    /* Main colors */
    :root {
        --dark-blue: #21314d;
        --blaster-blue: #09396C;
        --light-blue: #879EC3;
        --colorado-red: #CC4628;
        --pale-blue: #CFDCE9;
        --white: #FFFFFF;
        --dark-gray: #75757D;
        --light-gray: #AEB3B8;
    }
    
    /* Force light theme */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif !important;
        color: #21314d !important;
    }
    
    h1 {
        font-weight: 700 !important;
        font-size: 2.5rem !important;
    }
    
    h2 {
        font-weight: 600 !important;
        border-bottom: 3px solid #CC4628;
        padding-bottom: 0.5rem;
        margin-top: 2rem !important;
    }
    
    h3 {
        font-weight: 600 !important;
        color: #09396C !important;
    }
    
    /* Body text */
    p, li, span, div {
        font-family: 'Open Sans', sans-serif !important;
        color: #21314d;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #21314d;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown p {
        color: #FFFFFF !important;
    }
    
    /* Hide sidebar collapse/expand button text */
    [data-testid="stSidebarCollapseButton"] button,
    [data-testid="collapsedControl"] button {
        font-size: 0 !important;
        color: transparent !important;
    }
    
    [data-testid="stSidebarCollapseButton"] button span,
    [data-testid="collapsedControl"] button span {
        font-size: 0 !important;
        visibility: hidden !important;
    }
    
    /* Cards/Info boxes - Equal heights with explicit text colors */
    .info-card {
        background: #CFDCE9;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border-left: 5px solid #CC4628;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    .info-card h3 {
        color: #21314d !important;
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .info-card p {
        color: #21314d !important;
        margin-bottom: 0;
        flex-grow: 1;
    }
    
    .stat-card {
        background: #CFDCE9;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-left: 5px solid #CC4628;
    }
    
    .stat-card h3 {
        color: #21314d !important;
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .stat-card p {
        color: #4a5568 !important;
        margin-bottom: 0;
    }
    
    .highlight-card {
        background: #CFDCE9;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin: 0.5rem 0;
        border-left: 5px solid #CC4628;
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    .highlight-card h3 {
        color: #21314d !important;
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
        font-size: 1rem !important;
    }
    
    .highlight-card p {
        color: #21314d !important;
        margin-bottom: 0;
        font-size: 0.85rem !important;
        line-height: 1.4 !important;
    }
    
    /* Links */
    a {
        color: #CC4628 !important;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #CC4628;
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #21314d;
        color: #FFFFFF;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #21314d !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #75757D !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #CFDCE9;
        border-radius: 8px;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600;
        color: #21314d !important;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #21314d 0%, #09396C 100%);
        padding: 3rem;
        border-radius: 16px;
        margin-bottom: 2rem;
    }
    
    .hero-section h1, .hero-section h2, .hero-section h3, .hero-section h4,
    .hero-section p, .hero-section span, .hero-section li, .hero-section strong,
    .hero-section a, .hero-section div {
        color: #FFFFFF !important;
    }
    
    /* Feature list */
    .feature-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 1rem 0;
        border-bottom: 1px solid #CFDCE9;
    }
    
    .feature-icon {
        background: #CC4628;
        color: #FFFFFF;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(to right, #CC4628, #CFDCE9);
        margin: 2rem 0;
    }
    
    /* Quote styling */
    .quote-box {
        background: #FFFFFF;
        border-left: 4px solid #CC4628;
        padding: 1.5rem;
        margin: 1.5rem 0;
        font-style: italic;
        color: #21314d;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Home Page Header - Centered Horizontal Logo
def load_logo_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

horiz_logo_path = os.path.join(os.path.dirname(__file__), "resources", "Horizontal", "Mines-horiz.png")
horiz_logo_b64 = load_logo_base64(horiz_logo_path)

st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; padding: 1.5rem 0; margin-bottom: 1rem; border-bottom: 3px solid #CC4628;">
        <img src="data:image/png;base64,{horiz_logo_b64}"
             alt="Colorado School of Mines"
             style="max-height: 120px; width: auto; object-fit: contain;">
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://brand.mines.edu/wp-content/uploads/sites/425/2023/03/Mines-Logo-triangle-blue.png", width=80)
    st.markdown("### Mines ProEd")
    st.markdown("Professional Education from Colorado School of Mines")
    st.divider()
    st.markdown("#### Quick Links")
    st.markdown("🔗 [ProEd Catalog](https://proed.mines.edu/pages/catalog-featured-courses)")
    st.markdown("🔗 [ProEd Homepage](https://proed.mines.edu/)")
    st.markdown("🔗 [Alumni Discount Form](https://mailchi.mp/mines/gtowt1f82q)")
    st.divider()
    st.markdown("**Alumni Discount Code:**")
    st.code("ALUMNI10", language=None)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 style="margin-bottom: 1rem;">Mines ProEd</h1>
    <p style="font-size: 1.3rem; margin-bottom: 0;">Flexible, professional education options from Colorado School of Mines.<br>
    Translating cutting-edge technical expertise into real-world business impact.</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
Of the many things that differentiate Colorado School of Mines from other universities is our long history 
of preparing **industry-ready graduates** that go on to successful careers and industry leadership roles. 
That hasn't happened by accident. It reflects the strong partnerships that we have with industry and our 
commitment to aligning our education with industry needs.
""")

# Key Benefits
st.markdown("## Why Choose Mines ProEd?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Gain Technical Fluency</h3>
        <p>Develop deep understanding of the science and economics driving energy and resource industries.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>👨‍🏫 Learn from Experts</h3>
        <p>Access Mines' world-class faculty and industry experts shaping today's technologies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>💼 Build Credibility</h3>
        <p>Strengthen your standing with engineers, investors, and clients through recognized credentials.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🌱 Drive Innovation</h3>
        <p>Discover opportunities for innovation, sustainability, and growth in your field.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>🚀 Accelerate Your Career</h3>
        <p>Step into new responsibilities, accelerate advancement, or pivot with new technical expertise.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h3>⏰ Flexible Learning</h3>
        <p>From self-paced online modules to in-person sessions—learn in the way that works best for you.</p>
    </div>
    """, unsafe_allow_html=True)

# Quote
st.markdown("""
<div class="quote-box">
    <p style="font-size: 1.1rem; margin: 0;">"Your career doesn't stand still. Neither should your skills. Technology, innovation, and global challenges 
    are reshaping industries. To thrive, professionals need to keep learning, growing, and adapting."</p>
</div>
""", unsafe_allow_html=True)

# Course Categories
st.markdown("## Course Focus Areas")

focus_areas = [
    ("⚡", "Energy", "Future-looking perspectives on traditional sources, nuclear, and geothermal"),
    ("🤖", "AI in Industry", "Practical applications of artificial intelligence in professional settings"),
    ("📊", "Executive Education", "Leadership and management in STEM fields"),
    ("⛏️", "Mining & Minerals", "Advanced techniques and sustainable practices"),
    ("🚀", "Aerospace", "Cutting-edge aerospace engineering and technology"),
    ("🏗️", "Construction Engineering", "Modern construction methods and project management")
]

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, (icon, title, desc) in enumerate(focus_areas):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="highlight-card">
            <h3>{icon} {title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Call to Action
st.markdown("---")
st.markdown("## Ready to Get Started?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h3>📚 Browse Courses</h3>
        <p>Explore our catalog of professional education offerings</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Catalog →", "https://proed.mines.edu/pages/catalog-featured-courses", use_container_width=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h3>🎓 Become an SME</h3>
        <p>Share your expertise by becoming a Subject Matter Expert</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Apply Now →", "https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV", use_container_width=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h3>💰 Alumni Discount</h3>
        <p>Mines alumni receive special pricing on all courses</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Get Discount →", "https://mailchi.mp/mines/gtowt1f82q", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #75757D; padding: 1rem;">
    <p>Colorado School of Mines | Professional Education<br>
    <small>It's time to redirect your career. Let's turn "What if?" into "What's next!"</small></p>
</div>
""", unsafe_allow_html=True)
