"""
MAAG (Mines AI/ML Affinity Group) Updates Page
Information about AI/ML community and mentoring programs.
"""
import streamlit as st
from pathlib import Path
import sys

st.set_page_config(
    page_title="MAAG Updates | Mines",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Mines AI/ML Affinity Group (MAAG)")
st.markdown("*Connecting AI/ML professionals with Mines students*")

st.divider()

# Overview section
st.markdown("""
The **Mines AI/ML Affinity Group (MAAG)** brings together alumni and professionals 
working in artificial intelligence and machine learning to support current students 
and foster community within the Mines network.
""")

# Key metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Alumni Mentors",
        value="10+",
        delta="invited to mentor",
        help="Alumni working in AI/ML invited to serve as student mentors"
    )

with col2:
    st.metric(
        label="Focus Area",
        value="AI/ML",
        help="Artificial Intelligence and Machine Learning"
    )

with col3:
    st.metric(
        label="Initiative",
        value="Active",
        delta="ongoing",
        help="Student mentoring program currently active"
    )

st.divider()

# Main content in columns
main_col1, main_col2 = st.columns([2, 1])

with main_col1:
    st.header("🎓 Student Mentoring Initiative")
    
    st.markdown("""
    MAAG has launched a mentoring program connecting Mines students with alumni 
    who are actively working in the AI/ML field. This initiative provides students 
    with valuable industry insights and career guidance.
    """)
    
    with st.container(border=True):
        st.subheader("Program Highlights")
        
        st.markdown("""
        **🌟 Current Status:**
        - **10+ alumni** working in AI/ML have been invited to serve as mentors
        - Focus on providing real-world industry perspectives
        - Supporting students in their AI/ML career journeys
        
        **🎯 Mentorship Goals:**
        - Share industry experience and best practices
        - Provide career guidance and networking opportunities
        - Help students understand real-world AI/ML applications
        - Bridge the gap between academic learning and industry needs
        """)
    
    st.subheader("💼 What Mentors Provide")
    
    mentor_col1, mentor_col2 = st.columns(2)
    
    with mentor_col1:
        with st.container(border=True):
            st.markdown("**🗣️ Career Guidance**")
            st.caption("Advice on career paths, job searching, and professional development in AI/ML")
        
        with st.container(border=True):
            st.markdown("**🔧 Technical Insights**")
            st.caption("Real-world perspectives on tools, technologies, and best practices")
    
    with mentor_col2:
        with st.container(border=True):
            st.markdown("**🤝 Networking**")
            st.caption("Connections to industry professionals and opportunities")
        
        with st.container(border=True):
            st.markdown("**📚 Project Feedback**")
            st.caption("Input on student projects and research directions")

with main_col2:
    st.header("📊 MAAG Impact")
    
    with st.container(border=True):
        st.markdown("### By the Numbers")
        
        st.markdown("""
        | Metric | Value |
        |--------|-------|
        | Alumni Mentors | 10+ |
        | Focus | AI/ML |
        | Status | Active |
        """)
    
    st.divider()
    
    st.info("""
    **🙋 Interested in Mentoring?**
    
    If you're a Mines alum working in AI/ML 
    and would like to mentor students, 
    please reach out to the MAAG leadership team.
    """)
    
    st.divider()
    
    st.success("""
    **🎓 For Students:**
    
    Looking for an AI/ML mentor? Connect with 
    MAAG to be matched with an industry professional.
    """)

st.divider()

# Future Plans section
st.header("🔮 Future Initiatives")

future_col1, future_col2, future_col3 = st.columns(3)

with future_col1:
    with st.container(border=True):
        st.markdown("### 📅 Events")
        st.markdown("""
        - Industry speaker series
        - Virtual networking events
        - Career panels
        - Technical workshops
        """)

with future_col2:
    with st.container(border=True):
        st.markdown("### 🤝 Partnerships")
        st.markdown("""
        - Industry collaborations
        - Research partnerships
        - Internship programs
        - Project sponsorships
        """)

with future_col3:
    with st.container(border=True):
        st.markdown("### 📚 Resources")
        st.markdown("""
        - Learning materials
        - Career guides
        - Tool recommendations
        - Best practice documentation
        """)

# Get Involved section
st.divider()

st.header("🚀 Get Involved")

involved_col1, involved_col2 = st.columns(2)

with involved_col1:
    st.subheader("For Alumni")
    
    st.markdown("""
    **Ways to Contribute:**
    
    1. **Become a Mentor** - Share your experience with students
    2. **Speak at Events** - Present on AI/ML topics
    3. **Share Job Opportunities** - Help students find positions
    4. **Contribute Resources** - Share learning materials
    """)
    
    with st.expander("📧 Contact Information"):
        st.markdown("""
        Interested in joining MAAG or becoming a mentor?
        
        Reach out to the MAAG leadership team through the 
        Mines Alumni Association or ProEd office.
        """)

with involved_col2:
    st.subheader("For Students")
    
    st.markdown("""
    **Opportunities Available:**
    
    1. **Request a Mentor** - Get matched with an industry professional
    2. **Attend Events** - Join MAAG-sponsored activities
    3. **Share Your Work** - Present projects to alumni
    4. **Ask Questions** - Tap into the community's expertise
    """)
    
    with st.expander("🎓 Student Resources"):
        st.markdown("""
        Connect with MAAG through:
        
        - Mines Career Center
        - AI/ML student organizations
        - ProEd office
        - Alumni Association events
        """)

# Sidebar
with st.sidebar:
    st.header("MAAG Quick Facts")
    
    st.markdown("""
    **Mission:**
    
    Connect AI/ML professionals 
    with Mines students to foster 
    learning and career development.
    """)
    
    st.divider()
    
    st.markdown("""
    **Key Activities:**
    
    - 🎓 Student Mentoring
    - 📅 Industry Events
    - 🤝 Networking
    - 📚 Resource Sharing
    """)
    
    st.divider()
    
    st.info("""
    **Current Focus:**
    
    Building the mentoring program 
    with 10+ alumni mentors from the 
    AI/ML industry.
    """)
