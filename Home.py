import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Snowflake for the Cleveland Cavaliers",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Cavs branding
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #6F263D 0%, #041E42 100%);
        padding: 2rem 3rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        border-left: 6px solid #FFB81C;
    }
    .main-header h1 {
        color: #FFFFFF;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        color: #FFB81C;
        font-size: 1.2rem;
        margin: 0;
    }
    .metric-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: #FFB81C;
    }
    .metric-value {
        color: #FFB81C;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    .metric-label {
        color: #FFFFFF;
        font-size: 0.9rem;
        opacity: 0.85;
    }
    .nav-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C22;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #FFB81C;
    }
    .nav-card h3 {
        color: #FFB81C;
        margin-bottom: 0.5rem;
    }
    .nav-card p {
        color: #FFFFFF;
        opacity: 0.8;
        font-size: 0.9rem;
    }
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .section-divider {
        border: none;
        height: 2px;
        background: linear-gradient(to right, #6F263D, #FFB81C, #041E42);
        margin: 2rem 0;
    }
    [data-testid="stSidebar"] {
        background: #0a1929;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar branding
logo_path = Path(__file__).parent / "assets" / "cavs_small.png"
if logo_path.exists():
    st.sidebar.image(str(logo_path), width=120)
st.sidebar.markdown("### Snowflake Data Platform")
st.sidebar.markdown("*Prepared for the Cleveland Cavaliers*")
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Navigate Topics:**
- Platform Simplicity
- Data Sharing
- Governance
- Cost Intelligence
- Fivetran & dbt
- NBA Partnership
""")

# Hero Section
st.markdown("""
<div class="main-header">
    <h1>Snowflake for the Cleveland Cavaliers</h1>
    <p>A unified data platform built for performance, governance, and growth</p>
</div>
""", unsafe_allow_html=True)

# Quick metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Analytics Bridge</div>
        <div class="metric-value">pg_lake</div>
        <div class="metric-label">Postgres → Iceberg → Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Infrastructure Ops</div>
        <div class="metric-value">Zero</div>
        <div class="metric-label">Fully managed platform</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Cost Model</div>
        <div class="metric-value">Pay-per-query</div>
        <div class="metric-label">Auto-suspend when idle</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">NBA Partner</div>
        <div class="metric-value">Official</div>
        <div class="metric-label">Cloud Data Platform</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Navigation cards
st.markdown("## Explore the Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="nav-card">
        <h3>🏗️ Platform Simplicity</h3>
        <p>One platform, all workloads. Eliminate custom infrastructure and operational burden.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-card">
        <h3>🔗 Data Sharing</h3>
        <p>Zero-copy sharing with sponsors, partners, and the league — no ETL required.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="nav-card">
        <h3>🛡️ Governance</h3>
        <p>Automated classification, masking, lineage, and audit — centralized in Horizon.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-card">
        <h3>💰 Cost Intelligence</h3>
        <p>Per-workload tracking, resource monitors, budgets, and pay-per-query economics.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="nav-card">
        <h3>⚡ Fivetran & dbt</h3>
        <p>500+ managed connectors, existing dbt models migrate seamlessly.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-card">
        <h3>🏀 NBA Partnership</h3>
        <p>Same platform powering league analytics — competitive advantage built in.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Why Snowflake callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why Snowflake for the Cavaliers?</strong><br><br>
    The Cavaliers need a platform that grows with the organization — from fan engagement and 
    ticketing analytics to league reporting and sponsor partnerships. Snowflake delivers this as 
    a single, governed platform with zero infrastructure to manage, instant elasticity, and 
    native data sharing that connects you directly to the NBA ecosystem.<br><br>
    <em style="color: #FFB81C;">Use the sidebar to explore each topic in depth →</em>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; opacity: 0.6; font-size: 0.8rem;'>"
    "Prepared by Snowflake Solutions Engineering | 2025"
    "</div>",
    unsafe_allow_html=True
)
