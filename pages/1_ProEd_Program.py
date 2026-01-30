"""
Mines ProEd Program Details Page
SME Information, Financial Model, and Application Process
"""
import streamlit as st
from utils import (
    apply_mines_styling,
    render_sidebar,
    create_info_card,
    create_blue_card,
    MINES_COLORS,
    SME_DOMAINS,
)

# Page configuration
st.set_page_config(
    page_title="ProEd Program | Mines ProEd",
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
        <h1 style="color: {MINES_COLORS['dark_blue']};">📚 ProEd Program Details</h1>
        <p style="color: {MINES_COLORS['text_muted']}; font-size: 1.1rem;">
            Everything you need to know about becoming a Subject Matter Expert and our compensation model
        </p>
    </div>
    <div class="mines-divider"></div>
    """,
    unsafe_allow_html=True,
)

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["📋 SME Information", "💰 Financial Model", "📝 Apply Now"])

# ====================
# TAB 1: SME Information
# ====================
with tab1:
    st.markdown("## What is a Subject Matter Expert (SME)?")
    
    st.markdown(
        f"""
        <div class="blue-card">
            <p style="margin: 0; line-height: 1.8; color: {MINES_COLORS['text_dark']};">
                A <strong>Subject Matter Expert (SME)</strong> provides content and materials (text, graphics, slides, video, etc.) 
                to develop professional education short courses. This can be for online self-study, online facilitated, 
                in-person, or hybrid courses.
            </p>
            <p style="margin: 1rem 0 0 0; line-height: 1.8; color: {MINES_COLORS['text_dark']};">
                An <strong>Online Learning Experience Designer (OLED)</strong> will work with you to build the online course 
                components. The SME will review all course materials before it goes final.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("### Areas We're Seeking Course Development")
    
    col1, col2 = st.columns(2)
    
    domains_icons = {
        "Energy - Traditional Sources": "⛽",
        "Energy - Nuclear": "☢️",
        "Energy - Geothermal": "🌋",
        "AI Use in Industry": "🤖",
        "Executive Education in STEM Fields": "📊",
        "Mining & Minerals": "⛏️",
        "Aerospace": "🚀",
        "Construction Engineering": "🏗️",
    }
    
    for i, domain in enumerate(SME_DOMAINS):
        with col1 if i < len(SME_DOMAINS) // 2 else col2:
            icon = domains_icons.get(domain, "📋")
            st.markdown(
                f"""
                <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 0.75rem 1rem; 
                            border-radius: 8px; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.75rem;">
                    <span style="font-size: 1.5rem;">{icon}</span>
                    <span style="color: {MINES_COLORS['dark_blue']}; font-weight: 500;">{domain}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
    
    st.markdown("### Time Commitment")
    
    st.markdown(
        create_info_card(
            "Planning Your Commitment",
            """The time commitment varies depending on the course format and how organized your content and materials are. 
            <br><br><strong>General guideline:</strong> Approximately <span style="color: #CC4628; font-weight: 600;">4 hours of preparation 
            for every 1 hour of learning</span>.
            <br><br>Some SMEs take longer, while others who have well-organized content need less time. 
            New SMEs often find it takes more time than expected. We provide training (online self-study course) 
            and support throughout the process.""",
            "⏱️"
        ),
        unsafe_allow_html=True,
    )

# ====================
# TAB 2: Financial Model
# ====================
with tab2:
    st.markdown("## Financial Model for Mines ProEd")
    
    # Self-Paced Courses
    st.markdown("### 📹 Self-Paced (On-Demand) Courses")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%);
                        padding: 1.5rem; border-radius: 12px; color: white; height: 280px;">
                <h4 style="color: {MINES_COLORS['golden_tech']} !important; margin-bottom: 1rem;">Option A: Revenue Share</h4>
                <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">$250</div>
                <p style="color: {MINES_COLORS['pale_blue']}; margin-bottom: 1rem;">per learning hour created</p>
                <div style="background-color: rgba(255,255,255,0.1); padding: 0.75rem; border-radius: 8px;">
                    <span style="color: {MINES_COLORS['golden_tech']}; font-weight: 600;">PLUS:</span>
                    <span style="font-size: 1.25rem; font-weight: 600;"> 20%</span>
                    <span style="color: {MINES_COLORS['pale_blue']};"> of net revenue</span>
                </div>
                <p style="color: {MINES_COLORS['light_blue']}; font-size: 0.85rem; margin-top: 1rem;">
                    Great for courses with high enrollment potential
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="background-color: {MINES_COLORS['pale_blue']}; border: 3px solid {MINES_COLORS['dark_blue']};
                        padding: 1.5rem; border-radius: 12px; height: 280px;">
                <h4 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 1rem;">Option B: Flat Rate</h4>
                <div style="font-size: 2rem; font-weight: 700; color: {MINES_COLORS['dark_blue']}; margin-bottom: 0.5rem;">$750</div>
                <p style="color: {MINES_COLORS['text_dark']}; margin-bottom: 1rem;">per learning hour created</p>
                <div style="background-color: white; padding: 0.75rem; border-radius: 8px;">
                    <span style="color: {MINES_COLORS['text_dark']};">No additional revenue share</span>
                </div>
                <p style="color: {MINES_COLORS['text_muted']}; font-size: 0.85rem; margin-top: 1rem;">
                    Predictable compensation upfront
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Facilitated Courses
    st.markdown("### 👨‍🏫 Online Facilitated Courses")
    
    st.info(
        "**Note:** Facilitated delivery requires active participation from the instructor throughout the course each time it is taught.",
        icon="ℹ️"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            f"""
            <div style="background-color: {MINES_COLORS['dark_blue']}; padding: 1.5rem; border-radius: 12px; 
                        color: white; text-align: center;">
                <div style="font-size: 0.9rem; color: {MINES_COLORS['pale_blue']}; margin-bottom: 0.5rem;">Teaching Fee</div>
                <div style="font-size: 2rem; font-weight: 700;">$2,500</div>
                <div style="font-size: 0.85rem; color: {MINES_COLORS['light_blue']};">per teaching day</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="background-color: {MINES_COLORS['blaster_blue']}; padding: 1.5rem; border-radius: 12px; 
                        color: white; text-align: center;">
                <div style="font-size: 0.9rem; color: {MINES_COLORS['pale_blue']}; margin-bottom: 0.5rem;">Prep Fee</div>
                <div style="font-size: 2rem; font-weight: 700;">$1,250</div>
                <div style="font-size: 0.85rem; color: {MINES_COLORS['light_blue']};">per teaching day</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col3:
        st.markdown(
            f"""
            <div style="background-color: {MINES_COLORS['colorado_red']}; padding: 1.5rem; border-radius: 12px; 
                        color: white; text-align: center;">
                <div style="font-size: 0.9rem; color: rgba(255,255,255,0.8); margin-bottom: 0.5rem;">Revenue Share</div>
                <div style="font-size: 2rem; font-weight: 700;">20%</div>
                <div style="font-size: 0.85rem; color: rgba(255,255,255,0.8);">of net revenue</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    # Example calculation
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📊 Example Calculation")
    
    with st.expander("See example: Two-day facilitated course", expanded=True):
        st.markdown(
            f"""
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background-color: {MINES_COLORS['dark_blue']}; color: white;">
                    <th style="padding: 1rem; text-align: left;">Component</th>
                    <th style="padding: 1rem; text-align: right;">Calculation</th>
                    <th style="padding: 1rem; text-align: right;">Amount</th>
                </tr>
                <tr style="background-color: {MINES_COLORS['pale_blue']};">
                    <td style="padding: 0.75rem;">Teaching Fee</td>
                    <td style="padding: 0.75rem; text-align: right;">$2,500 × 2 days</td>
                    <td style="padding: 0.75rem; text-align: right; font-weight: 600;">$5,000</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">Preparation Fee</td>
                    <td style="padding: 0.75rem; text-align: right;">$1,250 × 2 days</td>
                    <td style="padding: 0.75rem; text-align: right; font-weight: 600;">$2,500</td>
                </tr>
                <tr style="background-color: {MINES_COLORS['pale_blue']};">
                    <td style="padding: 0.75rem;">Revenue Share</td>
                    <td style="padding: 0.75rem; text-align: right;">20% of net revenue</td>
                    <td style="padding: 0.75rem; text-align: right; font-weight: 600;">Variable</td>
                </tr>
                <tr style="background-color: {MINES_COLORS['dark_blue']}; color: white;">
                    <td style="padding: 0.75rem; font-weight: 600;">Base Total</td>
                    <td style="padding: 0.75rem;"></td>
                    <td style="padding: 0.75rem; text-align: right; font-weight: 700; font-size: 1.1rem;">$7,500 + 20%</td>
                </tr>
            </table>
            """,
            unsafe_allow_html=True,
        )

# ====================
# TAB 3: Apply Now
# ====================
with tab3:
    st.markdown("## Ready to Become an SME?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(
            f"""
            <div class="info-card">
                <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">🎯 What We're Looking For</h4>
                <ul style="color: {MINES_COLORS['text_dark']}; line-height: 1.8;">
                    <li>Deep expertise in one of our focus areas</li>
                    <li>Passion for teaching and sharing knowledge</li>
                    <li>Ability to translate complex topics for professionals</li>
                    <li>Willingness to collaborate with our learning design team</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown(
            f"""
            <div class="blue-card">
                <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">📚 What We Provide</h4>
                <ul style="color: {MINES_COLORS['text_dark']}; line-height: 1.8;">
                    <li>Dedicated Online Learning Experience Designer (OLED)</li>
                    <li>Self-study training course on course development</li>
                    <li>Ongoing support throughout the process</li>
                    <li>Review process before materials go final</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%);
                        padding: 2rem; border-radius: 12px; text-align: center; color: white;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📝</div>
                <h3 style="color: white !important; margin-bottom: 1rem;">Apply Now</h3>
                <p style="color: {MINES_COLORS['pale_blue']}; margin-bottom: 1.5rem; font-size: 0.9rem;">
                    Fill out our SME application form to get started
                </p>
                <a href="https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV" 
                   target="_blank"
                   style="background-color: {MINES_COLORS['colorado_red']}; color: white !important; 
                          padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none;
                          font-weight: 600; display: inline-block;">
                    Start Application →
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    # Contact Information
    st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
    st.markdown("### Questions?")
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 1.5rem; border-radius: 12px;">
            <p style="margin: 0; color: {MINES_COLORS['dark_blue']};">
                For more information about the SME program, please contact:
                <br><strong>Sam Spiegel</strong>, Assistant VP of Online & ProEd at Colorado School of Mines
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
