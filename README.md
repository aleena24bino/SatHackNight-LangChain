

![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)



# Law Sphere
### Powered by AI, driven by Justice
Law Sphere is an AI-driven web application providing intelligent legal assistance and document generation services. Utilizing advanced language models via the Groq API and leveraging the LangChain framework for prompt management, it ensures accessible, efficient, and reliable support through a secure and user-friendly interface built with Streamlit. Key features include user authentication, AI-powered legal advice, document generation, and query-response history tracking. The application leverages a modern, customizable theme and maintains security with SHA-256 password hashing. Designed for easy setup and deployment, Law Sphere aims to democratize legal support and streamline legal document creation for individuals and professionals alike.

## Team members
1. [Meenakshi M Kumar](https://github.com/Meenakshimkumar)
2. [Meenakshi Pramod](https://github.com/MeenakshiPramod)
3. [Aleena Bino](https://github.com/aleena24bino)
## Link to product walkthrough
[link to video](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/18f1236f-eda7-43dd-8f74-b2e31da11570)

## How it Works ?

**1. Setup and Configuration:**
 * Streamlit Page Configuration: The page is configured with a custom theme including background, text, and primary colors.
 * Groq API Key: The application retrieves the Groq API key from the environment variable GROQ_API_KEY.
   
**2. Database Initialization:**
  * SQLite Connection: The application connects to an SQLite database (user_profiles.db).
  * Tables Creation: If not already present, it creates two tables: users for user authentication data and user_profiles for storing user queries and AI-generated responses.
    
**3. Session State Initialization:**
  * Session Variables: It initializes session state variables to keep track of the user's login status, user ID, and username.
    
**4.  User Authentication:**
  * Signup: Users can create a new account by providing a username, email, and password. The password is hashed using SHA-256 before being stored.
  * Login: Existing users can log in using their email and password. Upon successful login, session state variables are updated with the user's information.
    
**5. AI Model Initialization:**
  * Chat Models: Two AI models are initialized using the Groq API:
   * chat for legal advice with the llama3-70b-8192 model.
   * llm for document generation with the llama3-8b-8192 model.
     
**6. Prompt Templates:**
 * Legal Advice Prompt: A prompt template for legal advice is defined.
 *  Document Generation Prompt: A prompt template for document generation is defined.
     
**7. User Interface:**
 * Main Interface: Once logged in, users are welcomed and presented with a text area to input their queries or document content.
 * Option Selection: Users can select either "Get Legal Advice" or "Generate Document" from a dropdown menu.
   
**8. Processing User Input:**
 * Legal Advice:
  Upon clicking "Give Advice," the user input is processed through the legal advice model.
  The generated response is displayed and saved in the database.
 * Document Generation:
 Upon clicking "Generate Document," the user input is processed through the document generation model.
 The generated document content is displayed and saved in the database.

**9. Display User History:**
 * Query and Response History: The application retrieves and displays the user's previous queries and responses from the database.
   
**10. Closing the Database Connection:**
 * Connection Closure: The database connection is closed at the end of the script to ensure proper resource management.
   
## Libraries used
1. Streamlit
2. ChatPromptTemplate
3. ChatGroq
4. os
## How to configure
1. Install Python.
2. Clone this repository.
3. Create the virtual environment.
   ```
    python -m venv env
   ```
5. Activate the virtual environment.
   ```
    env/Scripts/activate.bat
   ```
7. Install streamlit using pip.
   ```
    pip install streamlit
   ```
8. Install langchain and groq using pip.
   ```
    pip install langchain-groq
   ```
9. Install requests using pip
     ```
    pip install requests
   ```
10. Set an environment variable for the Groq API Key

    In cmd
    ```
    set GROQ_API_KEY=your_api_key_here
    ```
     In Powershell
     ```
     $env:GROQ_API_KEY = "your_api_key_here"
   ```
11. Verifying the environment variable is set
    In Command Prompt
    ```
    echo %GROQ_API_KEY%
   ```
    In Powershell
    ```
    echo $env:GROQ_API_KEY
   ```
## How to Run
Instructions for running
