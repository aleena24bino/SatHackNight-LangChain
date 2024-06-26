

![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)



# Law Sphere
### Powered by AI, driven by Justice
Law Sphere is an AI-driven web application providing intelligent legal assistance and document generation services. Utilizing advanced language models via the Groq API and leveraging the LangChain framework for prompt management, it ensures accessible, efficient, and reliable support through a secure and user-friendly interface built with Streamlit. Key features include user authentication, AI-powered legal advice, document generation, and query-response history tracking. The application leverages a modern, customizable theme and maintains security with SHA-256 password hashing. Designed for easy setup and deployment, Law Sphere aims to democratize legal support and streamline legal document creation for individuals and professionals alike.

<img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" height="30" alt="streamlit logo"/><img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="45" alt="python logo"/><img width="12" />
<img src="groq-logo.png" alt="groq-logo" height="40"><img width="12" />
<img src="https://images.seeklogo.com/logo-png/52/1/langchain-logo-png_seeklogo-528369.png" alt="langchain-logo" height="40"><img width="12"/>


## Team members
1. [Meenakshi M Kumar](https://github.com/Meenakshimkumar)
2. [Meenakshi Pramod](https://github.com/MeenakshiPramod)
3. [Aleena Bino](https://github.com/aleena24bino)

   
## Link to product walkthrough
![Law_Sphere_1](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/a11fb7a8-96c4-4d63-85ff-4736609aa668)
![Law_Sphere_2](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/cbf56c0c-97a3-48e8-ae76-9c8e2b568e55)
![Law_Sphere_3](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/6ac26baf-3e32-4136-852b-9d49252ff050)
![Law_Sphere_4](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/e6c654a8-21da-4ba8-92c7-bfad4666f802)
![Law_Sphere_5](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/8e84ba78-e25c-48f1-8da1-b01cb8fcd396)
![Law_Sphere_6](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/0c4a4227-4d7c-4731-9f50-6071a769e10a)



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

[link to video](https://github.com/aleena24bino/SatHackNight-LangChain/assets/118379816/18f1236f-eda7-43dd-8f74-b2e31da11570)

   
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
4. Activate the virtual environment.
   ```
    env/Scripts/activate.bat
   ```
5. Install streamlit using pip.
   ```
    pip install streamlit
   ```
6. Install langchain and groq using pip.
   ```
    pip install langchain-groq
   ```
7. Install requests using pip
     ```
    pip install requests
   ```
8. Set an environment variable for the Groq API Key

    In Command Prompt(cmd)
    ```
    set GROQ_API_KEY=your_api_key_here
    ```
     In Powershell
     ```
     $env:GROQ_API_KEY = "your_api_key_here"
     ```

9. Verifying whether the environment variable is set

    In Command Prompt(cmd)
    ```
    echo %GROQ_API_KEY%
    ```
     In Powershell
     ```
     echo $env:GROQ_API_KEY
    ```
    If set it will show your original API key.
   
10. If required, you can upgrade pip(optional)
    ```
    python -m pip install --upgrade pip
    ```

## How to Run
   ```
    streamlit run legalAI.py
   ```
