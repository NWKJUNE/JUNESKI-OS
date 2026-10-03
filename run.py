import os, uvicorn
from dotenv import load_dotenv
load_dotenv()
if __name__ == "__main__":
    uvicorn.run("cc.app:app", host="127.0.0.1", port=int(os.environ.get("PORT",8765)))
