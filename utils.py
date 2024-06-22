import streamlit as st
import pandas as pd
import numpy as np
import requests
import re
from datetime import datetime, timezone
import psycopg2 as pg


ttl_short = 900 # 15 minutes
ttl_long = 36000 # 10 hours


def run_query(query):
    """Run query and return results"""
    try:
        conn = pg.connect(host=st.secrets["indexer"]["host"], 
                           port=st.secrets["indexer"]["port"], 
                           dbname=st.secrets["indexer"]["dbname"], 
                           user=st.secrets["indexer"]["user"], 
                           password=st.secrets["indexer"]["password"])
        cur = conn.cursor()
        cur.execute(query)
        col_names = [desc[0] for desc in cur.description]
        results = pd.DataFrame(cur.fetchall(), columns=col_names)
    except pg.Error as e:
        st.warning(f"ERROR: Could not execute the query. {e}")
    finally:
        conn.close()
    return results

def run_query_with_params(query, params):
    conn = pg.connect(host=st.secrets["database"]["host"], 
                           port=st.secrets["database"]["port"], 
                           dbname=st.secrets["database"]["dbname"], 
                           user=st.secrets["database"]["user"], 
                           password=st.secrets["database"]["password"])
    cur = conn.cursor()
    cur.execute(query, params)
    col_names = [desc[0] for desc in cur.description]
    results = pd.DataFrame(cur.fetchall(), columns=col_names)
    cur.close()
    conn.close()
    return results


