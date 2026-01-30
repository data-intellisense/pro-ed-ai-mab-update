"""
Mines AI/ML Affinity Group (MAAG) Updates Page
Student mentoring initiatives and AI/ML community building
"""
import streamlit as st
from utils import (
    apply_mines_styling,
    render_sidebar,
    MINES_COLORS,
)

# Page configuration
st.set_page_config(
    page_title="MAAG Updates | Mines ProEd",
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
        <h1 style="color: {MINES_COLORS['dark_blue']};">🤖 Mines AI/ML Affinity Group (MAAG)</h1>
        <p style="color: {MINES_COLORS['text_muted']}; font-size: 1.1rem;">
            Connecting AI/ML professionals with Mines students through mentorship
        </p>
    </div>
    <div class="mines-divider"></div>
    """,
    unsafe_allow_html=True,
)

# Hero Banner
st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['earth_blue']} 100%);
                padding: 3rem 2rem; border-radius: 16px; color: white; text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🎓🤝🤖</div>
        <h2 style="color: white !important; margin-bottom: 1rem;">Student Mentorship Program</h2>
        <p style="color: {MINES_COLORS['pale_blue']}; font-size: 1.2rem; max-width: 600px; margin: 0 auto;">
            Building the next generation of AI/ML leaders through alumni mentorship
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Key Highlight
st.markdown("## 🌟 Latest Initiative")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 2rem; border-radius: 12px; 
                    border-left: 6px solid {MINES_COLORS['colorado_red']};">
            <h3 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 1rem;">
                Spring 2026 Mentorship Launch
            </h3>
            <p style="color: {MINES_COLORS['text_dark']}; font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">
                MAAG is excited to announce that we have invited <strong style="color: {MINES_COLORS['colorado_red']};">10+ alumni</strong> 
                working in the AI/ML field to serve as mentors for Mines students starting <strong>Spring 2026</strong>.
            </p>
            <p style="color: {MINES_COLORS['text_muted']}; margin: 0;">
                This initiative connects experienced professionals with students eager to learn about 
                real-world AI/ML applications, career paths, and industry insights.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 100%);
                    padding: 2rem; border-radius: 12px; text-align: center; color: white;">
            <div style="font-size: 3.5rem; font-weight: 700; margin-bottom: 0.5rem;">10+</div>
            <div style="font-size: 1.1rem; color: {MINES_COLORS['pale_blue']};">Alumni Mentors</div>
            <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.2);">
                <div style="font-size: 1.5rem; font-weight: 600;">Spring 2026</div>
                <div style="font-size: 0.9rem; color: {MINES_COLORS['pale_blue']};">Program Launch</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Program Benefits
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## 💡 Program Benefits")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div style="background-color: white; padding: 1.5rem; border-radius: 12px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 280px;">
            <div style="background-color: {MINES_COLORS['pale_blue']}; width: 60px; height: 60px; 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center;
                        font-size: 1.75rem; margin-bottom: 1rem;">👨‍🎓</div>
            <h4 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 0.75rem;">For Students</h4>
            <ul style="color: {MINES_COLORS['text_dark']}; padding-left: 1.25rem; font-size: 0.9rem; line-height: 1.8;">
                <li>Direct access to industry professionals</li>
                <li>Career guidance and advice</li>
                <li>Real-world project insights</li>
                <li>Networking opportunities</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color: white; padding: 1.5rem; border-radius: 12px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 280px;">
            <div style="background-color: {MINES_COLORS['pale_blue']}; width: 60px; height: 60px; 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center;
                        font-size: 1.75rem; margin-bottom: 1rem;">👨‍💼</div>
            <h4 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 0.75rem;">For Mentors</h4>
            <ul style="color: {MINES_COLORS['text_dark']}; padding-left: 1.25rem; font-size: 0.9rem; line-height: 1.8;">
                <li>Give back to the Mines community</li>
                <li>Shape future AI/ML talent</li>
                <li>Stay connected with campus</li>
                <li>Build leadership skills</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div style="background-color: white; padding: 1.5rem; border-radius: 12px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 280px;">
            <div style="background-color: {MINES_COLORS['pale_blue']}; width: 60px; height: 60px; 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center;
                        font-size: 1.75rem; margin-bottom: 1rem;">🏛️</div>
            <h4 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 0.75rem;">For Mines</h4>
            <ul style="color: {MINES_COLORS['text_dark']}; padding-left: 1.25rem; font-size: 0.9rem; line-height: 1.8;">
                <li>Strengthen alumni connections</li>
                <li>Enhance student experience</li>
                <li>Industry-aligned education</li>
                <li>Build AI/ML community</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# About MAAG
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## 🎯 About MAAG")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(
        f"""
        <div class="info-card">
            <h4 style="margin-top: 0; color: {MINES_COLORS['dark_blue']};">What is MAAG?</h4>
            <p style="color: {MINES_COLORS['text_dark']}; line-height: 1.8; margin-bottom: 1rem;">
                The <strong>Mines AI/ML Affinity Group (MAAG)</strong> is a community of Mines alumni 
                working in artificial intelligence and machine learning fields. Our mission is to:
            </p>
            <ul style="color: {MINES_COLORS['text_dark']}; line-height: 1.8;">
                <li>Connect AI/ML professionals in the Mines alumni network</li>
                <li>Support current students interested in AI/ML careers</li>
                <li>Share knowledge and best practices across industries</li>
                <li>Promote Mines as a leader in AI/ML education</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, {MINES_COLORS['colorado_red']} 0%, #E05A3C 100%);
                    padding: 1.5rem; border-radius: 12px; color: white;">
            <h4 style="color: white !important; margin-bottom: 1rem;">🚀 AI/ML Fields Represented</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                {' '.join([f'<span style="background-color: rgba(255,255,255,0.2); padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.85rem;">{field}</span>' for field in ['Machine Learning', 'Deep Learning', 'NLP', 'Computer Vision', 'MLOps', 'Data Science', 'GenAI', 'Robotics']])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# How to Get Involved
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)
st.markdown("## 🤝 Get Involved")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['pale_blue']}; padding: 2rem; border-radius: 12px;">
            <h4 style="color: {MINES_COLORS['dark_blue']} !important; margin-bottom: 1rem;">
                👨‍💼 Alumni: Become a Mentor
            </h4>
            <p style="color: {MINES_COLORS['text_dark']}; margin-bottom: 1.5rem;">
                If you're working in AI/ML and want to mentor Mines students, we'd love to hear from you!
            </p>
            <div style="background-color: white; padding: 1rem; border-radius: 8px;">
                <p style="color: {MINES_COLORS['text_dark']}; margin: 0; font-size: 0.9rem;">
                    <strong>Time Commitment:</strong> Flexible - typically a few hours per semester<br>
                    <strong>Format:</strong> Virtual meetings, email exchanges, career advice
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color: {MINES_COLORS['dark_blue']}; padding: 2rem; border-radius: 12px; color: white;">
            <h4 style="color: white !important; margin-bottom: 1rem;">
                👨‍🎓 Students: Join the Program
            </h4>
            <p style="color: {MINES_COLORS['pale_blue']}; margin-bottom: 1.5rem;">
                Interested in being mentored by an AI/ML professional? Sign up for the Spring 2026 cohort!
            </p>
            <div style="background-color: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px;">
                <p style="color: {MINES_COLORS['pale_blue']}; margin: 0; font-size: 0.9rem;">
                    <strong>Eligibility:</strong> Current Mines students interested in AI/ML<br>
                    <strong>Benefits:</strong> 1-on-1 mentorship, career guidance, networking
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact Section
st.markdown("<div class='mines-divider'></div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div style="background: linear-gradient(90deg, {MINES_COLORS['dark_blue']} 0%, {MINES_COLORS['blaster_blue']} 50%, {MINES_COLORS['dark_blue']} 100%);
                padding: 2rem; border-radius: 12px; text-align: center; color: white;">
        <h3 style="color: white !important; margin-bottom: 0.5rem;">Want to Learn More?</h3>
        <p style="color: {MINES_COLORS['pale_blue']}; margin-bottom: 1rem;">
            Reach out to learn more about MAAG and how you can contribute to our student mentorship initiative.
        </p>
        <p style="color: {MINES_COLORS['golden_tech']}; font-weight: 600; margin: 0;">
            Part of the Mines Alumni Board Life Long Learning & Development Committee
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
