# ✦ Installation and Introduction to FastAPI with Python✦

FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. It's easy to use, yet powerful enough for production-grade applications.

---

## 🔹 1. Prerequisites & Installation 

• 🐍 Python 3.7+

    Install from 🔗 https://www.python.org

• 📦 Pip (Python package installer)
  Usually comes with Python. Check with:

  ```Shell

  pip --version

  
  ```

💡 On macOS or Linux, if you have multiple Python versions installed, you may need to use pip3 instead:

 ```Shell

pip3 --version 
  
```

• 🧪Virtual Environment (optional but recommended)
  To isolate project dependencies:

```Shell

python -m venv .venv

```

💡 On macOS and Linux, you may need to use python3 instead:

```Shell

python3 -m venv .venv

```

💡 For more information about script commands in detail when working with virtual enviorment visit this REPO i have created about it. 

🔗 https://github.com/hanino87/Training_Virtual_Environments_With_Hannes

• ✅ FastAPI & 🚀 Uvicorn 

Install with Pip 

```Shell

pip install fastapi uvicorn

```
💡 On macOS or Linux, if you have multiple Python versions installed, you may need to use pip3 instead:

 ```Shell

pip3 install fastapi uvicorn
  
```

## 🔹 2. Create your first simple endpoint and run FastAPI server 

• 🐍 Create a Pythonfile 

• 🐍  In the pytonfile write following code:

from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World This is my first FastApi"}

@app.get("/welcome")
async def root_results():
    return {"message": "Hello World This is Hannes 1 "}



  




• ✅ Start FastAPI & 🚀 Uvicorn Server

 ```Shell

uvicorn main:app --reload
  
```

uvicorn main:app --reload