import streamlit as st

st.set_page_config(page_title="Governance | Cavs + Snowflake", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .cavs-callout {
        background: linear-gradient(135deg, #6F263D22 0%, #FFB81C11 100%);
        border: 1px solid #6F263D;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .gov-pillar {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        min-height: 180px;
    }
    .gov-pillar h4 { color: #FFB81C; }
    .before-after { margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🛡️ Governance")
st.markdown("*Unified, automated governance across every layer — from ingestion to consumption.*")
st.markdown("---")

# Horizon overview
st.markdown("## Snowflake Horizon: Unified Governance")
st.markdown("""
Snowflake Horizon is a built-in governance framework — not a bolt-on product. 
It provides discovery, security, privacy, compliance, and access management in a single pane, 
enforced consistently across all data and all users.
""")

# Four pillars
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="gov-pillar">
        <h4>Discovery</h4>
        <p>Find, understand, and trust your data</p>
        <p style="font-size: 0.75rem; color: #aaa;">
        Universal Search<br>
        Auto-documentation<br>
        Data lineage<br>
        Quality signals
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="gov-pillar">
        <h4>Security</h4>
        <p>Protect data at every level</p>
        <p style="font-size: 0.75rem; color: #aaa;">
        Column masking<br>
        Row access policies<br>
        Network policies<br>
        Auth policies
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="gov-pillar">
        <h4>Privacy</h4>
        <p>Sensitive data protection</p>
        <p style="font-size: 0.75rem; color: #aaa;">
        Auto-classification<br>
        Tag-based masking<br>
        Data Clean Rooms<br>
        Anonymization
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="gov-pillar">
        <h4>Compliance</h4>
        <p>Auditable access controls</p>
        <p style="font-size: 0.75rem; color: #aaa;">
        Access History<br>
        Trust Center<br>
        Audit logging<br>
        Retention policies
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Deep dives
st.markdown("## Capabilities in Detail")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Auto-Classification",
    "Tag-Based Masking",
    "Row Access Policies",
    "Lineage & Audit",
    "Trust Center"
])

with tab1:
    st.markdown("""
    ### Automatic Sensitive Data Classification
    
    Snowflake automatically scans your data and identifies sensitive categories:
    
    | Classification | Examples | Action |
    |---------------|----------|--------|
    | **PII** | Name, email, phone, address | Auto-tagged, mask by default |
    | **Identifier** | SSN, driver's license | Auto-tagged, full masking |
    | **Financial** | Credit card, bank account | Auto-tagged, tokenize |
    | **Health** | Medical record numbers | Auto-tagged, restrict access |
    
    **How it works:**
    1. Enable classification at the schema or database level
    2. Snowflake analyzes column names, data patterns, and metadata
    3. Semantic tags are applied (e.g., `SNOWFLAKE.CORE.SEMANTIC_CATEGORY = 'EMAIL'`)
    4. You define masking policies per tag — enforced everywhere, always
    
    ```sql
    -- Enable classification, then review results:
    SELECT * FROM TABLE(
      INFORMATION_SCHEMA.TAG_REFERENCES('CAVS_DB.TICKETING.CUSTOMERS', 'TABLE')
    );
    -- Shows: EMAIL → PII, PHONE → PII, CREDIT_CARD → FINANCIAL
    
    -- One masking policy per tag — covers all current and future columns
    ALTER TAG SNOWFLAKE.CORE.SEMANTIC_CATEGORY SET MASKING POLICY pii_mask;
    ```
    
    **Key benefit:** Once enabled, new tables with PII are automatically protected without manual intervention.
    """)

with tab2:
    st.markdown("""
    ### Tag-Based Dynamic Masking
    
    Instead of writing one masking policy per column (fragile, unscalable), 
    Snowflake lets you mask based on tags:
    
    ```
    ┌─────────────────────────────────────────────────────┐
    │  Tag: PII                                           │
    │  └── Masking Policy: pii_mask (one policy, conditional)│
    │      ├── IF role = ADMIN → show full value             │
    │      ├── IF role = ANALYST → show last 4 chars         │
    │      └── ELSE → fully mask                            │
    ├─────────────────────────────────────────────────────┤
    │  Applied to ALL columns tagged PII — automatically  │
    │  Covers: email, phone, address, name, etc.          │
    │  Future columns tagged PII → immediately protected  │
    └─────────────────────────────────────────────────────┘
    ```
    
    **What different roles see:**
    
    | Column | ADMIN | ANALYST | MARKETING |
    |--------|-------|---------|-----------|
    | `email` | john@example.com | j***@example.com | ****@*******.*** |
    | `phone` | 216-555-0123 | ***-***-0123 | ************ |
    | `credit_card` | 4111-1111-1111-1234 | ****-****-****-1234 | **************** |
    
    Same query, same table — different results based on role. Zero application changes required.
    """)

with tab3:
    st.markdown("""
    ### Row Access Policies
    
    Control which rows each user/role can see — enforced at the platform level:
    
    **Example: Regional ticket managers only see their territory**
    
    ```sql
    CREATE ROW ACCESS POLICY territory_policy AS (territory VARCHAR)
    RETURNS BOOLEAN ->
      CURRENT_ROLE() = 'ADMIN'
      OR territory IN (
        SELECT territory FROM access_control.territory_mapping
        WHERE role_name = CURRENT_ROLE()
      );
    
    -- Apply once, enforced everywhere
    ALTER TABLE ticketing.sales ADD ROW ACCESS POLICY territory_policy ON (territory);
    ```
    
    **Use cases for the Cavaliers:**
    
    | Policy | Who sees what |
    |--------|--------------|
    | Territory-based | Regional reps see only their territory's sales |
    | Sponsor-based | Each sponsor sees only their campaign data |
    | Department-based | Finance sees revenue, Marketing sees engagement |
    | Time-based | Historical data restricted after retention period |
    
    Policies follow the data — even through views, shares, and Streamlit apps.
    """)

with tab4:
    st.markdown("""
    ### Column-Level Lineage & Access History
    
    **Lineage** — trace data from source to dashboard:
    
    ```
    [Snowflake Postgres: customers]
         ↓ (pg_lake → Iceberg)
    [RAW.ticketing.customers_raw]
         ↓ (Dynamic Table)
    [STAGED.ticketing.customers_clean]
         ↓ (dbt model)
    [CURATED.analytics.fan_360]
         ↓ (Tableau dashboard)
    [Season Ticket Renewal Report]
    ```
    
    - Track how PII flows through your pipeline
    - Impact analysis: "If I change this column, what breaks?"
    - Regulatory compliance: prove data provenance
    
    **Access History** — complete audit of who accessed what:
    
    ```sql
    -- Who accessed customer data in the last 30 days?
    SELECT user_name, query_start_time, 
           f.value:"objectName"::STRING AS object_accessed
    FROM SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY,
         LATERAL FLATTEN(input => direct_objects_accessed) f
    WHERE f.value:"objectName"::STRING ILIKE '%customers%'
      AND query_start_time > DATEADD(day, -30, CURRENT_TIMESTAMP());
    ```
    
    Every query, every user, every column — logged and queryable.
    """)

with tab5:
    st.markdown("""
    ### Trust Center — Security Posture at a Glance
    
    A single dashboard showing your security posture:
    
    - **CIS Benchmarks** — automated checks against industry standards
    - **Security Essentials** — MFA enforcement, network policies, password policies
    - **Threat Intelligence** — anomalous access patterns, failed logins, privilege escalation
    - **AI Security** — guardrails for Cortex AI usage
    
    Trust Center continuously scans your account and surfaces findings with severity levels 
    and remediation steps. Think of it as a built-in security auditor.
    
    **Example findings:**
    - "3 users without MFA enabled" → one-click enforcement
    - "Network policy allows 0.0.0.0/0" → suggested restriction
    - "Unused admin role not rotated in 90 days" → recommended action
    """)

st.markdown("---")

# Before/After comparison
st.markdown("## Before & After: Governance Transformation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Before (Self-Managed RDS)")
    st.markdown("""
    - Manual, best-effort classification
    - Column-level GRANT/REVOKE in Postgres (doesn't extend to analytics)
    - No dynamic masking without application logic
    - No lineage beyond what dbt provides
    - Audit = pg_stat_statements (limited)
    - Compliance evidence gathered manually
    - No centralized governance across OLTP + analytics
    """)

with col2:
    st.markdown("### After (Snowflake Horizon)")
    st.markdown("""
    - Automatic classification — PII detected instantly
    - Tag-based masking — one policy covers all columns
    - Dynamic masking per role — no app changes
    - Full column-level lineage, source to dashboard
    - Complete access history — every query logged
    - Trust Center — continuous compliance monitoring
    - Single governance pane across all data
    """)

st.markdown("---")

# Cavs callout
st.markdown("""
<div class="cavs-callout">
    <strong style="color: #FFB81C;">Why This Matters for the Cavaliers</strong><br><br>
    You manage sensitive fan data (PII, payment info, loyalty profiles), sponsor relationships, 
    and league-mandated reporting. Today, governance is scattered across Postgres GRANTs, 
    application-level checks, and manual processes.<br><br>
    With Snowflake Horizon, governance is <strong>automatic</strong> (classification), 
    <strong>centralized</strong> (one policy engine), <strong>dynamic</strong> (role-based masking), 
    and <strong>auditable</strong> (complete access history). When a sponsor asks "who accessed our data?" 
    or an auditor asks "how is PII protected?" — the answer is one query away.
</div>
""", unsafe_allow_html=True)
