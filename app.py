from model_loader import load_model
from enhancer import enhance_resume_section

# Load the model
print("🔄 Loading model (may take a minute)...")
llm = load_model()

# Read resume content from text file
with open("sample_input.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

# Enhance resume
print("\\n🔍 Original Resume Text:")
print(resume_text)

print("\\n✨ Enhanced Resume Text:")
enhanced = enhance_resume_section(llm, resume_text)
print(enhanced)
