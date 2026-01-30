"""
Mines Alumni Board (MAB) Initiatives Page
Updates on Life Long Learning & Development focusing on ProEd
"""
import streamlit as st
import pandas as pd
from utils import (
    apply_mines_styling,
    render_sidebar,
    create_info_card,
    create_blue_card,
    load_sme_recommendations,
    save_sme_recommendation,
    MINES_COLORS,
    SME_DOMAINS,
)

# Page configuration
st.set_page_config(
    page_title="MAB Initiatives | Mines ProEd",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply Mines branding
apply_mines_styling()
render_sidebar()

# Page Header
st.markdown(
    f"""
    <div style="margin-bottom: 2rem;">
        <h1 style="color: {MINES_COLORS['dark_blue']};">🎓 Mines Alumni Board Initiatives</h1>
        <p style="color: {MINES_COLORS['text_muted']}; font-size: 1.1rem;">
            Life Long Learning & Development Updates - Focusing on ProEd
        </p>
    </div>
    <div class="mines-divider"></div>
    """,
    unsafe_allow_html=True,
)

# Initiative Overview Cards
st.markdown("## Current Initiatives")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%);
                    padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">🔍</span>
                <h3 style="color: white !important; margin: 0;">SME Search</h3>
            </div>
            <p style="color: {MINES_COLORS['pale_blue']}; margin: 0;">
                MAB is creating a focused recruitment plan and making targeted alumni introductions 
                to identify potential Subject Matter Experts.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, {MINES_COLORS['colorado_red']} 0%, #E05A3C 100%);
                    padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">📢</span>
                <h3 style="color: white !important; margin: 0;">ProEd Promotion</h3>
            </div>
            <p style="color: rgba(255,255,255,0.9); margin: 0;">
                Expanding awareness through Career Fair, Homecoming, Mines Magazine, 
                and the alumni portal.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, {MINES_COLORS['earth_blue']} 0%, {MINES_COLORS['muted_blue']} 100%);
                    padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">🤖</span>
                <h3 style="color: white !important; margin: 0;">AI for ProEd</h3>
            </div>
            <p style="color: rgba(255,255,255,0.9); margin: 0;">
                Julian will work with Sam Spiegel and course SMEs to develop AI teaching assistants 
                and sponsor initial AI implementation costs.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, {MINES_COLORS['environment_green']} 0%, #6DAD3A 100%);
                    padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">💬</span>
                <h3 style="color: white !important; margin: 0;">Alumni Feedback</h3>
            </div>
            <p style="color: rgba(255,255,255,0.9); margin: 0;">
                Collecting input from alumni on what courses to create 
                to meet professional development needs.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Detailed Initiative Sections
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)

# Initiative 1: SME Search
st.markdown("## 🔍 Initiative 1: SME Search & Recruitment")

st.markdown(
    f"""
    <div class="blue-card">
        <p style="margin: 0; color: {MINES_COLORS['text_dark']}; line-height: 1.8;">
            The Mines Alumni Board is actively seeking alumni to serve as Subject Matter Experts (SMEs) 
            for ProEd courses. We're looking for experts in the following domains:
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Domain cards in a grid
domains_with_icons = [
    ("⚡", "Energy - Future Looking", "Traditional sources, nuclear, geothermal"),
    ("🤖", "AI Use in Industry", "Practical AI applications"),
    ("📊", "Executive Education", "STEM leadership"),
    ("⛏️", "Mining & Minerals", "Modern mining technologies"),
    ("🚀", "Aerospace", "Space and aviation"),
    ("🏗️", "Construction Engineering", "Construction methods"),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(domains_with_icons):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 1rem; 
                        border-radius: 8px; margin-bottom: 0.75rem; text-align: center;">
                <div style="font-size: 1.75rem;">{icon}</div>
                <div style="color: {MINES_COLORS['dark_blue']}; font-weight: 600; font-size: 0.9rem;">{title}</div>
                <div style="color: {MINES_COLORS['text_muted']}; font-size: 0.8rem;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# SME Recommendation Form
st.markdown("### Submit an SME Recommendation")
st.markdown("Know a Mines alumni who would be a great SME? Submit their information below!")

with st.form("sme_recommendation_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        alumni_name = st.text_input("Alumni Name *", placeholder="John Doe")
        linkedin_url = st.text_input("LinkedIn Profile URL *", placeholder="https://linkedin.com/in/username")
        domain = st.selectbox("Expertise Domain *", options=["Select a domain..."] + SME_DOMAINS)
        alumni_email = st.text_input("Alumni Email (if known)", placeholder="alumni@email.com")
    
    with col2:
        submitted_by = st.text_input("Your Name *", placeholder="Your full name")
        submitter_email = st.text_input("Your Email *", placeholder="your@email.com")
        notes = st.text_area("Additional Notes", placeholder="Any additional context about why this person would be a great SME...", height=133)
    
    submitted = st.form_submit_button("Submit Recommendation", use_container_width=True)
    
    if submitted:
        # Validation
        if not alumni_name or not linkedin_url or domain == "Select a domain..." or not submitted_by or not submitter_email:
            st.error("Please fill in all required fields marked with *")
        elif "linkedin.com" not in linkedin_url.lower():
            st.error("Please enter a valid LinkedIn URL")
        elif "@" not in submitter_email:
            st.error("Please enter a valid email address")
        else:
            # Save recommendation
            recommendation = {
                "alumni_name": alumni_name,
                "linkedin_url": linkedin_url,
                "domain": domain,
                "alumni_email": alumni_email,
                "notes": notes,
                "submitted_by": submitted_by,
                "submitter_email": submitter_email,
            }
            
            if save_sme_recommendation(recommendation):
                st.success(f"Thank you! Your recommendation for {alumni_name} has been submitted successfully.")
                st.balloons()
            else:
                st.error("There was an error saving your recommendation. Please try again.")

# Display existing recommendations
st.markdown("### SME Recommendations Received")

recommendations = load_sme_recommendations()

if recommendations:
    # Convert to DataFrame for display
    df = pd.DataFrame(recommendations)
    
    # Reorder and rename columns for display
    display_cols = {
        "alumni_name": "Alumni Name",
        "domain": "Domain",
        "linkedin_url": "LinkedIn",
        "submitted_by": "Recommended By",
        "timestamp": "Submitted",
    }
    
    df_display = df[[col for col in display_cols.keys() if col in df.columns]].copy()
    df_display.columns = [display_cols[col] for col in df_display.columns]
    
    # Format timestamp
    if "Submitted" in df_display.columns:
        df_display["Submitted"] = pd.to_datetime(df_display["Submitted"]).dt.strftime("%Y-%m-%d")
    
    # Make LinkedIn clickable
    if "LinkedIn" in df_display.columns:
        df_display["LinkedIn"] = df_display["LinkedIn"].apply(
            lambda x: f'<a href="{x}" target="_blank">View Profile</a>' if x else ""
        )
    
    # Display with custom styling
    st.markdown(
        f"""
        <div style="background-color: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            {df_display.to_html(escape=False, index=False, classes='dataframe')}
        </div>
        <style>
            .dataframe {{
                width: 100%;
                border-collapse: collapse;
            }}
            .dataframe th {{
                background-color: {MINES_COLORS['dark_blue']} !important;
                color: white !important;
                padding: 1rem !important;
                text-align: left !important;
                font-family: 'Montserrat', sans-serif !important;
            }}
            .dataframe td {{
                padding: 0.75rem 1rem !important;
                border-bottom: 1px solid {MINES_COLORS['pale_blue']} !important;
            }}
            .dataframe tr:hover {{
                background-color: {MINES_COLORS['pale_blue']} !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(f"<p style='color: {MINES_COLORS['text_muted']}; font-size: 0.9rem;'>Total recommendations: {len(recommendations)}</p>", unsafe_allow_html=True)
else:
    st.info("No SME recommendations have been submitted yet. Be the first to recommend someone!")

# Initiative 2: ProEd Promotion
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## 📢 Initiative 2: ProEd Promotion")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="info-card">
            <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">📅 Promotion Channels</h4>
            <ul style="color: {MINES_COLORS['text_dark']}; line-height: 2;">
                <li><strong>Career Fair</strong> - Direct outreach to professionals</li>
                <li><strong>Homecoming</strong> - Alumni engagement events</li>
                <li><strong>Mines Magazine</strong> - Feature articles and success stories</li>
                <li><strong>Alumni Portal</strong> - Digital presence and resources</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="blue-card">
            <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">🌟 Success Story Initiative</h4>
            <p style="color: {MINES_COLORS['text_dark']}; line-height: 1.8;">
                We're looking to feature <strong>ProEd student success stories</strong> in:
            </p>
            <ul style="color: {MINES_COLORS['text_dark']}; line-height: 1.8;">
                <li>Mines Magazine articles</li>
                <li>Email blast campaigns</li>
                <li>Social media highlights</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Initiative 3: AI for ProEd
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## 🤖 Initiative 3: AI for ProEd")

st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['earth_blue']} 100%);
                padding: 2rem; border-radius: 12px; color: white; margin-bottom: 1rem;">
        <h3 style="color: white !important; margin-bottom: 1rem;">AI-Powered Course Enhancement</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
            <div>
                <h5 style="color: {MINES_COLORS['golden_tech']} !important; margin-bottom: 0.5rem;">🎓 AI Teaching Assistants</h5>
                <p style="color: {MINES_COLORS['pale_blue']}; font-size: 0.9rem; margin: 0;">
                    Julian will collaborate with Sam Spiegel and course SMEs to develop 
                    AI teaching assistants that enhance the learning experience.
                </p>
            </div>
            <div>
                <h5 style="color: {MINES_COLORS['golden_tech']} !important; margin-bottom: 0.5rem;">💰 Sponsored Development</h5>
                <p style="color: {MINES_COLORS['pale_blue']}; font-size: 0.9rem; margin: 0;">
                    Julian will sponsor the initial overhead cost of using AI 
                    for course development and deployment.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Upcoming Events
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## 📅 Upcoming Events")

st.markdown(
    f"""
    <div style="background-color: {MINES_COLORS['golden_tech']}; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="background-color: white; padding: 1rem; border-radius: 8px; text-align: center; min-width: 80px;">
                <div style="color: {MINES_COLORS['colorado_red']}; font-weight: 700; font-size: 1.5rem;">FEB</div>
                <div style="color: {MINES_COLORS['dark_blue']}; font-weight: 600;">2026</div>
            </div>
            <div>
                <h4 style="color: {MINES_COLORS['dark_blue']} !important; margin: 0 0 0.25rem 0;">idigMines Events</h4>
                <p style="color: {MINES_COLORS['dark_blue']}; margin: 0;">
                    ProEd will be one of the highlighted causes during idigMines events in mid-February.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
