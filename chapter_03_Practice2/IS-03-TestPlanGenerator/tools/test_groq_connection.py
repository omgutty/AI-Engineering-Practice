#!/usr/bin/env python3
"""
Phase 2: Link - GROQ Connection Verification
Verifies that GROQ API is accessible and can generate text.
"""

import os
import json
from dotenv import load_dotenv

try:
    from groq import Groq
except ImportError:
    print("ERROR: groq package not installed. Run: pip install groq")
    exit(1)

# Load environment variables
load_dotenv(dotenv_path="../.env")

def test_groq_connection():
    """Test GROQ API connectivity and model availability."""
    
    GROQ_KEY = os.getenv("GROQ_KEY")
    
    if not GROQ_KEY:
        return {
            "status": "error",
            "message": "Missing GROQ_KEY in .env"
        }
    
    try:
        client = Groq(api_key=GROQ_KEY)
        
        # Test with a simple prompt
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "user", "content": "Say 'GROQ connection successful' in exactly 5 words."}
            ],
            temperature=0.7,
            max_tokens=50
        )
        
        message_content = response.choices[0].message.content
        
        return {
            "status": "success",
            "message": "GROQ connection successful",
            "model": "mixtral-8x7b-32768",
            "response": message_content.strip(),
            "tokens_used": {
                "prompt": response.usage.prompt_tokens,
                "completion": response.usage.completion_tokens,
                "total": response.usage.total_tokens
            }
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"GROQ connection error: {str(e)}"
        }

if __name__ == "__main__":
    result = test_groq_connection()
    print(json.dumps(result, indent=2))
