import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timezone
import psycopg2 as pg

## Helper function to run queries
##  assumes you have database credentials stored in your secrets.toml file

def run_query(query, params=None, database="grants"):
    """Run a parameterized query on the specified database and return results as a DataFrame."""
    try:
        conn = pg.connect(host=st.secrets[database]["host"], 
                            port=st.secrets[database]["port"], 
                            dbname=st.secrets[database]["dbname"], 
                            user=st.secrets[database]["user"], 
                            password=st.secrets[database]["password"])
        cur = conn.cursor()
        if params is None:
            cur.execute(query)
        else:
            cur.execute(query, params)
        col_names = [desc[0] for desc in cur.description]
        results = pd.DataFrame(cur.fetchall(), columns=col_names)
    except pg.Error as e:
        st.warning(f"ERROR: Could not execute the query. {e}")
    finally:
        cur.close()
        conn.close()
    return results


