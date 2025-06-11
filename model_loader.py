from huggingface_hub import hf_hub_download
from llama_cpp import Llama

def load_model():
    model_path = hf_hub_download(
        repo_id="codegood/gemma-2b-it-Q4_K_M-GGUF",
        filename="gemma-2b-it.Q4_K_M.gguf",
        token=True
    )
    llm = Llama(model_path=model_path, n_gpu_layers=1, n_ctx=2048)
    return llm

