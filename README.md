# Cavs + Snowflake Value Proposition App

A Streamlit app showcasing Snowflake's value for the Cleveland Cavaliers.

## Deploy to Streamlit Community Cloud

1. Push this `cavs_value_app/` directory to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy with these settings:
   - **Repository:** your-github-user/repo-name
   - **Branch:** main
   - **Main file path:** Home.py
5. Done — public URL, you control updates via git push

## Local Development

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Structure

```
cavs_value_app/
├── .streamlit/config.toml   # Cavs theme (wine, gold, navy)
├── Home.py                  # Landing page (shows as "Home" in sidebar)
├── pages/
│   ├── 1_Platform_Simplicity.py
│   ├── 2_Data_Sharing.py
│   ├── 3_Governance.py
│   ├── 4_Cost_Intelligence.py
│   ├── 5_Fivetran_and_dbt.py
│   └── 6_NBA_Partnership.py
├── assets/
│   └── cavs_small.png
└── requirements.txt
```
