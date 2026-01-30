import streamlit as st

st.set_page_config(
    page_title="SME Information | Mines ProEd",
    page_icon="⛏️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap');
    
    .stApp {
        background-color: #FFFFFF;
    }
    
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
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
    
    [data-testid="stSidebar"] {
        background-color: #21314d;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    .info-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #CFDCE9 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #CC4628;
        box-shadow: 0 4px 6px rgba(33, 49, 77, 0.1);
    }
    
    .compensation-card {
        background: #21314d;
        border-radius: 12px;
        padding: 2rem;
        color: #FFFFFF !important;
        margin: 1rem 0;
    }
    
    .compensation-card h3, .compensation-card p, .compensation-card li {
        color: #FFFFFF !important;
    }
    
    .highlight-box {
        background: #CFDCE9;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
        border: 2px solid #879EC3;
    }
    
    .area-tag {
        display: inline-block;
        background: #09396C;
        color: #FFFFFF !important;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-weight: 500;
    }
    
    .stButton > button {
        background-color: #CC4628;
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
    }
    
    .stButton > button:hover {
        background-color: #21314d;
    }
    
    a {
        color: #CC4628 !important;
        text-decoration: none;
        font-weight: 500;
    }
    
    .or-divider {
        text-align: center;
        margin: 1.5rem 0;
        font-size: 1.2rem;
        color: #879EC3;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://brand.mines.edu/wp-content/uploads/sites/425/2023/03/Mines-Logo-triangle-blue.png", width=80)
    st.markdown("### Mines ProEd")
    st.markdown("Professional Education from Colorado School of Mines")
    st.divider()
    st.markdown("#### Quick Links")
    st.markdown("🔗 [SME Application](https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV)")
    st.markdown("🔗 [ProEd Homepage](https://proed.mines.edu/)")

# Header
st.markdown("# 📚 Become a Subject Matter Expert (SME)")
st.markdown("""
A Subject Matter Expert provides content and materials to develop professional education short courses 
at Colorado School of Mines. Work with our Online Learning Experience Designer (OLED) team to create 
impactful learning experiences.
""")

# What SME Does
st.markdown("## What Does an SME Do?")

st.markdown("""
<div class="info-card">
    <p style="margin: 0; font-size: 1.05rem;">
    An SME provides content and materials (text, graphics, slides, video, etc.) to develop professional education short courses. 
    This can be for:
    </p>
    <ul style="margin-top: 1rem;">
        <li><strong>Online Self-Study</strong> — Asynchronous, self-paced learning</li>
        <li><strong>Online Facilitated</strong> — Instructor-led virtual courses</li>
        <li><strong>In-Person</strong> — Traditional classroom experience</li>
        <li><strong>Hybrid</strong> — Combination of online and in-person</li>
    </ul>
    <p style="margin-bottom: 0;">
    An Online Learning Experience Designer (OLED) will work with you to build the online course components. 
    You will review all course materials before they go final.
    </p>
</div>
""", unsafe_allow_html=True)

# Areas of Interest
st.markdown("## Course Development Areas")
st.markdown("We are actively seeking SMEs for course development in these areas:")

areas = [
    ("⚡", "Energy", "Future-looking (traditional sources, nuclear, geothermal)"),
    ("🤖", "AI Use in Industry", "Practical applications of artificial intelligence"),
    ("📊", "Executive Education", "Leadership in STEM fields"),
    ("⛏️", "Mining & Minerals", "Advanced extraction and processing"),
    ("🚀", "Aerospace", "Space and aviation technologies"),
    ("🏗️", "Construction Engineering", "Modern construction methods")
]

col1, col2 = st.columns(2)

for i, (icon, title, desc) in enumerate(areas):
    with col1 if i < 3 else col2:
        st.markdown(f"""
        <div class="highlight-box">
            <h4 style="margin: 0;">{icon} {title}</h4>
            <p style="margin: 0.5rem 0 0 0; color: #75757D; font-size: 0.95rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Time Commitment
st.markdown("## Time Commitment")

st.markdown("""
<div class="info-card">
    <h3 style="margin-top: 0;">⏱️ What to Expect</h3>
    <p>The time commitment varies depending on the course format and how organized your existing content is.</p>
    <p><strong>General guideline:</strong> Approximately <strong>4 hours of preparation</strong> for every <strong>1 hour of learning</strong> content.</p>
    <p style="margin-bottom: 0;">
    <em>Some SMEs with well-organized materials take less time, while new SMEs often find it takes more than expected. 
    We provide training (online self-study course) and support throughout the process.</em>
    </p>
</div>
""", unsafe_allow_html=True)

# Compensation Model
st.markdown("## Financial Model & Compensation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="compensation-card">
        <h3 style="margin-top: 0;">💻 Self-Paced (On-Demand) Courses</h3>
        <hr style="border-color: #879EC3; margin: 1rem 0;">
        <h4 style="color: #879EC3 !important; margin: 0;">Option A: Revenue Share</h4>
        <p style="font-size: 1.1rem;"><strong>$250</strong> per learning hour created</p>
        <p style="margin-bottom: 1rem;"><strong>+ 20%</strong> of net revenue share</p>
        <div class="or-divider" style="color: #879EC3;">— OR —</div>
        <h4 style="color: #879EC3 !important; margin: 0;">Option B: Flat Rate</h4>
        <p style="font-size: 1.1rem; margin-bottom: 0;"><strong>$750</strong> per learning hour created</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="compensation-card">
        <h3 style="margin-top: 0;">👨‍🏫 Online Facilitated Courses</h3>
        <hr style="border-color: #879EC3; margin: 1rem 0;">
        <p style="color: #879EC3 !important; font-style: italic;">Requires active instructor participation throughout the course each time it is taught.</p>
        <p style="font-size: 1.1rem;"><strong>$2,500</strong> per teaching day</p>
        <p style="font-size: 0.95rem;">e.g., a two-day course = $5,000</p>
        <p style="font-size: 1.1rem;"><strong>+ $1,250</strong> preparation fee per teaching day</p>
        <p style="font-size: 1.1rem; margin-bottom: 0;"><strong>+ 20%</strong> of net revenue share</p>
    </div>
    """, unsafe_allow_html=True)

# Example Calculation
with st.expander("📊 See Example Compensation Calculations"):
    st.markdown("### Self-Paced Course Example")
    st.markdown("**Scenario:** Creating a 10-hour self-paced course")
    
    calc_col1, calc_col2 = st.columns(2)
    with calc_col1:
        st.markdown("""
        **Option A (with revenue share):**
        - Upfront: 10 hours × $250 = **$2,500**
        - Plus: 20% of ongoing net revenue
        """)
    with calc_col2:
        st.markdown("""
        **Option B (flat rate):**
        - Total: 10 hours × $750 = **$7,500**
        - No additional revenue share
        """)
    
    st.markdown("---")
    st.markdown("### Facilitated Course Example")
    st.markdown("**Scenario:** Teaching a 3-day facilitated course")
    st.markdown("""
    - Teaching: 3 days × $2,500 = **$7,500**
    - Preparation: 3 days × $1,250 = **$3,750**
    - **Total upfront: $11,250** + 20% of net revenue
    """)

# CTA
st.markdown("---")
st.markdown("## Ready to Share Your Expertise?")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #CFDCE9; border-radius: 12px;">
        <h3 style="margin-top: 0;">Apply to Become an SME</h3>
        <p>Join Colorado School of Mines in shaping the future of professional education.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "📝 Submit SME Application →",
        "https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV",
        use_container_width=True
    )

# Contact Info
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #75757D; padding: 1rem;">
    <p>Questions about the SME program?<br>
    Contact: <strong>Sam Spiegel</strong>, Assistant VP of Online & ProEd at Mines</p>
</div>
""", unsafe_allow_html=True)
