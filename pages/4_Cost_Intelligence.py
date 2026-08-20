import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Cost Intelligence | Cavs + Snowflake", page_icon="💰", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .cost-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
    }
    .cost-card h3 { color: #FFB81C; margin-bottom: 0.5rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 💰 Cost Intelligence & Control")
st.markdown("*Full visibility into spend. Granular controls to optimize. Pay only for what you use.*")
st.markdown("---")

# Cost model comparison
st.markdown("## Cost Model: Always-On vs. Pay-Per-Query")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="cost-card">
        <h3>Self-Managed RDS (Current)</h3>
        <p style="font-size: 2rem; color: #FFB81C; font-weight: 700;">$3,500+/mo</p>
        <p style="color: #aaa;">db.r6g.xlarge, always-on, you manage it</p>
        <p style="font-size: 0.85rem;">
        Runs 24/7 regardless of usage<br>
        OLTP + analytics on same box<br>
        You patch, backup, HA configure
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="cost-card">
        <h3>Snowflake Platform (Future)</h3>
        <p style="font-size: 2rem; color: #FFB81C; font-weight: 700;">Pay per second</p>
        <p style="color: #aaa;">Analytics: credits when queries run<br>Postgres: managed, right-sized</p>
        <p style="font-size: 0.85rem;">
        Analytics auto-suspend when idle ($0)<br>
        Postgres right-sized for OLTP only<br>
        One bill, one platform
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Interactive cost visualization
st.markdown("## Illustrative: Weekly Compute Pattern")

# Simulated weekly cost pattern
days = ["Mon", "Tue", "Wed", "Thu (Game)", "Fri", "Sat (Game)", "Sun"]
rds_cost = [120, 120, 120, 120, 120, 120, 120]  # flat
snowflake_cost = [35, 30, 40, 95, 25, 110, 15]  # bursty, matches workload

fig = go.Figure()
fig.add_trace(go.Bar(
    name="Snowflake (pay-per-use)",
    x=days, y=snowflake_cost,
    marker_color="#FFB81C"
))
fig.add_trace(go.Scatter(
    name="RDS (always-on)",
    x=days, y=rds_cost,
    mode="lines",
    line=dict(color="#6F263D", width=3, dash="dash")
))
fig.update_layout(
    plot_bgcolor="#041E42",
    paper_bgcolor="#041E42",
    font=dict(color="white"),
    legend=dict(orientation="h", y=1.12),
    yaxis_title="Daily Compute Cost ($)",
    xaxis_title="Day of Week",
    height=350,
    margin=dict(t=40)
)
st.plotly_chart(fig, use_container_width=True)

st.caption("""
*Illustrative pattern for a sports org. Game days drive spikes in ticket queries, 
fan engagement, and real-time analytics. Off-days are quiet. Snowflake matches cost to actual demand.*
""")

st.markdown("---")

# Cost control mechanisms
st.markdown("## Built-In Cost Controls")

tab1, tab2, tab3, tab4 = st.tabs([
    "Resource Monitors",
    "Budgets",
    "Per-Warehouse Tracking",
    "Auto-Suspend & Scaling"
])

with tab1:
    st.markdown("""
    ### Resource Monitors — Hard Guardrails
    
    Set credit limits at the account or warehouse level. When thresholds are hit, 
    Snowflake can notify, suspend new queries, or suspend the warehouse entirely.
    
    ```sql
    -- Set a monthly budget with escalating actions
    CREATE RESOURCE MONITOR cavs_monthly_budget
      WITH CREDIT_QUOTA = 500
      TRIGGERS
        ON 75 PERCENT DO NOTIFY          -- Alert at 75%
        ON 90 PERCENT DO NOTIFY          -- Escalate at 90%
        ON 100 PERCENT DO SUSPEND;       -- Hard stop at 100%
    
    -- Apply to specific warehouses
    ALTER WAREHOUSE WH_ANALYTICS SET RESOURCE_MONITOR = cavs_monthly_budget;
    ```
    
    **Outcomes:**
    - No surprise bills — hard limits prevent runaway spend
    - Escalating alerts give time to investigate before cutoff
    - Per-warehouse monitors isolate budget control by team/workload
    """)

with tab2:
    st.markdown("""
    ### Budgets — Proactive Spend Management
    
    Snowflake Budgets provide a higher-level view of spending against planned allocations:
    
    | Budget | Monthly Allocation | Alert Threshold | Owner |
    |--------|-------------------|-----------------|-------|
    | Analytics Team | 200 credits | 80% | Data Team Lead |
    | Data Engineering | 150 credits | 85% | Platform Team |
    | Data Science | 100 credits | 75% | ML Engineer |
    | Ad-hoc / Exploration | 50 credits | 90% | Admin |
    
    Budgets track serverless features too (Snowpipe, auto-clustering, search optimization) — 
    not just warehouse compute.
    
    **Custom budgets** can include:
    - Specific warehouses
    - Serverless features (clustering, materialized views)
    - Specific services (Cortex AI, Snowpipe)
    """)

with tab3:
    st.markdown("""
    ### Per-Warehouse Cost Attribution
    
    Every warehouse has its own credit consumption tracked independently:
    
    ```sql
    -- See exactly where credits are going
    SELECT warehouse_name, 
           SUM(credits_used) as total_credits,
           SUM(credits_used) * 3.00 as estimated_cost  -- $3/credit (Enterprise)
    FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
    WHERE start_time > DATEADD(month, -1, CURRENT_TIMESTAMP())
    GROUP BY warehouse_name
    ORDER BY total_credits DESC;
    ```
    
    **Chargeback model:** Assign warehouses to departments/teams and allocate costs directly:
    
    | Warehouse | Team | Monthly Credits | Monthly Cost |
    |-----------|------|-----------------|--------------|
    | `WH_ANALYTICS` | Business Intelligence | 120 | $360 |
    | `WH_TRANSFORM` | Data Engineering | 85 | $255 |
    | `WH_INGEST` | Platform | 40 | $120 |
    | `WH_DATA_SCIENCE` | Analytics | 60 | $180 |
    | `WH_ADHOC` | All Users | 25 | $75 |
    
    Full transparency — no shared-instance guessing about who used what.
    """)

with tab4:
    st.markdown("""
    ### Auto-Suspend & Right-Sizing
    
    **Auto-Suspend:** Warehouses automatically suspend after a configurable idle period.
    
    | Setting | Effect |
    |---------|--------|
    | `AUTO_SUSPEND = 60` | Suspend after 60 seconds idle |
    | `AUTO_RESUME = TRUE` | Resume instantly on next query |
    | `MIN_CLUSTER_COUNT = 1` | Start with 1 cluster |
    | `MAX_CLUSTER_COUNT = 3` | Scale up to 3 under load |
    
    **Right-sizing recommendations:** Snowflake provides query-level metrics to identify:
    - Oversized warehouses (low utilization)
    - Undersized warehouses (spilling to disk)
    - Candidates for multi-cluster scaling
    
    ```sql
    -- Find warehouses that could be smaller
    SELECT warehouse_name, 
           AVG(avg_running) as avg_concurrency,
           AVG(avg_queued) as avg_queue_depth
    FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_LOAD_HISTORY
    WHERE start_time > DATEADD(day, -7, CURRENT_TIMESTAMP())
    GROUP BY warehouse_name
    HAVING avg_concurrency < 1;  -- under-utilized
    ```
    """)

st.markdown("---")

# Cost optimization levers
st.markdown("## Cost Optimization Levers")

st.markdown("""
| Lever | How It Works | Typical Savings |
|-------|-------------|-----------------|
| **Auto-suspend** | Zero cost when idle | 40-70% for bursty workloads |
| **Right-sizing** | Match warehouse size to workload | 20-40% |
| **Multi-cluster** | Scale out for concurrency, not size | 15-30% |
| **Query optimization** | Clustering keys, search optimization | 20-50% on large scans |
| **Storage optimization** | Automatic compression, clustering | 60-80% vs. raw |
| **Caching** | Result cache + warehouse cache | First repeat query = free |
""")

st.markdown("---")

# Cavs callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    Sports organizations have extreme workload variability — 41 home games create spikes, 
    off-season is quiet, and playoff runs are unpredictable. A self-managed RDS instance 
    charges the same whether it's game day or July — and you're running analytics on it too.<br><br>
    With Snowflake, your Postgres handles only OLTP (right-sized, managed), while analytics 
    compute scales to zero when idle. Resource monitors ensure you never get a surprise bill. 
    Per-warehouse tracking gives your finance team clear cost attribution by department.<br><br>
    <strong>Bottom line:</strong> Keep Postgres for what it's good at, add elastic analytics alongside it, 
    and know exactly where every dollar goes — all on one bill.
</div>
""", unsafe_allow_html=True)
