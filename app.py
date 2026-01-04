import streamlit as st
import pandas as pd
from pathlib import Path
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Rajat Singh - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #1E40AF;
        border-bottom: 3px solid #3B82F6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #F1F5F9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 1rem 0;
    }
    .skill-tag {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        display: inline-block;
        margin: 0.3rem;
        font-size: 0.9rem;
    }
    .download-btn {
        background-color: #3B82F6;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem 0.5rem 0.5rem 0;
        font-size: 0.95rem;
    }
    .download-btn:hover {
        background-color: #2563EB;
    }
    .contact-info {
        font-size: 1.1rem;
        color: #475569;
    }
    .assignment-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 8px;
        border: 2px solid #E2E8F0;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .assignment-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: #1E40AF;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Function to create download link
def get_download_link(file_path, file_label):
    """Generate a download link for files"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        file_name = Path(file_path).name
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="download-btn">📥 Download {file_label}</a>'
        return href
    except FileNotFoundError:
        return f'<span style="color: red;">⚠️ File not found: {file_label}</span>'

# Function to get all assignment files
def get_assignment_files():
    """Get all Excel files from assignments folder"""
    assignments_path = Path("assets/assignments")
    if assignments_path.exists():
        return list(assignments_path.glob("*.xlsx")) + list(assignments_path.glob("*.xls"))
    return []

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "👤 About Me",
    "💼 Experience",
    "🎓 Education",
    "🛠️ Skills",
    "📊 Projects & Research",
    "📄 Documents",
    "📞 Contact"
])

# Main Content Based on Selection
if page == "🏠 Home":
    st.markdown('<div class="main-header">RAJAT SINGH</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Financial Professional | Investment Banking | Wealth Management</div>', unsafe_allow_html=True)
    
    # Profile Image and Introduction
    col1, col2, col3 = st.columns([1.2, 2.5, 1.3])
    
    with col1:
        # Add spacing to align with content
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        # Check if profile image exists
        profile_image_path = Path("images/profile_photo.jpg")
        if profile_image_path.exists():
            st.image(str(profile_image_path), use_container_width=True)
        else:
            st.info("📸 Add your photo as 'profile_photo.jpg' in the images folder")
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h3 style="text-align: center; color: #1E40AF;">Welcome to My Portfolio</h3>
        <p style="text-align: center; line-height: 1.8;">
        Results-driven financial professional with experience in client relationship management and 
        portfolio handling, seeking to leverage analytical skills and financial knowledge in investment banking.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Add spacing to align with content
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # Resume Download Button
        st.markdown(get_download_link("assets/resume.pdf", "My Resume"), unsafe_allow_html=True)
        
        # LinkedIn Link
        st.markdown("""
        <a href="https://www.linkedin.com/in/rajat-singh-810993128/" target="_blank" class="download-btn" style="background-color: #0A66C2;">
        💼 LinkedIn Profile
        </a>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown('<div class="section-header">Professional Highlights</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("HNI Clients Managed", "300+")
    with col2:
        st.metric("Compliance Record", "100%")
    with col3:
        st.metric("Target Achievement", "120%")
    with col4:
        st.metric("Experience", "1+ Year")

elif page == "👤 About Me":
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <p style="font-size: 1.1rem; line-height: 1.8;">
    I am a results-driven financial professional with a strong background in <b>client relationship management</b> 
    and <b>portfolio handling</b>. Currently pursuing my Master's in <b>Global Finance</b> from SP Jain School of 
    Global Management, I am seeking to leverage my analytical skills and financial knowledge in investment banking.
    </p>
    <p style="font-size: 1.1rem; line-height: 1.8;">
    My experience includes managing 300+ HNI clients at ICICI Bank, where I maintained a perfect compliance record 
    while consistently exceeding quarterly targets by 120%. I specialize in wealth management, financial analysis, 
    and building trustworthy client partnerships.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Personal Attributes")
    attributes = [
        "Attention to Detail", "Analytical", "Motivated", "Committed",
        "Ethical", "Highly Competitive", "Supportive", "Caring"
    ]
    
    attr_html = "".join([f'<span class="skill-tag">{attr}</span>' for attr in attributes])
    st.markdown(attr_html, unsafe_allow_html=True)

elif page == "💼 Experience":
    st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🏦 ICICI Bank, India
    **Deputy Manager** | January 2017 - January 2018
    
    <div class="info-box">
    <h4>Key Responsibilities & Achievements:</h4>
    <ul style="font-size: 1.05rem; line-height: 1.8;">
        <li>Led financial analysis and advisory for <b>300+ HNI clients</b>, demonstrating strong analytical and 
        client relationship management capabilities within wealth management</li>
        <li>Structured and executed complex financial transactions while ensuring <b>100% compliance</b> with 
        regulatory requirements, including KYC and AML protocols</li>
        <li>Demonstrated exceptional attention to detail through a perfect KYC/AML compliance record, 
        supporting risk management objectives</li>
        <li>Successfully managed multiple competing priorities while consistently achieving <b>120% of quarterly 
        targets</b>, contributing to sales objectives</li>
        <li>Developed and presented comprehensive client presentations using PowerPoint and Excel for 
        investment recommendations, supporting wealth planning</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏆 Awards & Achievements")
    st.markdown("""
    <div class="info-box">
    <ul style="font-size: 1.05rem;">
        <li>🥇 <b>Certificate of Appreciation</b> - Recognized as Top Performer in branch-level CASA acquisition drive (Q3 2017)</li>
        <li>🥈 <b>Sword of Honors</b> - Achieved 2nd place in regional product knowledge competition</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "🎓 Education":
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
    
    # Master's Degree
    st.markdown("""
    ### 🎓 Master of Global Business (Global Finance Specialization)
    **SP Jain School of Global Management** | Singapore-Dubai  
    **Duration:** June 2025 - May 2026 (Expected)
    
    <div class="info-box">
    <p><b>Key Knowledge Areas:</b></p>
    <ul style="font-size: 1.05rem;">
        <li>Financial Modeling & Valuation Methods</li>
        <li>Investment Banking & M&A</li>
        <li>Corporate Finance & Capital Markets</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Post Graduate Diploma
    st.markdown("""
    ### 📜 Post Graduate Diploma in Banking
    **Manipal University**  
    **Year:** 2016 - 2017
    
    <div class="info-box">
    <p style="font-size: 1.05rem; line-height: 1.8;">
    Comprehensive program focused on banking operations, financial services, and regulatory compliance. 
    Developed expertise in retail banking, wealth management, and core banking systems including KYC/AML protocols.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bachelor's Degree
    st.markdown("""
    ### 🎓 Bachelor's of Arts (Economics and Political Science)
    **Lucknow Christian College**  
    **Year:** 2012 - 2015
    
    <div class="info-box">
    <p style="font-size: 1.05rem; line-height: 1.8;">
    Foundation degree in Economics and Political Science providing strong analytical and critical thinking skills. 
    Studied macroeconomics, microeconomics, public policy, and political systems, establishing a solid base for financial career.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("### 📜 Certifications")
    st.markdown("""
    <div class="info-box">
    <ul style="font-size: 1.05rem;">
        <li>Post Graduate Diploma in Banking</li>
        <li>Design Thinking</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "🛠️ Skills":
    st.markdown('<div class="section-header">Skills & Expertise</div>', unsafe_allow_html=True)
    
    # Client Relationships & Sales
    st.markdown("### 💼 Client Relationships & Sales")
    skills_sales = [
        "HNI/NRI Client Handling", "Cross-selling (CASA, Loans, LI, FD, PPF)",
        "Sales", "Client Advisory", "Building Trustworthy Partnerships"
    ]
    skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills_sales])
    st.markdown(skills_html, unsafe_allow_html=True)
    
    # Wealth Management & Planning
    st.markdown("### 📈 Wealth Management & Planning")
    skills_wealth = [
        "Wealth Management", "Wealth Planning", "Portfolio Handling",
        "Investment Banking", "Capital Markets", "Asset Management",
        "Financial Services", "Risk Management", "Financial Analysis",
        "Financial Modeling", "Valuation Analysis", "M&A Transaction Support"
    ]
    skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills_wealth])
    st.markdown(skills_html, unsafe_allow_html=True)
    
    # Operations & Compliance
    st.markdown("### ⚙️ Operations & Compliance")
    skills_ops = [
        "KYC & AML Compliance", "Preparing Reports", "Regulatory Compliance",
        "Deal Documentation", "NEFT, RTGS, Fund Transfers",
        "Finacle Core Banking", "Sales CRM", "Banking Software Proficiency"
    ]
    skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills_ops])
    st.markdown(skills_html, unsafe_allow_html=True)
    
    # Technical Skills
    st.markdown("### 💻 Technical Skills")
    skills_tech = [
        "Microsoft Excel (Advanced Financial Modeling)",
        "Financial Analysis Tools",
        "Presentation Software (PowerPoint)",
        "Python", "Streamlit"
    ]
    skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills_tech])
    st.markdown(skills_html, unsafe_allow_html=True)
    
    # Communication & Collaboration
    st.markdown("### 🗣️ Communication & Collaboration")
    skills_comm = [
        "Written Communication", "Verbal Communication",
        "Excellent Interpersonal Skills", "Client Presentation",
        "Collaboration"
    ]
    skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills_comm])
    st.markdown(skills_html, unsafe_allow_html=True)

elif page == "📊 Projects & Research":
    st.markdown('<div class="section-header">Projects & Research</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 📱 ONDC Research Project (Ongoing)
    **Topic:** Evaluating the Financial Impact of ONDC on Small Retailers and Gig Service Providers in India
    
    <div class="info-box">
    <h4>Project Overview:</h4>
    <p style="font-size: 1.05rem; line-height: 1.8;">
    This study explores how <b>ONDC (Open Network for Digital Commerce)</b>, a government-backed digital 
    commerce initiative, is transforming the financial landscape for small retailers and gig-based service 
    providers such as taxi drivers and food delivery agents in India.
    </p>
    
    <h4>Key Research Areas:</h4>
    <ul style="font-size: 1.05rem; line-height: 1.8;">
        <li>Impact of ONDC on working capital efficiency</li>
        <li>Income stability for small retailers</li>
        <li>Financial transformation of gig service providers</li>
        <li>Analysis of early-adopting cities</li>
    </ul>
    
    <p style="font-size: 1.05rem; line-height: 1.8;">
    <b>Duration:</b> Term 1 and 2 Project<br>
    <b>Status:</b> In Progress
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Academic Assignments")
    st.markdown("""
    <div class="info-box">
    <p style="font-size: 1.05rem;">
    Throughout my MGB program, I have completed various assignments focusing on:
    </p>
    <ul style="font-size: 1.05rem;">
        <li><b>Time Value of Money</b> - Financial calculations and analysis</li>
        <li><b>Corporate Finance</b> - Domino's case study and financial statement analysis</li>
        <li><b>Financial Transactions</b> - DABANG Pharma Ltd comprehensive analysis</li>
        <li><b>Financial Statement Analysis</b> - Advanced modeling techniques</li>
    </ul>
    <p style="font-size: 0.95rem; color: #64748B; margin-top: 1rem;">
    💡 All assignments are available for download in the <b>Documents</b> section
    </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "📄 Documents":
    st.markdown('<div class="section-header">Downloadable Documents</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <p style="font-size: 1.1rem;">
    📥 Download my resume, academic assignments, and research papers below:
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Resume Section
    st.markdown("### 📄 Resume & CV")
    st.markdown(get_download_link("assets/resume.pdf", "Resume (PDF)"), unsafe_allow_html=True)
    st.markdown("---")
    
    # Academic Assignments Section
    st.markdown("### 📊 Academic Assignments")
    st.markdown("**MGB Program - Financial Analysis & Modeling**")
    
    # Get all assignment files dynamically
    assignment_files = get_assignment_files()
    
    if assignment_files:
        for assignment_file in assignment_files:
            file_name = assignment_file.name
            # Remove .xlsx or .xls extension for display
            display_name = file_name.replace('.xlsx', '').replace('.xls', '')
            
            st.markdown(f"""
            <div class="assignment-card">
                <div class="assignment-title">📈 {display_name}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(get_download_link(str(assignment_file), file_name), unsafe_allow_html=True)
    else:
        st.info("📁 Assignment files will appear here once uploaded to the assets/assignments folder")
    
    st.markdown("---")
    
    # Research Papers Section
    st.markdown("### 📝 Research Papers")
    st.markdown("**Ongoing Research Projects**")
    
    research_path = Path("assets/research/ondc_research.docx")
    if research_path.exists():
        st.markdown("""
        <div class="assignment-card">
            <div class="assignment-title">🔬 ONDC Research - Financial Impact Analysis</div>
            <p style="color: #64748B; margin: 0.5rem 0 0 0;">
            Study on Open Network for Digital Commerce impact on small retailers and gig workers
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(get_download_link("assets/research/ondc_research.docx", "ONDC Research (Word)"), unsafe_allow_html=True)
    else:
        st.info("📁 Research paper will appear here once uploaded to assets/research folder")
    
    st.markdown("---")
    
    # Certifications Section
    st.markdown("### 📜 Certifications")
    st.markdown("""
    <div class="info-box">
    <p style="font-size: 1rem;">
    ✅ Post Graduate Diploma in Banking - Manipal University<br>
    ✅ Design Thinking Certification<br><br>
    <span style="color: #64748B; font-size: 0.9rem;">
    📧 Additional certification documents available upon request
    </span>
    </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "📞 Contact":
    st.markdown('<div class="section-header">Contact Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>📍 Location</h3>
        <p class="contact-info">Nova Tower, Silicon Oasis<br>Dubai, UAE</p>
        
        <h3>📧 Email</h3>
        <p class="contact-info">rajatsingh199412@gmail.com</p>
        
        <h3>📱 Phone</h3>
        <p class="contact-info">+971 58 130 9517</p>
        
        <h3>💼 LinkedIn</h3>
        <p class="contact-info">
        <a href="https://www.linkedin.com/in/rajat-singh-810993128/" target="_blank" style="color: #0A66C2; text-decoration: none;">
        Connect with me on LinkedIn →
        </a>
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📬 Send Me a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message", height=150)
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("Thank you! Your message has been received. I'll get back to you soon!")
                else:
                    st.error("Please fill in all fields.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; padding: 2rem 0;">
    <p>© 2026 Rajat Singh | Built with Streamlit & Python</p>
    <p>Last Updated: January 2026</p>
</div>
""", unsafe_allow_html=True)