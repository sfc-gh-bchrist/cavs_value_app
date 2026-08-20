import streamlit as st

st.set_page_config(page_title="NBA Partnership | Cavs + Snowflake", page_icon="🏀", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .partnership-hero {
        background: linear-gradient(135deg, #6F263D 0%, #041E42 100%);
        border: 2px solid #FFB81C;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .partnership-hero h2 { color: #FFB81C; }
    .partnership-hero p { color: #FFFFFF; font-size: 1.1rem; }
    .use-case-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.2rem;
        margin: 0.5rem 0;
        min-height: 150px;
    }
    .use-case-card h4 { color: #FFB81C; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🏀 NBA Partnership")
st.markdown("*The NBA is building its data infrastructure on Snowflake — a strategic advantage for teams on the platform.*")
st.markdown("---")

# Hero
st.markdown("""
<div class="partnership-hero">
    <h2>Snowflake x NBA</h2>
    <p>The NBA has selected Snowflake as a core platform for its data and analytics infrastructure</p>
    <p style="font-size: 0.9rem; color: #FFB81C;">Multi-year strategic partnership</p>
</div>
""", unsafe_allow_html=True)

# Public partnership details
st.markdown("## The League Partnership")

tab1, tab2, tab3 = st.tabs(["What Snowflake Powers", "Data Products", "League Analytics"])

with tab1:
    st.markdown("""
    ### Snowflake Powers NBA's Data Infrastructure
    
    The NBA is building on Snowflake to:
    
    - **Unify** player tracking, game stats, and operational data
    - **Enable** real-time analytics for broadcasts, coaching, and fan engagement
    - **Power** advanced statistics used by teams, media, and fans
    - **Scale** to handle billions of data points per game from player tracking
    
    | Capability | Description |
    |-----------|-------------|
    | **Player Tracking** | Hawk-Eye (Sony) optical tracking — position, speed, distance for every player, every frame |
    | **Advanced Stats** | Win probability, shot quality, defensive matchups |
    | **Real-time Feeds** | Live game data powering broadcasts and apps |
    | **Historical Archive** | Decades of game data, standardized and queryable |
    | **Fan Engagement** | Personalized content, fantasy sports, betting integrations |
    
    The NBA is consolidating these capabilities on Snowflake — the same platform you'd be adopting.
    """)

with tab2:
    st.markdown("""
    ### NBA Data Products via Snowflake
    
    The NBA is building toward delivering data products to teams via Snowflake Data Sharing:
    """)

    st.markdown("""
<div style="background: #0a1929; border-radius: 12px; padding: 1.5rem; border: 1px solid #FFB81C33;">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 0.6rem;">
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 2rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 700;">NBA League Office</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.2rem;">↓ <span style="font-size: 0.75rem; color: #aaa;">Data Share</span></div>
    <div style="display: flex; gap: 1rem; align-items: center;">
      <div style="background: #1a2d4d; border: 1px solid #FFB81C; border-radius: 8px; padding: 0.6rem 1.2rem; text-align: center;">
        <div style="color: #fff; font-size: 0.85rem;">Team Accounts</div>
      </div>
      <div style="color: #FFB81C;">←</div>
      <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.6rem 1.2rem; text-align: center;">
        <div style="color: #FFB81C; font-weight: 600;">Cavaliers on Snowflake</div>
      </div>
    </div>
    <div style="color: #FFB81C; font-size: 1.2rem;">↓</div>
    <div style="border: 1px solid #FFB81C; border-radius: 8px; padding: 1rem; text-align: center;">
      <div style="color: #FFB81C; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Available Data Products</div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center;">
        <div style="background: #041E42; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.4rem 0.7rem; color: #fff; font-size: 0.8rem;">Player Tracking</div>
        <div style="background: #041E42; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.4rem 0.7rem; color: #fff; font-size: 0.8rem;">League-wide Stats</div>
        <div style="background: #041E42; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.4rem 0.7rem; color: #fff; font-size: 0.8rem;">Scheduling</div>
        <div style="background: #041E42; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.4rem 0.7rem; color: #fff; font-size: 0.8rem;">Fan Engagement</div>
      </div>
    </div>
  </div>
</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **By being on Snowflake, the Cavaliers would be positioned to receive:**
    - League-provided data products (no ETL, no API integration)
    - Player tracking data shared directly to your account
    - Cross-team benchmarking data
    - League-wide fan engagement metrics
    
    This uses Snowflake's **zero-copy sharing** — always current, always governed, no pipelines to build.
    """)

with tab3:
    st.markdown("""
    ### League-Wide Analytics Capabilities
    
    Teams on Snowflake can leverage:
    
    | Analytics Area | What's Available | Powered By |
    |---------------|-----------------|------------|
    | **Player Performance** | Tracking data, shot charts, defensive metrics | Hawk-Eye + Snowflake |
    | **Game Strategy** | Play-type effectiveness, lineup analysis | Snowflake ML |
    | **Scouting** | Draft combine data, college stats, projections | Snowflake Data Sharing |
    | **Health & Load** | Minutes management, injury correlation | Snowpark + Cortex |
    | **Fan Intelligence** | Engagement patterns, content personalization | Cortex AI |
    | **Business Ops** | Revenue optimization, attendance forecasting | Snowflake ML |
    
    The league is moving toward a unified data ecosystem where teams on Snowflake 
    benefit from native data sharing and a common analytics platform.
    """)

st.markdown("---")

# Cavs-specific angle
st.markdown("## What This Means for the Cavaliers")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="use-case-card">
        <h4>Fan Engagement & Personalization</h4>
        <p>Build 360-degree fan profiles combining:</p>
        <ul style="font-size: 0.85rem;">
            <li>Ticket purchase history</li>
            <li>In-arena behavior (concessions, merch)</li>
            <li>Digital engagement (app, email, social)</li>
            <li>League-provided fan sentiment data</li>
        </ul>
        <p style="font-size: 0.85rem;">
        Use Cortex AI for personalized offers, content recommendations, 
        and churn prediction — all inside Snowflake.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="use-case-card">
        <h4>Dynamic Ticket Pricing</h4>
        <p>ML models on Snowflake for optimal pricing:</p>
        <ul style="font-size: 0.85rem;">
            <li>Opponent strength (league data)</li>
            <li>Day of week, time of year</li>
            <li>Historical demand curves</li>
            <li>Weather, local events</li>
            <li>Secondary market signals</li>
        </ul>
        <p style="font-size: 0.85rem;">
        Train and deploy pricing models entirely within Snowflake — 
        same platform as your ticketing data.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="use-case-card">
        <h4>Performance Analytics</h4>
        <p>Access the same data infrastructure the league uses:</p>
        <ul style="font-size: 0.85rem;">
            <li>Hawk-Eye optical player tracking</li>
            <li>Shot quality and defensive metrics</li>
            <li>Load management analytics</li>
            <li>Lineup optimization</li>
        </ul>
        <p style="font-size: 0.85rem;">
        Being on Snowflake means player tracking data can be shared directly 
        to your account — no export/import pipeline needed.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="use-case-card">
        <h4>Sponsor ROI & Revenue</h4>
        <p>Prove value to sponsors with data:</p>
        <ul style="font-size: 0.85rem;">
            <li>Attribution modeling (exposure → action)</li>
            <li>Clean room overlap analysis</li>
            <li>Real-time campaign performance sharing</li>
            <li>Audience segmentation for targeted activations</li>
        </ul>
        <p style="font-size: 0.85rem;">
        Share performance data securely with sponsors via 
        Snowflake's zero-copy sharing — no CSVs, always current.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Competitive advantage
st.markdown("## Competitive Advantage: Platform Alignment")

st.markdown("""
Being on Snowflake aligns the Cavaliers with:

| Entity | Relationship | Benefit |
|--------|-------------|---------|
| **NBA League Office** | Same platform | Native data sharing, zero integration cost |
| **Other NBA teams** | Shared ecosystem | Benchmarking, collaborative analytics |
| **Broadcast partners** | Data consumers | Real-time stat delivery |
| **Sponsors** | Data sharing | Secure, governed performance reporting |
| **Ticketmaster** | Marketplace | Event data available via Snowflake Marketplace |
| **Hawk-Eye (Sony)** | Player tracking | Tracking data integration via Snowflake |

**The strategic question:** As the NBA ecosystem builds on Snowflake, 
being on the same platform positions you for native integration — a competitive advantage.
""")

st.markdown("---")

# Timeline
st.markdown("## From Here to There")

st.markdown("""
```
Phase 1: Foundation
├── Move Postgres to Snowflake Postgres (pg_dump/restore — zero app changes)
├── Enable pg_lake (Postgres → Iceberg → Analytics, no CDC pipeline)
├── Connect external sources via Fivetran (Salesforce, Ticketmaster, etc.)
├── Port dbt models to Snowflake Analytics target
├── Establish governance framework (Horizon)
└── Connect Tableau to Snowflake Analytics

Phase 2: Acceleration
├── Enable NBA data products (Data Sharing)
├── Build fan 360 profile (Cortex AI)
├── Dynamic ticket pricing model (Snowpark ML)
└── Sponsor analytics dashboard (Streamlit)

Phase 3: Innovation
├── Data Clean Rooms with sponsors
├── Real-time game-day analytics (Dynamic Tables)
├── Predictive fan engagement (Cortex AI)
└── Cross-platform data exchange (Marketplace)
```
""")

st.markdown("---")

# Final callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    The NBA is building its data infrastructure on Snowflake — player tracking, advanced stats, 
    fan engagement — with the goal of delivering data products to teams via native Data Sharing.<br><br>
    By adopting Snowflake, the Cavaliers position themselves for 
    <strong>native access to the NBA's evolving data ecosystem</strong>. As the league rolls out 
    data products, teams on Snowflake receive them without integration work, APIs, or ETL.<br><br>
    This is a first-mover advantage. Teams that adopt Snowflake early are best positioned to 
    benefit from the league's data investment as it matures.
</div>
""", unsafe_allow_html=True)

# CTA
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h3 style="color: #FFB81C;">Ready to bring the Cavaliers onto the NBA's data platform?</h3>
    <p style="color: #FFFFFF; opacity: 0.8;">
    Let's build a POC that demonstrates the full pipeline — your Postgres on Snowflake Postgres, 
    data flowing via pg_lake to governed analytics, with NBA data sharing enabled. 
    Zero app changes required.
    </p>
</div>
""", unsafe_allow_html=True)
