import os, certifi
from huggingface_hub import snapshot_download
from sentence_transformers import SentenceTransformer

CACERT_PATH = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = CACERT_PATH
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_ENABLE_XET"] = "False"  # Critical fix

# Pre-download model
#model_path = snapshot_download(
#    repo_id="sentence-transformers/all-MiniLM-L6-v2",
#    cache_dir="./hf_cache",
#    local_dir="./hf_cache/all-MiniLM-L6-v2",
#    resume_download=True
#)
#print(f"Model downloaded to: {model_path}")

# Load SentenceTransformer from local path
#model = SentenceTransformer(model_path)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', cache_folder='./hf_cache')
print("✅ Model loaded successfully!")

