from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.open_router import router as open_router_router
from utils.port import is_free_port, kill_process_by_port
import uvicorn
import time

app = FastAPI()

app.include_router(open_router_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEFAULT_PORT = 6399

def start_server():
  if not is_free_port(DEFAULT_PORT):    
    success = kill_process_by_port(DEFAULT_PORT)
    if success:
      for i in range(5):
        time.sleep(0.5)
        if is_free_port(DEFAULT_PORT):
          print(f"Port {DEFAULT_PORT} is now available")
          break
        print(f"Waiting for port {DEFAULT_PORT} to be released... ({i+1}/5)")
      else:
        print(f"Warning: Port {DEFAULT_PORT} might still be in use")
    else:
      print(f"Failed to free port {DEFAULT_PORT}")

  try:
    uvicorn.run(app, port=DEFAULT_PORT, host="127.0.0.1")
  except Exception as e:
    print(f"Failed to start server: {e}")

if __name__ == "__main__":
    start_server()