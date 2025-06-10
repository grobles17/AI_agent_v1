import os
import sys #import to use sys.argv to allow for inputs from the shell
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY") #Reads the .env file where the API key is stored (same directory as main.py!)

    client = genai.Client(api_key=api_key) #connects to google ai api

    import sys 
    #Check if string is passed before assigning it or it will error
    if len(sys.argv) < 2: #if length of list smaller than 2 i.e. not string passed
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1) #sys exit with error code 1

    prompt = " ".join(sys.argv[1:]) #[0] is the name of the script (not useful) and each after are the strings passed
            
    answer = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

    print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")
    print("Response:")

    try:
        print(answer.text)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__=="__main__":
    main()