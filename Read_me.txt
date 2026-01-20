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





1. Install required packages
pip install langchain langchain-openai openai python-dotenv



2. Set your OpenRouter API key (SAFE WAY)
Linux / macOS
export OPENROUTER_API_KEY="your_new_api_key_here"

Windows (PowerShell)
setx OPENROUTER_API_KEY "your_new_api_key_here"



##in first level
Or use a .env file:

OPENROUTER_API_KEY=your_new_api_key_here