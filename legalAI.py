import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
import sqlite3
from hashlib import sha256

# Get the Groq API key from the environment variable
groq_api_key = os.getenv('GROQ_API_KEY', 'your_groq_api_key_here')

# SQLite connection and cursor initialization
conn = sqlite3.connect('user_profiles.db')
c = conn.cursor()

# Create user_profiles and users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS user_profiles
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER,
              query TEXT,
              response TEXT,
              FOREIGN KEY(user_id) REFERENCES users(id))''')
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              email TEXT UNIQUE,
              password TEXT)''')

if not groq_api_key:
    st.error("Groq API key not found. Please set the GROQ_API_KEY environment variable.")
else:
    # Initialize the chat model for legal advice
    chat = ChatGroq(
        temperature=0,
        model="llama3-70b-8192",
        api_key=groq_api_key 
    )
    # Initialize the model for document generation
    llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

# Define the chat prompts
system_legal = "You are an intelligent legal assistant who provides legal advice."
human_legal = "{text}"
prompt_legal_advice = ChatPromptTemplate.from_messages([("system", system_legal), ("human", human_legal)])

system_doc_gen = "You are an intelligent assistant for document generation."
human_doc_gen = "{text}"
prompt_doc_gen = ChatPromptTemplate.from_messages([("system", system_doc_gen), ("human", human_doc_gen)])

st.set_page_config(page_title="Law Sphere")
st.title("Law Sphere")
st.markdown('### Powered by AI, driven by Justice')

# Function to hash passwords
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Initialize session state variables if not already set
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "username" not in st.session_state:
    st.session_state.username = ""

# User authentication
if not st.session_state.logged_in:
    auth_mode = st.selectbox("Select Authentication Mode:", ["Signup", "Login"])

    if auth_mode == "Signup":
        st.header("Signup")
        username = st.text_input("Enter your username:")
        email = st.text_input("Enter your email:")
        password = st.text_input("Enter your password:", type="password")
        if st.button("Signup"):
            if username and email and password:
                c.execute("SELECT * FROM users WHERE email=?", (email,))
                if c.fetchone() is not None:
                    st.error("Email already exists. Please use a different email.")
                else:
                    hashed_password = hash_password(password)
                    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                              (username, email, hashed_password))
                    conn.commit()
                    st.success("Signup successful. Please login.")
            else:
                st.error("Please fill all the fields.")
    elif auth_mode == "Login":
        st.header("Login")
        email = st.text_input("Enter your email:")
        password = st.text_input("Enter your password:", type="password")
        if st.button("Login"):
            if email and password:
                hashed_password = hash_password(password)
                c.execute("SELECT id, username FROM users WHERE email=? AND password=?", (email, hashed_password))
                user = c.fetchone()
                if user:
                    user_id, username = user
                    st.session_state.logged_in = True
                    st.session_state.user_id = user_id
                    st.session_state.username = username
                    st.success(f"Welcome, {username}!")
                else:
                    st.error("Invalid email or password.")
            else:
                st.error("Please fill all the fields.")
else:
    st.header(f"Welcome, {st.session_state.username}!")

    user_input = st.text_area("Enter your query or document content:")

    # User selects whether to get legal advice or generate a document
    option = st.selectbox("Choose an option:", ["Get Legal Advice", "Generate Document"])

    if option == "Get Legal Advice":
        if st.button("Give Advice"):
            # Chain for legal advice
            chain = prompt_legal_advice | chat
            response = chain.invoke({"text": user_input})
            st.write(response.content)
            # Save query and response to database
            c.execute("INSERT INTO user_profiles (user_id, query, response) VALUES (?, ?, ?)",
                      (st.session_state.user_id, user_input, response.content))
            conn.commit()
    elif option == "Generate Document":
        if st.button("Generate Document"):
            # Chain for document generation
            chain = prompt_doc_gen | llm
            response = chain.invoke({"text": user_input})
            st.write(response.content)
            # Save query and response to database
            c.execute("INSERT INTO user_profiles (user_id, query, response) VALUES (?, ?, ?)",
                      (st.session_state.user_id, user_input, response.content))
            conn.commit()

    # Display user's previous queries and responses
    st.header("Your Previous Queries and Responses:")
    c.execute("SELECT query, response FROM user_profiles WHERE user_id=? ", (st.session_state.user_id,))
    rows = c.fetchall()
    for row in rows:
        st.text("Query: " + row[0])
        st.text("Response: " + row[1])

# Close database connection
conn.close()
