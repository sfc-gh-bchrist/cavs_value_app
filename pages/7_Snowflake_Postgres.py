import streamlit as st

st.set_page_config(page_title="Snowflake Postgres | Cavs + Snowflake", page_icon="🐘", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .pg-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    .pg-card h4 { color: #FFB81C; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🐘 Snowflake Postgres")
st.markdown("*Keep Postgres for what it does best — and unify it with Snowflake's analytics platform.*")
st.markdown("---")

# What it is
st.markdown("## What is Snowflake Postgres?")

st.markdown("""
Snowflake Postgres lets you **run fully managed PostgreSQL instances directly within Snowflake**. 
You get a real Postgres database — compatible with all your existing tools, ORMs, and applications — 
but managed by Snowflake with zero operational overhead.

This is not a migration-or-nothing proposition. The Cavaliers can:
- **Keep Postgres for operational/transactional workloads** (where it excels)
- **Use Snowflake for analytics, data sharing, and governance** (where it excels)
- **Connect them natively** within a single platform
""")

st.markdown("---")

# Architecture diagram
st.markdown("## Best of Both Worlds Architecture")

st.markdown("""
<div style="background: #0a1929; border-radius: 12px; padding: 1.5rem; border: 1px solid #FFB81C33;">
  <div style="display: flex; align-items: stretch; gap: 1rem; flex-wrap: wrap; justify-content: center;">
    <div style="flex: 1; min-width: 220px; background: #041E42; border: 2px solid #336791; border-radius: 10px; padding: 1.2rem; text-align: center;">
      <div style="color: #336791; font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">Snowflake Postgres</div>
      <div style="color: #FFB81C; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Transactional Workloads</div>
      <div style="display: flex; flex-direction: column; gap: 0.3rem;">
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Ticketing system</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Fan app backend</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">CRM operations</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Point-of-sale</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Low-latency reads/writes</div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 0 0.5rem;">
      <div style="color: #FFB81C; font-size: 1.5rem;">⇄</div>
      <div style="color: #aaa; font-size: 0.7rem; text-align: center; max-width: 80px;">Native<br/>integration</div>
    </div>
    <div style="flex: 1; min-width: 220px; background: #041E42; border: 2px solid #FFB81C; border-radius: 10px; padding: 1.2rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">Snowflake Analytics</div>
      <div style="color: #FFB81C; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Analytical Workloads</div>
      <div style="display: flex; flex-direction: column; gap: 0.3rem;">
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Dashboards & BI</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">dbt transformations</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Data sharing (NBA, sponsors)</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">ML & Cortex AI</div>
        <div style="background: #1a2d4d; border-radius: 4px; padding: 0.3rem; color: #fff; font-size: 0.8rem;">Governance (Horizon)</div>
      </div>
    </div>
  </div>
  <div style="text-align: center; margin-top: 1rem; padding-top: 0.8rem; border-top: 1px solid #FFB81C33;">
    <span style="color: #FFB81C; font-size: 0.8rem; font-weight: 600;">Single Platform</span>
    <span style="color: #aaa; font-size: 0.8rem;"> — unified security, billing, and management</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Key capabilities
st.markdown("## Key Capabilities")

tab1, tab2, tab3, tab4 = st.tabs([
    "Fully Managed",
    "100% Compatible",
    "pg_lake (Iceberg)",
    "Unified Platform"
])

with tab1:
    st.markdown("""
    ### Zero-Ops Postgres
    
    Snowflake manages the entire Postgres lifecycle:
    
    | What Snowflake Manages | What You Don't Do Anymore |
    |----------------------|---------------------------|
    | Provisioning | No instance setup or config |
    | Patching & upgrades | No maintenance windows to schedule |
    | High availability | Built-in HA option, automatic failover |
    | Backups | Automatic, no cron jobs |
    | Connection pooling | PgBouncer built-in for high concurrency |
    | Security | Private network isolation, TLS enforced |
    | Monitoring | Integrated with Snowflake account |
    
    ```sql
    -- Create a managed Postgres instance in Snowflake
    CREATE POSTGRES INSTANCE cavs_operational
      COMPUTE_POOL = 'STANDARD_2'
      STORAGE_SIZE_GB = 100
      POSTGRES_VERSION = '17'
      ENABLE_HA = TRUE;
    
    -- That's it. Connect with any Postgres client.
    ```
    
    Instance sizes scale from small development (2 vCPU / 8 GB) to 
    large production workloads — resize with a single command.
    """)

with tab2:
    st.markdown("""
    ### Full PostgreSQL Compatibility
    
    Snowflake Postgres runs **real PostgreSQL** (versions 16, 17, 18) — not a Postgres-compatible engine:
    
    - **All your existing code works** — ORMs, migrations, application queries
    - **All your tools work** — psql, pgAdmin, DBeaver, any Postgres client
    - **Extensions supported** — the Postgres extension ecosystem you rely on
    - **Standard wire protocol** — connect with any language driver (Python, Node, Go, Java, etc.)
    
    **Migration story:** If you're already on Postgres, moving to Snowflake Postgres is a 
    `pg_dump` / `pg_restore` — or logical replication for zero-downtime migration. 
    No application code changes required.
    
    | Feature | Standard Postgres | Snowflake Postgres |
    |---------|------------------|-------------------|
    | SQL compatibility | Full | Full (same engine) |
    | Extensions | Yes | Yes |
    | JSONB, arrays, CTEs | Yes | Yes |
    | Wire protocol | Standard | Standard |
    | Managed by you | Yes (patches, HA, backups) | No — Snowflake manages |
    | Connected to analytics | Manual ETL | Native integration |
    """)

with tab3:
    st.markdown("""
    ### pg_lake: Postgres to Snowflake via Iceberg
    
    **pg_lake** lets your Postgres instance write data as Apache Iceberg tables 
    that Snowflake can query directly — no ETL pipeline needed:
    
    ```
    Snowflake Postgres Instance
         │
         ├── Operational tables (standard Postgres)
         │       ↕ Your applications read/write normally
         │
         └── pg_lake tables (Iceberg format)
                 │
                 ├── Written to S3 as Iceberg
                 │
                 └── Queryable from Snowflake Analytics
                         (via catalog integration)
    ```
    
    **Use case for the Cavaliers:**
    
    1. Your ticketing app writes transactions to Postgres (low-latency, ACID)
    2. pg_lake exports that data as Iceberg tables to S3
    3. Snowflake reads those Iceberg tables directly for analytics
    4. No ETL pipeline, no Lambdas, no custom scripts
    
    This replaces the current pattern of custom CDC scripts moving data 
    from Postgres to your analytics layer.
    """)

with tab4:
    st.markdown("""
    ### One Platform, Unified Management
    
    With Snowflake Postgres, your operational and analytical databases live under one roof:
    
    | Dimension | Separate (Today) | Unified (Snowflake) |
    |-----------|-----------------|---------------------|
    | **Billing** | RDS bill + analytics bill | Single Snowflake bill |
    | **Security** | Separate IAM, networking | Single security model |
    | **Access control** | Postgres roles + Snowflake roles | Unified RBAC |
    | **Networking** | Separate VPCs, peering | Single network policy |
    | **Monitoring** | CloudWatch + Snowflake UI | Single pane of glass |
    | **Governance** | Manual across systems | Horizon covers both |
    
    **Your DBA manages Postgres the way they always have** (psql, extensions, 
    standard PG admin) — but it's billed, secured, and monitored alongside 
    your analytics workloads.
    """)

st.markdown("---")

# When to use what
st.markdown("## When to Use Postgres vs. Snowflake Analytics")

st.markdown("""
| Workload | Best Fit | Why |
|----------|----------|-----|
| Ticket purchases (real-time OLTP) | **Snowflake Postgres** | Low-latency writes, ACID transactions |
| Fan app backend | **Snowflake Postgres** | High concurrency, row-level operations |
| Point-of-sale system | **Snowflake Postgres** | Sub-millisecond reads |
| Revenue dashboards | **Snowflake Analytics** | Complex aggregations, large scans |
| Season ticket renewal predictions | **Snowflake Analytics** | ML models, large datasets |
| Sponsor reporting & data sharing | **Snowflake Analytics** | Zero-copy sharing, governance |
| Fan 360 profile | **Snowflake Analytics** | Multi-source joins, Cortex AI |
| Historical trend analysis | **Snowflake Analytics** | Time Travel, unlimited scale |
""")

st.markdown("---")

# Migration approach
st.markdown("## Migration Approach: Gradual, Not All-or-Nothing")

st.markdown("""
The Cavaliers don't need to choose between Postgres and Snowflake. 
The recommended path:

**Phase 1:** Move your existing Postgres to Snowflake Postgres (lift-and-shift, zero app changes)

**Phase 2:** Enable pg_lake to flow operational data into Snowflake Analytics (replaces custom CDC)

**Phase 3:** Build analytics, governance, and sharing on top of the unified platform

This preserves your team's Postgres expertise while adding Snowflake's 
analytics, sharing, and governance capabilities alongside it.
""")

st.markdown("---")

# Cavs callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    Your team knows Postgres. Your applications run on Postgres. That doesn't have to change.<br><br>
    Snowflake Postgres means you can <strong>keep Postgres for what it's good at</strong> (transactional 
    workloads, low-latency operations, application backends) while gaining everything Snowflake offers 
    for analytics, governance, and data sharing — <strong>all on one platform, one bill, one security model</strong>.<br><br>
    No more managing RDS instances, patching, HA configuration, or building custom CDC pipelines 
    to move data between your operational and analytical systems. It's all Snowflake.
</div>
""", unsafe_allow_html=True)
