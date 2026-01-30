"""
ProEd Program Information Page
Detailed information about SME roles and financial models.
"""
import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import FOCUS_AREAS, FINANCIAL_MODEL, SME_APPLICATION_LINK, read_docx_content, get_data_path

st.set_page_config(
    page_title="ProEd Program | Mines",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ProEd Program Information")
st.markdown("*Comprehensive guide to the Mines Professional Education program*")

st.divider()

# Tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs([
    "🎓 SME Overview", 
    "💰 Financial Models", 
    "📢 Promotion & Awareness",
    "📄 Swipe File Content"
])

# Tab 1: SME Overview
with tab1:
    st.header("What is a Subject Matter Expert (SME)?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        A **Subject Matter Expert (SME)** provides content and materials to develop professional 
        education short courses. This includes:
        
        - 📝 Text content and written materials
        - 🎨 Graphics and visual elements
        - 📊 Slides and presentations
        - 🎥 Video content
        
        An **Online Learning Experience Designer (OLED)** will work with you to build the 
        online course components. The SME reviews all course materials before finalization.
        """)
        
        st.subheader("Course Formats")
        format_col1, format_col2 = st.columns(2)
        
        with format_col1:
            with st.container(border=True):
                st.markdown("**🖥️ Online Self-Study**")
                st.caption("Learn at your own pace, anytime, anywhere")
            
            with st.container(border=True):
                st.markdown("**🏫 In-Person**")
                st.caption("Traditional classroom experience")
        
        with format_col2:
            with st.container(border=True):
                st.markdown("**👨‍🏫 Online Facilitated**")
                st.caption("Instructor-led virtual sessions")
            
            with st.container(border=True):
                st.markdown("**🔄 Hybrid**")
                st.caption("Combined online and in-person")
    
    with col2:
        st.info("""
        **⏱️ Time Commitment**
        
        Approximately **4 hours** of preparation 
        for every **1 hour** of learning content.
        
        *Training and support provided throughout the process.*
        """)
        
        st.link_button(
            "📝 Apply to be an SME",
            SME_APPLICATION_LINK,
            type="primary",
            use_container_width=True
        )
    
    st.subheader("🎯 Focus Areas")
    st.markdown("We are seeking course development in the following areas:")
    
    focus_cols = st.columns(3)
    icons = ["🔋", "🤖", "📈", "⛏️", "🚀", "🏗️"]
    
    for i, (area, icon) in enumerate(zip(FOCUS_AREAS, icons)):
        with focus_cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{icon} {area}**")

# Tab 2: Financial Models
with tab2:
    st.header("💰 SME Financial Models")
    
    # Self-Paced Courses
    st.subheader("📖 Self-Paced (On-Demand) Courses")
    
    opt_col1, opt_col2 = st.columns(2)
    
    with opt_col1:
        with st.container(border=True):
            st.markdown("### Option A: Revenue Share Model")
            st.metric(
                label="Base Compensation",
                value="$250",
                delta="per learning hour created"
            )
            st.markdown("**Plus:** 20% of net revenue share")
            st.caption("Ideal for courses with high enrollment potential")
    
    with opt_col2:
        with st.container(border=True):
            st.markdown("### Option B: Flat Rate Model")
            st.metric(
                label="Base Compensation",
                value="$750",
                delta="per learning hour created"
            )
            st.markdown("**Revenue Share:** None")
            st.caption("Predictable income, no ongoing revenue")
    
    st.divider()
    
    # Facilitated Courses
    st.subheader("👨‍🏫 Online Facilitated Courses")
    
    st.warning("""
    **Note:** Facilitated delivery requires active participation from the instructor 
    throughout the course each time it is taught.
    """)
    
    fac_col1, fac_col2, fac_col3 = st.columns(3)
    
    with fac_col1:
        st.metric(
            label="Teaching Compensation",
            value="$2,500",
            delta="per teaching day"
        )
    
    with fac_col2:
        st.metric(
            label="Preparation Fee",
            value="$1,250",
            delta="per teaching day"
        )
    
    with fac_col3:
        st.metric(
            label="Revenue Share",
            value="20%",
            delta="of net revenue"
        )
    
    # Example calculation
    with st.expander("📊 Example: Two-Day Course Calculation"):
        st.markdown("""
        For a **two-day facilitated course**:
        
        | Component | Calculation | Amount |
        |-----------|-------------|--------|
        | Teaching | 2 days × $2,500 | $5,000 |
        | Preparation | 2 days × $1,250 | $2,500 |
        | **Total Base** | | **$7,500** |
        | Revenue Share | 20% of net revenue | Variable |
        """)

# Tab 3: Promotion & Awareness
with tab3:
    st.header("📢 Promotion & Awareness Building")
    
    st.markdown("""
    Promotion of ProEd is currently in the **awareness building** phase. 
    Word of mouth and opportunities to make alumni aware of the program are greatly appreciated.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Promotion Efforts")
        
        with st.container(border=True):
            st.markdown("**📧 Email Campaigns**")
            st.caption("Based on funding and available resources")
        
        with st.container(border=True):
            st.markdown("**🎉 idigMines Events**")
            st.caption("ProEd will be a highlighted cause in mid-February events")
        
        with st.container(border=True):
            st.markdown("**📋 Swipe Sheet**")
            st.caption("Available for consistent messaging and links")
    
    with col2:
        st.subheader("How You Can Help")
        
        st.success("""
        **Ways to Support ProEd Awareness:**
        
        - 🗣️ Share with your professional network
        - 📱 Post about ProEd on social media
        - 👥 Mention to fellow Mines alumni
        - 📧 Forward information to interested colleagues
        - 🎤 Speak about ProEd at events
        """)
    
    st.divider()
    
    st.subheader("🤖 AI Integration")
    
    st.info("""
    **Future AI Opportunities:**
    
    There is openness to conversations about using AI both in course development and promotion. 
    
    Note: The HiTA (AI Teaching Assistant) program is currently only available for credit-bearing 
    courses, not for ProEd. Future plans for this program are being evaluated.
    """)

# Tab 4: Swipe File Content
with tab4:
    st.header("📄 ProEd Swipe File Content")
    st.markdown("*Content from the official Mines ProEd Swipe File document*")
    
    # Try to load the DOCX file
    docx_path = get_data_path() / "MINES PROED SWIPE FILE.docx"
    
    if docx_path.exists():
        try:
            content = read_docx_content(str(docx_path))
            
            if content:
                current_heading = None
                for item in content:
                    if item["type"] == "heading":
                        level = item.get("level", 1)
                        if level == 1:
                            st.header(item["content"])
                        elif level == 2:
                            st.subheader(item["content"])
                        else:
                            st.markdown(f"**{item['content']}**")
                        current_heading = item["content"]
                    elif item["type"] == "list_item":
                        st.markdown(f"- {item['content']}")
                    else:
                        st.markdown(item["content"])
            else:
                st.info("The swipe file appears to be empty or could not be parsed.")
                
        except Exception as e:
            st.error(f"Error loading document: {str(e)}")
            st.info("Please ensure python-docx is installed: `pip install python-docx`")
    else:
        st.warning(f"Swipe file not found at: {docx_path}")
        st.info("Please ensure the 'MINES PROED SWIPE FILE.docx' is in the data folder.")

# Sidebar info
with st.sidebar:
    st.header("Quick Links")
    
    st.link_button(
        "📝 SME Application",
        SME_APPLICATION_LINK,
        use_container_width=True
    )
    
    st.divider()
    
    st.markdown("""
    **Contact:**
    
    Sam Spiegel  
    *Assistant VP of Online & ProEd*  
    Colorado School of Mines
    """)
