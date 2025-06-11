def enhance_resume_section(llm, text: str) -> str:
    prompt = f"""
You are an expert resume writer.
Improve the following resume section to make it more professional:
---
{text}
---
Return the improved version only.
"""
    result = llm(prompt, max_tokens=256)
    return result["choices"][0]["text"]
