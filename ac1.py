import os
import google.generativeai as g
from google.generativeai import types
client=g.configure(api_key="AIzaSyAhKCXXHgbr8f9Ld0NPzLuF0jKnfESUz2A")

def generate_response(prompt,temperature=0.3):
    try:
        contents=[types.Content(role="user",parts=[types.Part.from_text(text=prompt)])]
        config_params=types.GenerateContentConfig(temperature=temperature)
        response=client.models.generate_content(
            model="gemini-2.0-flash",contents=contents,config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")

    prompt=input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'):")
    initial_response=generate_response(prompt)
    print(f"\nInitial AI response: {initial_response}")

    modified_prompt=input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): ")
    modified_response=generate_response(modified_prompt)
    print(f"\nModified AI Response (Neutral): {modified_response}")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")

    long_prompt=input("Enter a long prompt (more than 300 words, e.g., a detailed story or description):")
    long_resopnse=generate_response(long_prompt)
    print(f"\nResponse to Long Prompt: {long_resopnse[:500]}...")

    short_prompt=input("Now, condense the prompt to be more concise: ")
    short_response=generate_response(short_prompt)
    print(f"\nResponse to Condensed Prompt: {short_response}")

def run_activity():
    print("\n=== AI Learning Activity ===")

    activity_choice=input("Which activity would you like to run? (1. Bias Mitigation. 2:Token Limits): ")

    if activity_choice=="1":
        bias_mitigation_activity()
    elif activity_choice=="2":
        token_limit_activity()
    else:
        print("Invalid choice.Please choose either 1 or 2.")

if __name__=="__main__":
    run_activity()