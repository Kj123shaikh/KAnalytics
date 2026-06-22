import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

def get_gemini_client():
    """Initializes and returns the Gemini API client safely."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n❌ Error: GEMINI_API_KEY not found in environment variables.")
        print("Please check your .env file and ensure it is properly set.")
        sys.exit(1)
    return genai.Client(api_key=api_key)

def generate_email(client, purpose, sender, receiver, recipient_type):
    """Handles Project 1: Professional Email Generation with Prompt Engineering."""
    # Strict prompt engineering to shape structured AI output
    prompt = f"""
    You are an elite professional writing assistant. 
    Write a highly professional email based on the following structural constraints:
    
    - Purpose/Context: {purpose}
    - Sender Role: {sender}
    - Receiver Role: {receiver}
    - Recipient Domain Type: {recipient_type}
    
    Requirements:
    1. Provide a clear, relevant, and compelling Subject line.
    2. Write a well-structured, polite, and professional email body.
    3. Use standard professional placeholders (like [Your Name]) where required if not fully detailed.
    """
    
    print("\n⏳ Formulating your professional email...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"❌ An error occurred during email generation: {e}"

def generate_study_notes(client, subject, topic, depth):
    """Handles Project 2: Study Notes Generation with Prompt Engineering."""
    # Strict prompt engineering to enforce specific formatting (bullets, key concepts)
    prompt = f"""
    You are an expert academic educator. 
    Generate structured, comprehensive, yet clean study notes based on the following constraints:
    
    - Subject: {subject}
    - Topic Name: {topic}
    - Targeted Depth Level: {depth}
    
    Requirements:
    1. Format the output clearly using structured markdown headers.
    2. Provide a 'Key Concepts' section first.
    3. Use clean bullet points for explanations.
    4. Keep the explanations simple, accurate, and completely matched to the '{depth}' depth tier.
    """
    
    print(f"\n⏳ Synthesizing {depth} level notes for {topic}...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"❌ An error occurred during study notes generation: {e}"

def display_banner():
    """Displays an interactive aesthetic text banner."""
    print("=" * 60)
    print("      🚀 GEMINI AI MULTI-PROJECT TERMINAL WORKBENCH 🚀      ")
    print("=" * 60)

def main():
    # Initialize client safely inside try/except block
    try:
        client = get_gemini_client()
    except Exception as e:
        print(f"❌ Initialization Failed: {e}")
        return

    while True:
        display_banner()
        print("Select an AI Engine tool to execute:")
        print("1️⃣  Project 1: Professional Email Writer")
        print("2️⃣  Project 2: Study Notes Generator")
        print("3️⃣  Exit Application")
        print("=" * 60)
        
        choice = input("Enter option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- 📝 PROFESSIONAL EMAIL WRITER MODE ---")
            purpose = input("Enter email purpose (e.g., leave request, complaint, inquiry): ").strip() #
            sender = input("Enter your role (e.g., student, employee, intern): ").strip() #
            receiver = input("Enter receiver's role (e.g., teacher, manager, HR, client): ").strip() #
            recipient_type = input("Enter recipient type context (e.g., corporate office, academic): ").strip() #
            
            if not all([purpose, sender, receiver, recipient_type]):
                print("\n⚠️  All input parameters are required. Please try again.")
                continue
                
            output = generate_email(client, purpose, sender, receiver, recipient_type)
            print("\n" + "✨" * 15 + " GENERATED OUTPUT " + "✨" * 15)
            print(output)
            print("✨" * 48 + "\n")
            
        elif choice == "2":
            print("\n--- 📚 STUDY NOTES GENERATOR MODE ---")
            subject = input("Enter Subject (e.g., DBMS, Python, AI, Networking): ").strip() #
            topic = input("Enter specific Topic Name: ").strip() #
            
            print("\nSelect Depth Level:")
            print("A. Beginner\nB. Intermediate\nC. Exam-ready") #
            depth_choice = input("Select choice (A/B/C): ").strip().upper()
            
            depth_mapping = {"A": "Beginner", "B": "Intermediate", "C": "Exam-ready"}
            depth = depth_mapping.get(depth_choice, "Intermediate")
            
            if not all([subject, topic]):
                print("\n⚠️  Subject and Topic Name cannot be blank.")
                continue
                
            output = generate_study_notes(client, subject, topic, depth)
            print("\n" + "✨" * 15 + " GENERATED OUTPUT " + "✨" * 15)
            print(output)
            print("✨" * 48 + "\n")
            
        elif choice == "3":
            print("\n👋 Exiting AI Workbench application. Happy Coding!")
            break
        else:
            print("\n❌ Invalid selection! Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Application interrupted by user. Exiting safely.")
        sys.exit(0)