import os
try:
    import uvicorn
except:
    os.system("sudo apt install python3-pip")
    os.system("pip install uvicorn")
    import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
    