import gradio as gr
from model_loader import load_model

llm = load_model()

def enhance_text(input_text):
    prompt = f"Enhance the following resume:\n\n{input_text}\n\nImproved Version:"
    output = llm(prompt, max_tokens=500, temperature=0.7, top_p=0.9)
    return output["choices"][0]["text"]

iface = gr.Interface(
    fn=enhance_text,
    inputs=gr.Textbox(lines=10, placeholder="Paste your resume here..."),
    outputs="text",
    title="Resume Enhancer AI",
    description="Improve your resume using an open-source LLM!"
)

iface.launch(share=True)
