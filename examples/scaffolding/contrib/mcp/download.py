import argparse
import os
from huggingface_hub import snapshot_download, login
from huggingface_hub.utils import HfHubHTTPError


def download_model(repo_id, local_dir, revision=None, token=None):
    if token:
        login(token=token)
        print("🔐 Using Hugging Face token for authentication.")
    else:
        print("ℹ️ No token provided. If the repo is private, make sure you're logged in or pass --token.")

    try:
        print(f"⬇️ Downloading model from: {repo_id}")
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            revision=revision,
            local_dir_use_symlinks=False,
            token=token,
        )
        print(f"✅ Model downloaded to: {local_dir}")
    except HfHubHTTPError as e:
        print(f"❌ Download failed: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a model from Hugging Face Hub to a local directory.")
    parser.add_argument("--repo", required=True, help="Model repo id (e.g., 'meta-llama/Llama-2-7b-hf')")
    parser.add_argument("--out", required=True, help="Output directory to save the model")
    parser.add_argument("--revision", default=None, help="Branch name or commit hash (optional)")
    parser.add_argument("--token", default=os.environ.get("HUGGINGFACE_HUB_TOKEN"), help="Hugging Face access token")

    args = parser.parse_args()
    download_model(args.repo, args.out, args.revision, args.token)

