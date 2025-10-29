README

1. Tools Used
- Python 3
- Google Gemini 2.5 Flash API

2. Thought Process / Architecture
- I wanted to keep the code as minimal as possible since an LLM is supposed to be used to read the Policy PDF and apply the rules. The code uploads the Loan Policy PDF to Gemini and it also sends the Application JSON to Gemini. Gemini uses the Policy PDF to evaluate the Application and returns the output of the loan. 

3. Potential Future Improvements/Challenges
- A challenge I was faced with was how to take in the Loan Policy PDF and the Application JSON. My initial option was to keep both files in the parent folder. However, if the Application JSON keeps changing, it would be tedious for the user to keep switching files or overwriting the file. So then I decided to keep the Loan Policy PDF in the parent folder while the user must provide the path to the Application JSON as a path when running the code. 
- A future improvement can be a better way for the user to upload the Application JSON. Maybe a more intuitive way of uploading it by using an interface, so it is easier for the user. 

4. How To Run The Code
- Install the Dependencies 
    - pip3 install google-generativeai
- run "python3 athena.py path/to/application.json"