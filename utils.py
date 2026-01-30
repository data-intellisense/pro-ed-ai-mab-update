"""
Utility functions and Mines branding styles for ProEd Information App
"""
import streamlit as st
import json
import os
from datetime import datetime

# Mines Brand Colors - Optimized for contrast and readability
MINES_COLORS = {
    "dark_blue": "#21314d",
    "blaster_blue": "#09396C",
    "light_blue": "#879EC3",
    "colorado_red": "#CC4628",
    "pale_blue": "#E8EEF4",  # Lighter for better text contrast
    "white": "#FFFFFF",
    "light_gray": "#AEB3B8",
    "silver": "#81848A",
    "dark_gray": "#4a4a4a",  # Darker for better readability
    "text_dark": "#1a1a1a",  # High contrast text color
    "text_muted": "#374151",  # Muted but still readable
    "earth_blue": "#0272DE",
    "muted_blue": "#57A2BD",
    "golden_tech": "#F1B91A",
    "environment_green": "#80C342",
}

# SME Domains
SME_DOMAINS = [
    "Energy - Traditional Sources",
    "Energy - Nuclear",
    "Energy - Geothermal",
    "AI Use in Industry",
    "Executive Education in STEM Fields",
    "Mining & Minerals",
    "Aerospace",
    "Construction Engineering",
]

# File path for SME recommendations
SME_FILE = os.path.join(os.path.dirname(__file__), "data", "sme_recommendations.json")


def apply_mines_styling():
    """Apply Mines branding CSS to the Streamlit app"""
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@300;400;500;600&display=swap');
        
        /* Main app styling */
        .stApp {{
            font-family: 'Open Sans', sans-serif;
        }}
        
        /* Headers */
        h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
            font-family: 'Montserrat', sans-serif !important;
            color: {MINES_COLORS['dark_blue']} !important;
        }}
        
        /* Main title styling */
        .main-title {{
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            font-weight: 700;
            color: {MINES_COLORS['dark_blue']};
            margin-bottom: 0.5rem;
        }}
        
        .subtitle {{
            font-family: 'Open Sans', sans-serif;
            font-size: 1.1rem;
            color: {MINES_COLORS['text_muted']};
            margin-bottom: 2rem;
        }}
        
        /* Card styling */
        .info-card {{
            background-color: {MINES_COLORS['white']};
            border-left: 4px solid {MINES_COLORS['colorado_red']};
            padding: 1.5rem;
            border-radius: 0 8px 8px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }}
        
        .blue-card {{
            background-color: {MINES_COLORS['pale_blue']};
            border-left: 4px solid {MINES_COLORS['blaster_blue']};
            padding: 1.5rem;
            border-radius: 0 8px 8px 0;
            margin-bottom: 1rem;
        }}
        
        /* Metric cards */
        .metric-card {{
            background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
        }}
        
        .metric-value {{
            font-family: 'Montserrat', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            color: white;
        }}
        
        .metric-label {{
            font-family: 'Open Sans', sans-serif;
            font-size: 0.9rem;
            color: {MINES_COLORS['pale_blue']};
            margin-top: 0.5rem;
        }}
        
        /* Button styling */
        .stButton > button {{
            background-color: {MINES_COLORS['colorado_red']} !important;
            color: white !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.5rem 2rem !important;
            transition: all 0.3s ease !important;
        }}
        
        .stButton > button:hover {{
            background-color: {MINES_COLORS['dark_blue']} !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        
        /* Link styling */
        a {{
            color: {MINES_COLORS['blaster_blue']} !important;
            text-decoration: none;
            font-weight: 500;
        }}
        
        a:hover {{
            color: {MINES_COLORS['colorado_red']} !important;
            text-decoration: underline;
        }}
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background-color: {MINES_COLORS['dark_blue']};
        }}
        
        [data-testid="stSidebar"] .stMarkdown {{
            color: white;
        }}
        
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3 {{
            color: white !important;
        }}
        
        /* Expander styling */
        .streamlit-expanderHeader {{
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600 !important;
            color: {MINES_COLORS['dark_blue']} !important;
            background-color: {MINES_COLORS['pale_blue']} !important;
        }}
        
        /* Table styling */
        .dataframe {{
            font-family: 'Open Sans', sans-serif !important;
        }}
        
        .dataframe th {{
            background-color: {MINES_COLORS['dark_blue']} !important;
            color: white !important;
            font-family: 'Montserrat', sans-serif !important;
        }}
        
        .dataframe td {{
            color: {MINES_COLORS['text_dark']} !important;
        }}
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
            color: {MINES_COLORS['dark_blue']};
            background-color: {MINES_COLORS['pale_blue']};
            border-radius: 6px 6px 0 0;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: {MINES_COLORS['dark_blue']} !important;
            color: white !important;
        }}
        
        /* Success/Info/Warning messages */
        .stSuccess {{
            background-color: {MINES_COLORS['environment_green']}20 !important;
            border-left: 4px solid {MINES_COLORS['environment_green']} !important;
        }}
        
        .stInfo {{
            background-color: {MINES_COLORS['earth_blue']}20 !important;
            border-left: 4px solid {MINES_COLORS['earth_blue']} !important;
        }}
        
        /* Divider */
        .mines-divider {{
            height: 3px;
            background: linear-gradient(90deg, {MINES_COLORS['colorado_red']} 0%, {MINES_COLORS['dark_blue']} 50%, {MINES_COLORS['light_blue']} 100%);
            margin: 2rem 0;
            border-radius: 2px;
        }}
        
        /* Quick link cards */
        .quick-link {{
            background-color: {MINES_COLORS['pale_blue']};
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
        }}
        
        .quick-link:hover {{
            background-color: {MINES_COLORS['dark_blue']};
            color: white;
        }}
        
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        /* Form styling */
        .stTextInput > div > div > input {{
            border: 2px solid {MINES_COLORS['light_blue']} !important;
            border-radius: 6px !important;
        }}
        
        .stTextInput > div > div > input:focus {{
            border-color: {MINES_COLORS['colorado_red']} !important;
            box-shadow: 0 0 0 2px {MINES_COLORS['colorado_red']}20 !important;
        }}
        
        .stSelectbox > div > div {{
            border: 2px solid {MINES_COLORS['light_blue']} !important;
            border-radius: 6px !important;
        }}
        
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    """Render the Mines branded header with logo"""
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
            <img src="https://www.mines.edu/wp-content/uploads/assets/icon_4c_r_274-1.png" 
                 alt="Mines Logo" style="height: 80px;">
            <div>
                <div class="main-title">Mines ProEd</div>
                <div class="subtitle">Professional Education at Colorado School of Mines</div>
            </div>
        </div>
        <div class="mines-divider"></div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():
    """Render the sidebar with navigation and key links"""
    with st.sidebar:
        st.image(
            "https://www.mines.edu/wp-content/uploads/assets/icon_4c_r_274-1.png",
            width=150,
        )
        st.markdown("---")
        st.markdown("### Quick Links")
        st.markdown(
            f"""
            <a href="https://proed.mines.edu/" target="_blank" style="color: white !important;">
                🏠 ProEd Homepage
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <a href="https://proed.mines.edu/pages/catalog-featured-courses" target="_blank" style="color: white !important;">
                📚 Course Catalog
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <a href="https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV" target="_blank" style="color: white !important;">
                📝 SME Application
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("---")
        st.markdown("### Alumni Discount")
        st.code("ALUMNI10", language=None)
        st.markdown(
            f"""
            <a href="https://mailchi.mp/mines/gtowt1f82q" target="_blank" style="color: {MINES_COLORS['golden_tech']} !important;">
                🎫 Get Discount Form
            </a>
            """,
            unsafe_allow_html=True,
        )


def load_sme_recommendations():
    """Load SME recommendations from JSON file"""
    if os.path.exists(SME_FILE):
        with open(SME_FILE, "r") as f:
            return json.load(f)
    return []


def save_sme_recommendation(recommendation: dict):
    """Save a new SME recommendation to JSON file"""
    recommendations = load_sme_recommendations()
    recommendation["timestamp"] = datetime.now().isoformat()
    recommendations.append(recommendation)
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(SME_FILE), exist_ok=True)
    
    with open(SME_FILE, "w") as f:
        json.dump(recommendations, f, indent=2)
    
    return True


def create_metric_card(value: str, label: str):
    """Create a styled metric card"""
    return f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
    """


def create_info_card(title: str, content: str, icon: str = "📋"):
    """Create a styled info card"""
    return f"""
        <div class="info-card">
            <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">{icon} {title}</h4>
            <p style="margin-bottom: 0; color: {MINES_COLORS['text_dark']};">{content}</p>
        </div>
    """


def create_blue_card(title: str, content: str, icon: str = "💡"):
    """Create a styled blue card"""
    return f"""
        <div class="blue-card">
            <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">{icon} {title}</h4>
            <p style="margin-bottom: 0; color: {MINES_COLORS['text_dark']};">{content}</p>
        </div>
    """
