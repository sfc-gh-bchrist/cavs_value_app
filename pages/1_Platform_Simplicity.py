import streamlit as st

st.set_page_config(page_title="Platform Simplicity | Cavs + Snowflake", page_icon="🏗️", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .comparison-box {
        background: #1a2d4d;
        border-radius: 8px;
        padding: 1.2rem;
        border: 1px solid #FFB81C33;
        height: 100%;
    }
    .pain-point {
        background: #6F263D33;
        border-left: 3px solid #6F263D;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 0 6px 6px 0;
    }
    .solution-point {
        background: #FFB81C11;
        border-left: 3px solid #FFB81C;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 0 6px 6px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🏗️ Platform Simplicity")
st.markdown("*One platform. All workloads. Zero infrastructure to manage.*")
st.markdown("---")

# The problem
st.markdown("## The Challenge Today")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="pain-point">
        <strong>Coupled Compute & Storage</strong><br>
        Running analytics on a self-managed PostgreSQL instance ties compute to storage. 
        Scaling analytics means upgrading the entire OLTP instance — even if only queries need more power.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pain-point">
        <strong>Custom Orchestration</strong><br>
        Lambdas, Python scripts, and a custom orchestrator require ongoing maintenance, 
        monitoring, and on-call support.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pain-point">
        <strong>Resource Contention</strong><br>
        Analytics queries compete with operational workloads on the same self-managed Postgres instance, 
        degrading both. Postgres is great for OLTP — but it shouldn't also be your analytics engine.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pain-point">
        <strong>Vertical Scaling Only</strong><br>
        When analytics runs on RDS, the only lever is a bigger instance. Costs scale linearly 
        while utilization stays low during off-peak hours.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pain-point">
        <strong>Tool Sprawl</strong><br>
        Separate systems for ingestion, transformation, governance, and analytics — 
        each with its own access model and maintenance burden.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pain-point">
        <strong>No Elasticity for Analytics</strong><br>
        Game-day analytics spikes (dashboards, reports, fan engagement queries) require over-provisioning 
        the RDS instance or risk degrading both analytics AND transactional workloads.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# The solution
st.markdown("## How Snowflake Simplifies Everything")

tab1, tab2, tab3, tab4 = st.tabs([
    "Separated Compute & Storage",
    "Workload Isolation",
    "Managed Infrastructure",
    "Instant Elasticity"
])

with tab1:
    st.markdown("""
    ### Independent Scaling
    
    Snowflake separates compute from storage completely:
    
    - **Storage** scales automatically as data grows — pay only for what you store
    - **Compute** scales on-demand per workload — spin up warehouses in seconds, suspend when idle
    - No instance upgrades, no migrations, no downtime
    """)
    
    st.markdown("""
<div style="padding: 1.5rem; background: #0a1929; border-radius: 12px; border: 1px solid #FFB81C33;">
  <div style="text-align: center; color: #FFB81C; font-weight: 600; margin-bottom: 1rem; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Compute Layer (Independent, Elastic)</div>
  <div style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 8px; padding: 1rem 1.5rem; text-align: center; min-width: 150px;">
      <div style="color: #FFB81C; font-weight: 600;">Analytics</div>
      <div style="color: #aaa; font-size: 0.8rem;">Medium</div>
    </div>
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 8px; padding: 1rem 1.5rem; text-align: center; min-width: 150px;">
      <div style="color: #FFB81C; font-weight: 600;">Ingestion</div>
      <div style="color: #aaa; font-size: 0.8rem;">Small</div>
    </div>
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 8px; padding: 1rem 1.5rem; text-align: center; min-width: 150px;">
      <div style="color: #FFB81C; font-weight: 600;">ML / Data Science</div>
      <div style="color: #aaa; font-size: 0.8rem;">X-Large</div>
    </div>
  </div>
  <div style="text-align: center; color: #FFB81C; font-size: 1.5rem; margin-bottom: 0.5rem;">⇅ &nbsp; ⇅ &nbsp; ⇅</div>
  <div style="text-align: center; color: #aaa; font-size: 0.75rem; margin-bottom: 1rem;">Independent connections to shared storage</div>
  <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 1.2rem; text-align: center;">
    <div style="color: #FFB81C; font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Shared Cloud Storage</div>
    <div style="color: #fff; font-size: 0.85rem; margin-top: 0.3rem;">Auto-managed · Compressed · Encrypted · Single copy of data</div>
  </div>
</div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    ### Dedicated Resources per Workload
    
    No more resource contention. Each workload gets its own compute:
    
    | Workload | Warehouse | Size | Auto-Suspend |
    |----------|-----------|------|--------------|
    | **Tableau dashboards** | `WH_ANALYTICS` | Medium | 2 min |
    | **dbt transformations** | `WH_TRANSFORM` | Large | 1 min |
    | **Data ingestion (Openflow)** | `WH_INGEST` | Small | Immediate |
    | **Data science / ML** | `WH_DATA_SCIENCE` | X-Large | 5 min |
    | **Ad-hoc queries** | `WH_ADHOC` | X-Small | 1 min |
    
    Game-day spike in ticket queries? Scale `WH_ANALYTICS` to X-Large for the evening, 
    scale back down at midnight. Other workloads are unaffected.
    """)

with tab3:
    st.markdown("""
    ### What You No Longer Manage
    
    | Component | Before (You manage) | After (Snowflake manages) |
    |-----------|--------------------|-----------------------------|
    | OLTP database | PostgreSQL RDS patches, upgrades | Snowflake Postgres (fully managed PG) |
    | Analytics engine | Also on that same RDS instance | Snowflake Analytics (elastic, separated) |
    | Postgres → Analytics | Custom Lambdas, CDC scripts | pg_lake (native Iceberg bridge) |
    | External sources | Custom Lambdas per source | Fivetran (managed connectors) |
    | Orchestration | Custom orchestrator | Snowflake Tasks / dbt Cloud |
    | Security patches | Manual | Automatic (both PG and analytics) |
    | Backups | Configured per-instance | Automatic |
    | High availability | Multi-AZ setup, failover config | Built-in HA option |
    | Scaling | Manual instance resizing | Right-size PG for OLTP; auto-scale analytics |
    | Monitoring | CloudWatch + custom alerting | Built-in + Account Usage views |
    
    **Net result:** Your team focuses on analytics and business value, not keeping the lights on.
    """)

with tab4:
    st.markdown("""
    ### Scale to Zero, Scale to Infinity
    
    Snowflake's auto-suspend and auto-resume means:
    
    - **Off-season:** Warehouses suspend automatically. You pay $0 in compute when idle.
    - **Game day:** Warehouses resume in seconds. Multi-cluster mode handles concurrency spikes.
    - **Playoff run:** Scale everything up with a single `ALTER WAREHOUSE` command. No migration needed.
    
    ```
    Compute Cost Over Time (Illustrative)
    
    Always-On Postgres:    ████████████████████████████  $$$$ (flat, 24/7)
    
    Snowflake:             █░░█░░█████░░█░░░░█████████  $$ (pay only for activity)
                           ↑      ↑                ↑
                        morning  game day        playoffs
    ```
    
    This is especially powerful for a sports organization where workloads are 
    inherently bursty — heavy on game days, light on off-days.
    """)

st.markdown("---")

# Cavs-specific callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    Your workload pattern is inherently bursty — 41 home games, playoff runs, off-season lulls, 
    draft-day spikes. With Snowflake Postgres, your transactional workloads stay on Postgres 
    (zero app changes, fully managed) while analytics scales elastically via pay-per-query compute.<br><br>
    No more self-managing RDS, custom orchestrators, or Lambda functions. 
    Your data team gets to focus on fan engagement, ticketing optimization, and performance analytics — 
    not infrastructure.
</div>
""", unsafe_allow_html=True)

# Comparison table
st.markdown("## Side-by-Side Comparison")

comparison_data = {
    "Dimension": [
        "Scaling model",
        "Compute isolation",
        "Infrastructure ops",
        "Time to scale",
        "Cost when idle",
        "HA / DR",
        "Concurrent users",
    ],
    "Current (Self-Managed RDS)": [
        "Vertical (bigger instance)",
        "None — OLTP + analytics share one instance",
        "Patches, backups, failover — all on you",
        "Minutes to hours (resize)",
        "Full instance cost 24/7",
        "Multi-AZ config required",
        "Limited by instance size",
    ],
    "Future (Snowflake Platform)": [
        "Snowflake Postgres for OLTP; elastic analytics",
        "Full — OLTP isolated from analytics",
        "Zero — both Postgres and analytics managed",
        "Seconds (analytics resume/resize)",
        "Analytics: $0 when idle; PG: right-sized",
        "Built-in HA for both PG and analytics",
        "PG handles OLTP; analytics auto-scales",
    ],
}

st.table(comparison_data)
