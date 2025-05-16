import uvicorn

def main():
    uvicorn.run("src.auth_service.main:app", host="127.0.0.1", port=8002, reload=True)
