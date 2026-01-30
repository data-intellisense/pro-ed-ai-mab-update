"""
Mines ProEd Information Portal - Home Page
A Streamlit app showcasing Colorado School of Mines Professional Education program
"""
import streamlit as st
from utils import (
    apply_mines_styling,
    render_header,
    render_sidebar,
    create_metric_card,
    create_info_card,
    MINES_COLORS,
)

# Page configuration
st.set_page_config(
    page_title="Mines ProEd Portal",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply Mines branding
apply_mines_styling()

# Render sidebar
render_sidebar()

# Main content
render_header()

# Hero Section
st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%); 
                padding: 2rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
        <h2 style="color: white !important; margin-bottom: 1rem;">Welcome to Mines ProEd</h2>
        <p style="font-size: 1.1rem; line-height: 1.6; color: {MINES_COLORS['pale_blue']};">
            Mines ProEd delivers flexible, professional education options from Colorado School of Mines. 
            Our courses translate cutting-edge technical expertise into real-world business impact.
        </p>
        <div style="margin-top: 1.5rem;">
            <a href="https://proed.mines.edu/" target="_blank" 
               style="background-color: {MINES_COLORS['colorado_red']}; color: white !important; 
                      padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none;
                      font-weight: 600; margin-right: 1rem;">
                Explore Courses →
            </a>
            <a href="https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV" 
               target="_blank" 
               style="background-color: transparent; color: white !important; 
                      padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none;
                      font-weight: 600; border: 2px solid white;">
                Become an SME
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Value Propositions
st.markdown("## Why Mines ProEd?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 1.5rem; 
                    border-radius: 12px; height: 200px;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎓</div>
            <h4 style="color: {MINES_COLORS['dark_blue']}; margin-bottom: 0.5rem;">Expert Faculty</h4>
            <p style="color: {MINES_COLORS['text_dark']};">
                Learn directly from Mines' world-class faculty and industry experts shaping today's technologies.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 1.5rem; 
                    border-radius: 12px; height: 200px;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
            <h4 style="color: {MINES_COLORS['dark_blue']}; margin-bottom: 0.5rem;">Flexible Learning</h4>
            <p style="color: {MINES_COLORS['text_dark']};">
                Access self-paced online, facilitated, hybrid, and in-person options that fit your schedule.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 1.5rem; 
                    border-radius: 12px; height: 200px;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🚀</div>
            <h4 style="color: {MINES_COLORS['dark_blue']}; margin-bottom: 0.5rem;">Career Impact</h4>
            <p style="color: {MINES_COLORS['text_dark']};">
                Step into new responsibility, accelerate advancement, or pivot careers with new technical expertise.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# What You'll Gain Section
st.markdown("## What You'll Gain")

gains = [
    ("🔬", "Technical Fluency", "Gain fluency in the science and economics driving energy and resource industries"),
    ("🏆", "Professional Credibility", "Build credibility with engineers, investors, and clients"),
    ("💡", "Innovation Insights", "Discover opportunities for innovation, sustainability, and growth"),
    ("📈", "Career Advancement", "Step into new responsibility or accelerate your advancement"),
]

col1, col2 = st.columns(2)

for i, (icon, title, desc) in enumerate(gains):
    with col1 if i % 2 == 0 else col2:
        st.markdown(
            create_info_card(title, desc, icon),
            unsafe_allow_html=True,
        )

# Course Focus Areas
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## Course Development Areas")
st.markdown(
    "We are actively seeking Subject Matter Experts (SMEs) to help develop courses in these key areas:"
)

areas = [
    ("⚡", "Energy", "Future-looking: traditional sources, nuclear, geothermal"),
    ("🤖", "AI in Industry", "Practical AI applications across industries"),
    ("📊", "Executive Education", "STEM leadership and management"),
    ("⛏️", "Mining & Minerals", "Modern mining technologies and practices"),
    ("🚀", "Aerospace", "Space and aviation technologies"),
    ("🏗️", "Construction Engineering", "Modern construction methods and management"),
]

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, (icon, title, desc) in enumerate(areas):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%);
                        padding: 1.25rem; border-radius: 10px; margin-bottom: 1rem; min-height: 120px;">
                <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">{icon}</div>
                <h5 style="color: white !important; margin: 0 0 0.25rem 0;">{title}</h5>
                <p style="color: {MINES_COLORS['pale_blue']}; font-size: 0.85rem; margin: 0;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Quick Stats Section
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## At a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(create_metric_card("6", "Focus Areas"), unsafe_allow_html=True)

with col2:
    st.markdown(create_metric_card("3", "Course Formats"), unsafe_allow_html=True)

with col3:
    st.markdown(create_metric_card("10%", "Alumni Discount"), unsafe_allow_html=True)

with col4:
    st.markdown(create_metric_card("20%", "SME Revenue Share"), unsafe_allow_html=True)

# Call to Action
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 2rem; 
                border-radius: 12px; text-align: center; margin-top: 1rem;">
        <h3 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 1rem;">
            Ready to Advance Your Career?
        </h3>
        <p style="color: {MINES_COLORS['text_dark']}; margin-bottom: 1.5rem;">
            Your career doesn't stand still. Neither should your skills. 
            It's time to turn "What if?" into "What's next!"
        </p>
        <a href="https://proed.mines.edu/pages/catalog-featured-courses" target="_blank" 
           style="background-color: {MINES_COLORS['colorado_red']}; color: white !important; 
                  padding: 0.75rem 2rem; border-radius: 6px; text-decoration: none;
                  font-weight: 600; font-size: 1.1rem;">
            Browse Course Catalog →
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="text-align: center; color: {MINES_COLORS['text_muted']}; padding: 1rem; 
                border-top: 1px solid {MINES_COLORS['light_gray']};">
        <p style="margin: 0;">© Colorado School of Mines | <a href="https://brand.mines.edu/" target="_blank">Brand Guidelines</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
