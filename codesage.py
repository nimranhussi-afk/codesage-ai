"""
CodeSage - AI Code Review Agent
Automatically reviews GitHub repositories and provides detailed feedback
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from git import Repo
import tempfile

load_dotenv()

# Setup AI model
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0
)

def get_github_code(github_url: str):
    """Download code from GitHub repository"""
    temp_folder = tempfile.mkdtemp()
    Repo.clone_from(github_url, temp_folder)
    
    code_files = []
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    code_files.append({
                        'name': file,
                        'code': f.read()[:2000]
                    })
    
    return code_files

async def review_code_simple(github_url: str):
    """
    Review a GitHub repository and provide detailed feedback
    
    Args:
        github_url: URL of the GitHub repository to review
        
    Returns:
        str: Detailed code review
    """
    print("📥 Downloading code...")
    files = get_github_code(github_url)
    print(f"✓ Found {len(files)} files\n")
    
    all_code = "\n\n".join([f"FILE: {f['name']}\n{f['code']}" for f in files[:5]])
    
    print("🤖 Analyzing...\n")
    
    prompt = f"""
Review this GitHub code:

{all_code}

Provide:
1. What it does (simple explanation)
2. Good things
3. Problems found
4. 3 improvements
"""
    
    response = await llm.ainvoke([{"role": "user", "content": prompt}])
    review = response.content
    
    print("="*60)
    print(review)
    print("="*60)
    
    with open("code_review.txt", "w") as f:
        f.write(review)
    
    print("\n✓ Saved to code_review.txt")
    return review

if __name__ == "__main__":
    import asyncio
    
    # Example usage
    example_repo = "https://github.com/pallets/flask"
    asyncio.run(review_code_simple(example_repo))
