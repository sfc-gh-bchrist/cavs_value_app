import streamlit as st

st.set_page_config(page_title="Data Sharing | Cavs + Snowflake", page_icon="🔗", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .share-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    .share-card h4 { color: #FFB81C; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🔗 Data Sharing")
st.markdown("*Share live data instantly — no ETL, no copies, no pipelines to maintain.*")
st.markdown("---")

# Core concept
st.markdown("## Zero-Copy Data Sharing")

st.markdown("""
Snowflake's data sharing model is fundamentally different from traditional approaches:

- **No data movement** — consumers query your data in-place
- **No copies** — single source of truth, always current
- **No ETL pipelines** — eliminate the integration tax
- **Governed** — you control exactly who sees what, with full audit trail
- **Real-time** — consumers always see the latest data, not yesterday's export
""")

st.markdown("---")

# Traditional vs Snowflake
st.markdown("## Traditional Sharing vs. Snowflake")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Traditional: Export & Send")
    st.markdown("""
<div style="background: #0a1929; border-radius: 10px; padding: 1.2rem; border: 1px solid #6F263D;">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 0.4rem;">
    <div style="background: #6F263D; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">Source DB</div>
    <div style="color: #FFB81C;">↓ <span style="font-size: 0.7rem; color:#aaa;">extract</span></div>
    <div style="background: #6F263D; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">ETL Pipeline</div>
    <div style="color: #FFB81C;">↓ <span style="font-size: 0.7rem; color:#aaa;">transform</span></div>
    <div style="background: #6F263D; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">File / API</div>
    <div style="color: #FFB81C;">↓ <span style="font-size: 0.7rem; color:#aaa;">send</span></div>
    <div style="background: #6F263D; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">Partner's System</div>
    <div style="color: #FFB81C;">↓ <span style="font-size: 0.7rem; color:#aaa;">load</span></div>
    <div style="background: #6F263D; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">Partner's DB</div>
  </div>
</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Latency: **Hours to days**
    - Cost: Pipeline infra + storage x N partners
    - Governance: Lost once data leaves
    - Issues: Schema drift, stale data, versioning
    """)

with col2:
    st.markdown("#### Snowflake: Zero-Copy Share")
    st.markdown("""
<div style="background: #0a1929; border-radius: 10px; padding: 1.2rem; border: 1px solid #FFB81C;">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 0.4rem;">
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 6px; padding: 0.6rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">Your Snowflake Account</div>
    <div style="color: #FFB81C; font-size: 1.2rem;">↓</div>
    <div style="background: #FFB81C; border-radius: 6px; padding: 0.6rem 1rem; color: #041E42; font-weight: 600; font-size: 0.85rem; width: 80%; text-align: center;">CREATE SHARE (instant)</div>
    <div style="color: #FFB81C; font-size: 1.2rem;">↓</div>
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 6px; padding: 0.6rem 1rem; color: #fff; font-size: 0.85rem; width: 80%; text-align: center;">Partner's Snowflake Account</div>
  </div>
  <div style="text-align: center; margin-top: 0.8rem; color: #aaa; font-size: 0.75rem;">Live, governed pointer — no data moves</div>
</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Latency: **Real-time (seconds)**
    - Cost: $0 for sharing (consumer pays compute)
    - Governance: Full control, revocable, auditable
    - Always current — no sync, no drift
    """)

st.markdown("---")

# Use cases for the Cavs
st.markdown("## Use Cases for the Cavaliers")

tab1, tab2, tab3, tab4 = st.tabs([
    "League Reporting",
    "Sponsor Analytics",
    "Partner Data Exchange",
    "Data Clean Rooms"
])

with tab1:
    st.markdown("""
    ### NBA League Office Reporting
    
    The NBA requires standardized reporting from all teams. With Snowflake:
    
    - **Share attendance, revenue, and operational data** directly with the league
    - **Always current** — no manual CSV exports or API integrations
    - **Schema enforcement** — the league defines the structure, you populate it
    - **Audit trail** — complete history of when data was accessed
    
    Since the NBA is already on Snowflake (Official Cloud Data Platform), sharing is native 
    and instant — the same account-to-account sharing mechanism.
    
    ```sql
    -- Create a share for NBA league reporting
    CREATE SHARE nba_league_reporting;
    GRANT USAGE ON DATABASE cavs_reporting TO SHARE nba_league_reporting;
    GRANT USAGE ON SCHEMA cavs_reporting.league TO SHARE nba_league_reporting;
    GRANT SELECT ON cavs_reporting.league.attendance TO SHARE nba_league_reporting;
    GRANT SELECT ON cavs_reporting.league.revenue_summary TO SHARE nba_league_reporting;
    
    -- The NBA sees real-time data — no export needed
    ```
    """)

with tab2:
    st.markdown("""
    ### Sponsor & Partner Analytics
    
    Share campaign performance data with sponsors without exposing raw customer data:
    
    - **Aggregated views** — sponsors see performance metrics, not PII
    - **Row-level security** — each sponsor only sees their own campaigns
    - **Real-time** — sponsors can self-serve on current data
    - **Revocable** — remove access instantly when a partnership ends
    
    **Example:** Share anonymized ticket purchase patterns with a jersey sponsor to optimize 
    in-arena merchandise placement — without ever moving data outside Snowflake.
    
    ```sql
    -- Secure view: each consuming account sees only their campaigns
    CREATE OR REPLACE SECURE VIEW sharing.sponsor_campaign_performance AS
    SELECT campaign_id, impressions, conversions, revenue_attributed
    FROM marketing.campaigns c
    JOIN sharing.account_sponsor_map m
      ON c.sponsor_id = m.sponsor_id
    WHERE m.snowflake_account = CURRENT_ACCOUNT();  -- filters by consumer's account
    ```
    """)

with tab3:
    st.markdown("""
    ### Partner Data Exchange
    
    Bring external data IN and share your data OUT — all governed:
    
    | Direction | Example | Mechanism |
    |-----------|---------|-----------|
    | **Inbound** | Ticketmaster event data | Marketplace listing |
    | **Inbound** | Weather data for demand modeling | Marketplace listing |
    | **Inbound** | Social media sentiment | Fivetran + Marketplace |
    | **Outbound** | Fan engagement metrics to sponsors | Direct share |
    | **Outbound** | Compliance data to the league | Direct share |
    | **Bidirectional** | Joint analytics with arena vendors | Data exchange |
    
    The **Snowflake Marketplace** has 2,000+ live data sets from providers like 
    Ticketmaster, Weather Source, and social analytics firms — accessible with a single click.
    """)

with tab4:
    st.markdown("""
    ### Data Clean Rooms
    
    For sensitive collaborations where neither party should see the other's raw data:
    
    - **Overlap analysis** — "How many of our season ticket holders are also customers of Sponsor X?"
    - **Privacy-safe** — neither party exposes individual records
    - **No data movement** — runs inside Snowflake's secure computation environment
    - **Use cases:**
      - Sponsor ROI measurement
      - Joint audience segmentation
      - Cross-sell optimization with retail partners
    """)

    st.markdown("""
<div style="background: #0a1929; border-radius: 10px; padding: 1.5rem; border: 1px solid #FFB81C33;">
  <div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 1rem; flex-wrap: wrap;">
    <div style="background: #6F263D; border: 1px solid #FFB81C; border-radius: 8px; padding: 1rem; text-align: center; flex: 1; min-width: 180px;">
      <div style="color: #FFB81C; font-weight: 600;">Cavaliers Data</div>
      <div style="color: #aaa; font-size: 0.8rem;">Fan demographics, ticket history</div>
    </div>
    <div style="background: #041E42; border: 1px solid #FFB81C; border-radius: 8px; padding: 1rem; text-align: center; flex: 1; min-width: 180px;">
      <div style="color: #FFB81C; font-weight: 600;">Sponsor Data</div>
      <div style="color: #aaa; font-size: 0.8rem;">Customer purchase history</div>
    </div>
  </div>
  <div style="text-align: center; color: #FFB81C; font-size: 1.5rem; margin: 0.5rem 0;">↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↓</div>
  <div style="background: #FFB81C; border-radius: 8px; padding: 1rem; text-align: center; margin: 0.5rem auto; max-width: 300px;">
    <div style="color: #041E42; font-weight: 700;">Data Clean Room</div>
    <div style="color: #041E42; font-size: 0.8rem;">Privacy-safe computation</div>
  </div>
  <div style="text-align: center; color: #FFB81C; font-size: 1.5rem; margin: 0.5rem 0;">↓</div>
  <div style="background: #1a2d4d; border: 2px solid #FFB81C; border-radius: 8px; padding: 1rem; text-align: center; margin: 0 auto; max-width: 250px;">
    <div style="color: #FFB81C; font-weight: 600;">Result: 12,400 matched fans</div>
  </div>
  <div style="text-align: center; color: #aaa; font-size: 0.8rem; margin-top: 0.8rem; font-style: italic;">Neither party sees the other's raw data.</div>
</div>
    """, unsafe_allow_html=True)
    
st.markdown("---")

# Key differentiators
st.markdown("## Sharing Capabilities at a Glance")

capabilities = {
    "Capability": [
        "Live data (no copies)",
        "Cross-cloud sharing",
        "Row-level access control",
        "Revocable access",
        "Marketplace (2,000+ datasets)",
        "Data Clean Rooms",
        "Reader accounts (non-Snowflake consumers)",
        "Full audit trail",
    ],
    "Available": ["Yes"] * 8,
    "Impact": [
        "Always current, zero maintenance",
        "Share with partners on any cloud",
        "Each consumer sees only their data",
        "Remove access in seconds",
        "Weather, social, economic data — one click",
        "Privacy-safe collaboration",
        "Share with anyone, even non-Snowflake users",
        "Complete visibility into access patterns",
    ],
}

st.table(capabilities)

st.markdown("---")

# Cavs callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    Sports organizations are inherently collaborative — you share data with the league, sponsors, 
    ticketing partners, arena vendors, and media. Today each of these is a custom integration. 
    With Snowflake, every one becomes a governed, real-time data share with zero pipelines to maintain.<br><br>
    And since the NBA is already on Snowflake, league reporting becomes as simple as granting access 
    to a share — not building and maintaining export pipelines.
</div>
""", unsafe_allow_html=True)
