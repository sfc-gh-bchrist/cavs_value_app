import streamlit as st

st.set_page_config(page_title="Fivetran & dbt | Cavs + Snowflake", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .integration-card {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.5rem;
    }
    .integration-card h4 { color: #FFB81C; }
</style>
""", unsafe_allow_html=True)

st.markdown("# ⚡ Fivetran & dbt Integration")
st.markdown("*Managed ingestion. Battle-tested transformation. Native compatibility with Snowflake.*")
st.markdown("---")

# Two pillars
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="integration-card">
        <h4>Fivetran — Managed Data Ingestion</h4>
        <p>500+ pre-built connectors. Fully managed CDC. Schema drift handled automatically.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="integration-card">
        <h4>dbt — Transformation Framework</h4>
        <p>SQL-based modeling. Version-controlled. Tested. Documented. Already in your stack.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Fivetran deep dive
st.markdown("## Fivetran + Snowflake")

tab1, tab2, tab3 = st.tabs(["Why Fivetran", "Relevant Connectors", "How It Works"])

with tab1:
    st.markdown("""
    ### Replace Custom Ingestion for External Sources
    
    Today you have Lambdas and Python scripts pulling data from external sources. 
    Fivetran replaces this with managed connectors for non-Postgres sources:
    
    > **Note:** Your Postgres operational data flows to Snowflake Analytics natively 
    via pg_lake (Iceberg) — no Fivetran connector needed for that path.
    
    | Current | With Fivetran |
    |---------|---------------|
    | Custom Lambda per source | Pre-built connector (configure, not code) |
    | You handle schema changes | Automatic schema migration |
    | You handle failures & retries | Built-in retry, alerting, SLA guarantees |
    | You monitor & maintain | Fivetran dashboard + Snowflake integration |
    | Initial load = your problem | Automated historical backfill |
    
    **Key differentiator:** Fivetran + Snowflake have a native integration — 
    Fivetran writes directly to your Snowflake account using optimized micro-batches. 
    No staging area, no intermediate storage.
    """)

with tab2:
    st.markdown("""
    ### Connectors Relevant to the Cavaliers
    
    | Source | Connector | Use Case |
    |--------|-----------|----------|
    | **PostgreSQL** | CDC (log-based) | Only needed for external Postgres instances (not Snowflake Postgres) |
    | **Salesforce** | Full + incremental | CRM data, fan profiles, sponsorships |
    | **Ticketmaster** | API-based | Ticket sales, event data |
    | **HubSpot / Marketo** | Full sync | Marketing automation, campaigns |
    | **Google Analytics** | API-based | Web/app engagement metrics |
    | **Stripe / Square** | Incremental | Payment processing, merchandise |
    | **Social (Meta, X)** | API-based | Social engagement, ad performance |
    | **Workday / ADP** | Incremental | HR and payroll |
    | **NetSuite / SAP** | CDC | Financial systems |
    | **Custom APIs** | Fivetran Functions | Any REST API via serverless function |
    
    Each connector handles:
    - Initial historical load
    - Incremental updates (CDC where supported)
    - Schema changes (new columns auto-added)
    - Deletions (soft delete tracking)
    """)

with tab3:
    st.markdown("### Architecture: Fivetran → Snowflake")

    st.markdown("""
<div style="background: #0a1929; border-radius: 12px; padding: 1.5rem; border: 1px solid #FFB81C33;">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 0.8rem;">
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center;">
      <div style="background: #1a2d4d; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 0.8rem; color: #fff; font-size: 0.8rem;">Postgres</div>
      <div style="background: #1a2d4d; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 0.8rem; color: #fff; font-size: 0.8rem;">Salesforce</div>
      <div style="background: #1a2d4d; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 0.8rem; color: #fff; font-size: 0.8rem;">Ticketmaster</div>
      <div style="background: #1a2d4d; border: 1px solid #FFB81C; border-radius: 6px; padding: 0.5rem 0.8rem; color: #fff; font-size: 0.8rem;">Google Analytics</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.3rem;">↓</div>
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 2rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600;">Fivetran (Managed)</div>
      <div style="color: #aaa; font-size: 0.8rem;">CDC / API · Schema evolution · Retry & alerting</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.3rem;">↓</div>
    <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 2rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600;">Snowflake RAW Layer</div>
      <div style="color: #fff; font-size: 0.8rem;">Landing zone · Full history preserved</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.3rem;">↓</div>
    <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 2rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600;">dbt Models</div>
      <div style="color: #fff; font-size: 0.8rem;">Cleanse → Stage → Business-ready</div>
    </div>
  </div>
</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Sync frequency:** As low as 1 minute for critical sources, 
    or 5-15 minutes for standard workloads.
    
    **Fivetran + Snowflake Partner Connect:** One-click setup from within Snowflake.
    """)

st.markdown("---")

# dbt deep dive
st.markdown("## dbt + Snowflake")

tab1, tab2, tab3, tab4 = st.tabs([
    "Migration Path",
    "dbt Cloud Integration",
    "Dynamic Tables Alternative",
    "Your dbt Project"
])

with tab1:
    st.markdown("""
    ### Your Existing dbt Models Run on Snowflake Analytics
    
    Your dbt models are analytics transformations — they belong on Snowflake's elastic 
    analytics engine, not competing for resources on your OLTP Postgres. The migration is minimal:
    
    **What stays the same:**
    - Model SQL (SELECT statements are ANSI-compatible)
    - Tests (not_null, unique, accepted_values, relationships)
    - Documentation (schema.yml files)
    - Jinja macros (most are adapter-agnostic)
    - Project structure and ref() relationships
    
    **What changes:**
    - `profiles.yml` → point to Snowflake instead of Postgres
    - A few Postgres-specific functions → Snowflake equivalents
    - Materializations → leverage Snowflake-specific options (clustering, etc.)
    
    | Postgres Function | Snowflake Equivalent |
    |-------------------|---------------------|
    | `::text` | `::VARCHAR` |
    | `ILIKE` | `ILIKE` (same!) |
    | `DATE_TRUNC('month', col)` | `DATE_TRUNC('month', col)` (same!) |
    | `generate_series()` | `GENERATOR()` / `TABLE(GENERATOR(...))` |
    | `string_agg()` | `LISTAGG()` |
    | `EXTRACT(EPOCH FROM ts)` | `DATEDIFF('second', '1970-01-01'::TIMESTAMP, ts)` |
    
    Most dbt projects migrate with < 5% of models needing changes.
    """)

with tab2:
    st.markdown("""
    ### dbt Cloud: Native Snowflake Integration
    
    If you move to dbt Cloud (or already use it), you get:
    
    | Feature | Benefit |
    |---------|---------|
    | **Snowflake Native Auth** | OAuth, key-pair — no passwords in config |
    | **IDE in browser** | Develop and test dbt models directly |
    | **Job scheduling** | Cron-based or event-triggered runs |
    | **CI/CD** | PR-based slim CI (only test changed models) |
    | **Discovery** | Auto-generated docs, lineage, freshness |
    | **Semantic Layer** | Metrics definitions consumed by BI tools |
    | **Notifications** | Slack, email, webhook on failure |
    
    **dbt Cloud + Snowflake Partner Connect:**
    - One-click setup from Snowflake UI
    - Auto-provisions service user and warehouse
    - Pre-configured connection
    
    dbt Cloud is the recommended path for teams wanting managed orchestration 
    without building their own scheduler.
    """)

with tab3:
    st.markdown("""
    ### Dynamic Tables: A Native Alternative for Real-Time
    
    For models that need to refresh faster than dbt's batch schedule, 
    Snowflake offers **Dynamic Tables** — declarative SQL that auto-refreshes:
    
    ```sql
    -- This replaces a dbt model + scheduler for real-time use cases
    CREATE DYNAMIC TABLE curated.fan_engagement_live
      TARGET_LAG = '5 minutes'      -- refresh every 5 min
      WAREHOUSE = WH_TRANSFORM
    AS
      SELECT fan_id, 
             COUNT(*) as interactions_today,
             MAX(event_time) as last_activity
      FROM staged.fan_events
      WHERE event_date = CURRENT_DATE()
      GROUP BY fan_id;
    ```
    
    **When to use each:**
    
    | Approach | Best For | Refresh |
    |----------|----------|---------|
    | **dbt models** | Batch transformations, complex logic, CI/CD | Scheduled (hourly/daily) |
    | **Dynamic Tables** | Real-time metrics, streaming aggregations | Minutes (declarative lag) |
    | **Both together** | dbt for complex models, DTs for fresh metrics | Mix of batch + real-time |
    
    You can use dbt for your core medallion architecture and Dynamic Tables 
    for specific real-time use cases (game-day dashboards, live ticket metrics).
    """)

with tab4:
    st.markdown("""
    ### Your Current dbt Project
    
    Based on your existing dbt setup, here's what the migration looks like:
    
    ```yaml
    # profiles.yml — change from Postgres to Snowflake
    cavs_analytics:
      target: prod
      outputs:
        prod:
          type: snowflake
          account: your_account
          user: "{{ env_var('SNOWFLAKE_USER') }}"
          authenticator: externalbrowser  # or key-pair
          role: TRANSFORM_ROLE
          warehouse: WH_TRANSFORM
          database: CAVS_DB
          schema: CURATED
    ```
    
    **Migration steps:**
    1. Update `profiles.yml` to target Snowflake
    2. Run `dbt debug` to verify connection
    3. Run `dbt compile` to check for syntax issues
    4. Fix any Postgres-specific SQL (typically < 5% of models)
    5. Run `dbt build` — tests validate data integrity
    6. Point Tableau/BI tools to new Snowflake objects
    
    **Your existing tests, docs, and lineage all carry over unchanged.**
    """)

st.markdown("---")

# Combined architecture
st.markdown("## Combined: Fivetran + dbt + Snowflake")

st.markdown("""
<div style="background: #0a1929; border-radius: 12px; padding: 1.5rem; border: 1px solid #FFB81C33;">
  <div style="display: flex; align-items: center; gap: 0.8rem; flex-wrap: wrap; justify-content: center;">
    <div style="text-align: center;">
      <div style="color: #FFB81C; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.4rem;">Sources</div>
      <div style="display: flex; flex-direction: column; gap: 0.3rem;">
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">Postgres</div>
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">Salesforce</div>
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">Ticketmaster</div>
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">Google / Meta</div>
      </div>
    </div>
    <div style="color: #FFB81C; font-size: 1.5rem;">→</div>
    <div style="background: #041E42; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 1rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600; font-size: 0.85rem;">Fivetran</div>
      <div style="color: #aaa; font-size: 0.7rem;">Managed CDC/API</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.5rem;">→</div>
    <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 1rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600; font-size: 0.85rem;">RAW</div>
      <div style="color: #fff; font-size: 0.7rem;">Landing zone</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.5rem;">→</div>
    <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 1rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600; font-size: 0.85rem;">dbt</div>
      <div style="color: #fff; font-size: 0.7rem;">Transform & test</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.5rem;">→</div>
    <div style="background: #6F263D; border: 2px solid #FFB81C; border-radius: 8px; padding: 0.8rem 1rem; text-align: center;">
      <div style="color: #FFB81C; font-weight: 600; font-size: 0.85rem;">CURATED</div>
      <div style="color: #fff; font-size: 0.7rem;">Business-ready</div>
    </div>
    <div style="color: #FFB81C; font-size: 1.5rem;">→</div>
    <div style="text-align: center;">
      <div style="color: #FFB81C; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.4rem;">Consumption</div>
      <div style="display: flex; flex-direction: column; gap: 0.3rem;">
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">Tableau / BI</div>
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">ML & AI</div>
        <div style="background: #1a2d4d; border: 1px solid #FFB81C66; border-radius: 4px; padding: 0.3rem 0.6rem; color: #fff; font-size: 0.75rem;">Data Sharing</div>
      </div>
    </div>
  </div>
  <div style="text-align: center; margin-top: 1rem; padding-top: 0.8rem; border-top: 1px solid #FFB81C33;">
    <span style="color: #FFB81C; font-size: 0.8rem; font-weight: 600;">Snowflake Horizon Governance</span>
    <span style="color: #aaa; font-size: 0.8rem;"> — enforced across all layers</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("**Orchestration:** dbt Cloud scheduling + Snowflake Tasks for Dynamic Tables")

st.markdown("---")

# Cavs callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    You already use dbt — that investment carries forward. Your models, tests, and documentation 
    migrate with minimal changes. Fivetran replaces your custom ingestion scripts with managed, 
    reliable connectors for every source you care about (Postgres, Salesforce, Ticketmaster, etc.).<br><br>
    The result: <strong>no custom orchestrator, no Lambda maintenance, no ingestion scripts</strong> — 
    just managed connectors feeding clean data into a transformation framework your team already knows.<br><br>
    And for real-time game-day use cases, Dynamic Tables give you sub-minute freshness 
    without changing your dbt workflow.
</div>
""", unsafe_allow_html=True)
