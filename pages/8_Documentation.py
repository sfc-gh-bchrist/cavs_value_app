import streamlit as st

st.set_page_config(page_title="Learn More | Cavs + Snowflake", page_icon="📚", layout="wide")

st.markdown("""
<style>
    .doc-section {
        background: #1a2d4d;
        border: 1px solid #FFB81C33;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .doc-section h4 { color: #FFB81C; margin-bottom: 0.8rem; }
    .doc-link {
        display: block;
        color: #FFB81C;
        text-decoration: none;
        padding: 0.3rem 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# 📚 Snowflake Documentation")
st.markdown("*Dive deeper into the capabilities covered in this presentation.*")
st.markdown("---")

st.markdown("## Platform & Compute")
st.markdown("""
| Topic | Documentation Link |
|-------|-------------------|
| Virtual Warehouses Overview | [docs.snowflake.com/en/user-guide/warehouses-overview](https://docs.snowflake.com/en/user-guide/warehouses-overview) |
| Multi-Cluster Warehouses | [docs.snowflake.com/en/user-guide/warehouses-multicluster](https://docs.snowflake.com/en/user-guide/warehouses-multicluster) |
| Warehouse Sizing & Best Practices | [docs.snowflake.com/en/user-guide/warehouses-considerations](https://docs.snowflake.com/en/user-guide/warehouses-considerations) |
| Snowflake Postgres | [docs.snowflake.com/en/user-guide/snowflake-postgres/about](https://docs.snowflake.com/en/user-guide/snowflake-postgres/about) |
| Snowflake Postgres Instance Management | [docs.snowflake.com/en/user-guide/snowflake-postgres/managing-instances](https://docs.snowflake.com/en/user-guide/snowflake-postgres/managing-instances) |
""")

st.markdown("## Data Sharing & Collaboration")
st.markdown("""
| Topic | Documentation Link |
|-------|-------------------|
| Secure Data Sharing Overview | [docs.snowflake.com/en/user-guide/data-sharing-intro](https://docs.snowflake.com/en/user-guide/data-sharing-intro) |
| Secure Views for Sharing | [docs.snowflake.com/en/user-guide/data-sharing-secure-views](https://docs.snowflake.com/en/user-guide/data-sharing-secure-views) |
| Data Clean Rooms | [docs.snowflake.com/en/user-guide/cleanrooms/overview](https://docs.snowflake.com/en/user-guide/cleanrooms/overview) |
| Snowflake Marketplace | [docs.snowflake.com/en/user-guide/data-marketplace](https://docs.snowflake.com/en/user-guide/data-marketplace) |
| Reader Accounts | [docs.snowflake.com/en/user-guide/data-sharing-reader-create](https://docs.snowflake.com/en/user-guide/data-sharing-reader-create) |
""")

st.markdown("## Governance (Snowflake Horizon)")
st.markdown("""
| Topic | Documentation Link |
|-------|-------------------|
| Sensitive Data Classification | [docs.snowflake.com/en/user-guide/classify-intro](https://docs.snowflake.com/en/user-guide/classify-intro) |
| Dynamic Data Masking | [docs.snowflake.com/en/user-guide/security-column-ddm-use](https://docs.snowflake.com/en/user-guide/security-column-ddm-use) |
| Tag-Based Masking Policies | [docs.snowflake.com/en/user-guide/tag-based-masking-policies](https://docs.snowflake.com/en/user-guide/tag-based-masking-policies) |
| Row Access Policies | [docs.snowflake.com/en/user-guide/security-row-intro](https://docs.snowflake.com/en/user-guide/security-row-intro) |
| Access History | [docs.snowflake.com/en/user-guide/access-history](https://docs.snowflake.com/en/user-guide/access-history) |
| Object Tagging | [docs.snowflake.com/en/user-guide/object-tagging](https://docs.snowflake.com/en/user-guide/object-tagging) |
| Trust Center | [docs.snowflake.com/en/user-guide/trust-center/overview](https://docs.snowflake.com/en/user-guide/trust-center/overview) |
""")

st.markdown("## Cost Management")
st.markdown("""
| Topic | Documentation Link |
|-------|-------------------|
| Controlling Cost | [docs.snowflake.com/en/user-guide/cost-controlling](https://docs.snowflake.com/en/user-guide/cost-controlling) |
| Resource Monitors | [docs.snowflake.com/en/user-guide/resource-monitors](https://docs.snowflake.com/en/user-guide/resource-monitors) |
| Budgets (Custom) | [docs.snowflake.com/en/user-guide/budgets/custom-budget](https://docs.snowflake.com/en/user-guide/budgets/custom-budget) |
| Monitoring Budgets | [docs.snowflake.com/en/user-guide/budgets/monitor](https://docs.snowflake.com/en/user-guide/budgets/monitor) |
| Cost Access Control | [docs.snowflake.com/en/user-guide/cost-access-control](https://docs.snowflake.com/en/user-guide/cost-access-control) |
""")

st.markdown("## Data Engineering (dbt & Dynamic Tables)")
st.markdown("""
| Topic | Documentation Link |
|-------|-------------------|
| Dynamic Tables Overview | [docs.snowflake.com/en/user-guide/dynamic-tables/overview](https://docs.snowflake.com/en/user-guide/dynamic-tables/overview) |
| Dynamic Tables Target Lag | [docs.snowflake.com/en/user-guide/dynamic-tables/target-lag](https://docs.snowflake.com/en/user-guide/dynamic-tables/target-lag) |
| Dynamic Tables Best Practices | [docs.snowflake.com/en/user-guide/dynamic-tables/best-practices](https://docs.snowflake.com/en/user-guide/dynamic-tables/best-practices) |
| dbt Projects on Snowflake (Native) | [docs.snowflake.com/en/user-guide/data-engineering/dbt-projects-on-snowflake](https://docs.snowflake.com/en/user-guide/data-engineering/dbt-projects-on-snowflake) |
| Snowflake Tasks (Orchestration) | [docs.snowflake.com/en/user-guide/tasks-intro](https://docs.snowflake.com/en/user-guide/tasks-intro) |
| Fivetran + Snowflake | [docs.snowflake.com/en/user-guide/ecosystem-fivetran](https://docs.snowflake.com/en/user-guide/ecosystem-fivetran) |
""")

st.markdown("## AI & Machine Learning")
st.markdown("""
| Topic | Documentation Link |
|-------|-------------------|
| Cortex AI Functions | [docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions) |
| Snowpark ML | [docs.snowflake.com/en/developer-guide/snowpark-ml/overview](https://docs.snowflake.com/en/developer-guide/snowpark-ml/overview) |
| Streamlit in Snowflake | [docs.snowflake.com/en/developer-guide/streamlit/about-streamlit](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit) |
""")

st.markdown("---")

st.markdown("""
<div style="text-align: center; opacity: 0.6; font-size: 0.8rem;">
All links point to official Snowflake documentation at docs.snowflake.com
</div>
""", unsafe_allow_html=True)
