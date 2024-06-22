# Streamlit Application Template
This is a template for a Streamlit application that connects to a PostgreSQL database to run queries and display the results. The application is set up to match Gitcoin branding with a light theme and uses the monospace font. 

## To get started with this template, follow these steps:

1. Clone the repository.
2. Install the required packages listed in the requirements.txt file. You can do this by running `pip install -r requirements.txt` in your terminal.
3. Update the .streamlit/secrets.toml file with your database credentials.
4. Run the Streamlit application by typing `streamlit run app.py` in your terminal.

## Optional: Use the helper function to run queries on your database
The application includes helper functions to run queries on your database and return the results as a pandas DataFrame. 

Please note that the functions assume you have your database credentials stored in your secrets.toml file. If you do not have this file set up, you can: 
1. Create a new file called secrets.toml in the .streamlit folder.
2. Add your database credentials to the file in the following format:
```
[database]
host = "your_host"
port = "your_port"
database = "your_database"
user = "your_user"
password = "your_password"
```




