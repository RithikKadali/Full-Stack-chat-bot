Create a virtual environment:
(VScode)Menu → Terminal → New Terminal  
python -m venv env


PS C:\Rithik_Personal\projects\lang_chain> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
PS C:\Rithik_Personal\projects\lang_chain> env\Scripts\Activate
(env) PS C:\Rithik_Personal\projects\lang_chain> 

You’ll see (env) in the terminal when it’s active ✅



(env) PS C:\Rithik_Personal\projects\lang_chain> python -c "import sys; print(sys.executable)"
C:\Rithik_Personal\projects\lang_chain\env\Scripts\python.exe

✅ Final VS Code check (IMPORTANT)

Ctrl + Shift + P

Python: Select Interpreter

	Select:

	Python 3.x ('env': venv)


VS Code will now:

	Use correct Python

	Use correct pip

	Auto-activate env





1. Install required packages(imp)
pip install langchain langchain-openai openai python-dotenv



2. Set your OpenRouter API key (SAFE WAY)
https://openrouter.ai/settings/keys
(unlimited access)

Linux / macOS
export OPENROUTER_API_KEY="your_new_api_key_here"

Windows (PowerShell)
setx OPENROUTER_API_KEY "your_new_api_key_here"

| Error Type | Code | Cause               |
| ---------- | ---- | ------------------- |
| Auth       | 401  | Bad API key         |
| Permission | 403  | Model access denied |
| Rate Limit | 429  | Too many requests   |
| Billing    | 402  | No credits          |
| Model      | 404  | Wrong model         |
| Request    | 400  | Bad payload         |
| Tokens     | —    | Input too large     |
| Network    | —    | Connection issues   |
| Server     | 5xx  | API down            |


##in first level
Or use a .env file:

OPENROUTER_API_KEY=your_new_api_key_here


ques like:
doc: Which area has the highest call drop rate?
doc: What is the downlink speed in the Airport Zone?
doc: List areas with partial cell availability greater than 2%.



######
pip install pypdf
pip install --upgrade langchain langchain-openai python-dotenv pypdf faiss-cpu
pip install langchain langchain-openai faiss-cpu python-dotenv

pip install langchain-community
pip install -U langchain-community

pip uninstall langchain langchain-community -y
pip install langchain==0.1.0
pip install openai python-dotenv faiss-cpu pypdf
✅ BEST & EASIEST FIX (Recommended)
🔥 Option 1: Use NEW LangChain (Stable, 2024+)

This is the correct long-term solution.

Step 1️⃣ Remove conflicting packages
pip uninstall -y langchain langchain-core langchain-community langchain-openai langsmith numpy

Step 2️⃣ Install compatible versions (NEW stack)
pip install \
  langchain \
  langchain-openai \
  langchain-community \
  faiss-cpu \
  python-dotenv \
  numpy<2

pip install langchain langchain-openai langchain-community faiss-cpu python-dotenv "numpy<2"


✔ Works
✔ Stable
✔ Future-proof

Step 3️⃣ Verify
pip list | grep langchain