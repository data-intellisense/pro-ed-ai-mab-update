import streamlit as st
import os
import base64

st.set_page_config(
    page_title="SME Information | Mines ProEd",
    page_icon="⛏️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap');
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');
    
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
    
    
    .info-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #CFDCE9 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border-left: 5px solid #CC4628;
        box-shadow: 0 4px 6px rgba(33, 49, 77, 0.1);
    }
    
    .info-card h3, .info-card h4 {
        color: #21314d !important;
        margin-top: 0 !important;
    }
    
    .info-card p, .info-card li {
        color: #21314d !important;
    }
    
    .compensation-card {
        background: #CFDCE9;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin: 0.5rem 0;
        height: 340px;
        display: flex;
        flex-direction: column;
        border-left: 5px solid #CC4628;
    }
    
    .compensation-card h3 {
        color: #21314d !important;
        margin-top: 0 !important;
        margin-bottom: 0.25rem !important;
        font-size: 1.1rem !important;
    }
    
    .compensation-card h4 {
        color: #09396C !important;
        margin-top: 0.5rem !important;
        margin-bottom: 0.25rem !important;
        font-size: 0.95rem !important;
    }
    
    .compensation-card p {
        color: #21314d !important;
        margin: 0.2rem 0 !important;
        line-height: 1.4 !important;
        font-size: 0.9rem !important;
    }
    
    .compensation-card strong {
        color: #21314d !important;
    }
    
    .compensation-card li {
        color: #21314d !important;
    }
    
    .compensation-card hr {
        border-color: #879EC3 !important;
        margin: 0.5rem 0 !important;
    }
    
    .compensation-card .subtitle {
        color: #4a5568 !important;
        font-style: italic;
        font-size: 0.85rem !important;
    }
    
    .compensation-card .or-text {
        color: #09396C !important;
        text-align: center;
        margin: 0.5rem 0 !important;
        font-weight: 600;
    }
    
    .highlight-box {
        background: #CFDCE9;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        border-left: 5px solid #CC4628;
        height: 120px;
    }
    
    .highlight-box h4 {
        color: #21314d !important;
        margin: 0 !important;
    }
    
    .highlight-box p {
        color: #21314d !important;
        margin: 0.5rem 0 0 0 !important;
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
    
    .cta-box {
        text-align: center;
        padding: 2rem;
        background: #CFDCE9;
        border-radius: 12px;
    }
    
    .cta-box h3 {
        color: #21314d !important;
        margin-top: 0 !important;
    }
    
    .cta-box p {
        color: #4a5568 !important;
        margin-bottom: 0;
    }
</style>
""", unsafe_allow_html=True)

# Top Right Logo
def load_logo_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "Mines-Logo-triangle-blue.webp")
logo_b64 = load_logo_base64(logo_path)

st.markdown(f"""
    <div style="display: flex; justify-content: flex-end; align-items: center; padding: 0.5rem 0; margin-bottom: 0.5rem;">
        <img src="data:image/webp;base64,{logo_b64}"
             alt="Colorado School of Mines"
             style="max-height: 60px; width: auto; object-fit: contain;">
    </div>
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
            <h4>{icon} {title}</h4>
            <p>{desc}</p>
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
        <h3>💻 Self-Paced (On-Demand) Courses</h3>
        <hr>
        <h4>Option A: Revenue Share</h4>
        <p><strong>$250</strong> per learning hour created</p>
        <p><strong>+ 20%</strong> of net revenue share</p>
        <p class="or-text">— OR —</p>
        <h4>Option B: Flat Rate</h4>
        <p><strong>$750</strong> per learning hour created</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="compensation-card">
        <h3>👨‍🏫 Online Facilitated Courses</h3>
        <hr>
        <p class="subtitle">Requires active instructor participation throughout the course each time it is taught.</p>
        <p><strong>$2,500</strong> per teaching day</p>
        <p class="subtitle">e.g., a two-day course = $5,000</p>
        <p><strong>+ $1,250</strong> preparation fee per teaching day</p>
        <p><strong>+ 20%</strong> of net revenue share</p>
    </div>
    """, unsafe_allow_html=True)

# Example Calculations
st.markdown("### Example Compensation Calculations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="compensation-card">
        <h3>Self-Paced Course Example</h3>
        <hr>
        <p><strong>Scenario:</strong> Creating a 10-hour self-paced course</p>
        <h4>Option A (with revenue share):</h4>
        <p>• Upfront: 10 hours × $250 = <strong>$2,500</strong></p>
        <p>• Plus: 20% of ongoing net revenue</p>
        <h4>Option B (flat rate):</h4>
        <p>• Total: 10 hours × $750 = <strong>$7,500</strong></p>
        <p>• No additional revenue share</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="compensation-card">
        <h3>Facilitated Course Example</h3>
        <hr>
        <p><strong>Scenario:</strong> Teaching a 3-day facilitated course</p>
        <p>• Teaching: 3 days × $2,500 = <strong>$7,500</strong></p>
        <p>• Preparation: 3 days × $1,250 = <strong>$3,750</strong></p>
        <p class="or-text" style="margin-top: 1rem;"><strong>Total upfront: $11,250</strong></p>
        <p>+ 20% of net revenue</p>
    </div>
    """, unsafe_allow_html=True)

# CTA
st.markdown("---")
st.markdown("## Ready to Share Your Expertise?")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="cta-box">
        <h3>Apply to Become an SME</h3>
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
