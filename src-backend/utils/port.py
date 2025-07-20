import socket
import subprocess
import os
import sys

def is_free_port(port: int,host: str = "127.0.0.1") -> bool:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
          sock.settimeout(1)
          result = sock.connect_ex((host, port))
          return result != 0
  except Exception:
      return False

def get_free_port(start_port: int, end_port: int, host: str = "127.0.0.1") -> int:
  for port in range(start_port, end_port):
    if is_free_port(port, host):
      return port
  raise Exception("No free port found")

def kill_process_by_port(port: int) -> bool:
  try:
      result = subprocess.check_output(
            f'lsof -t -i:{port}', shell=True, encoding='utf-8')
      pids = result.strip().split('\n')
      for pid in pids:
          if pid:
              os.system(f'kill -9 {pid}')
      return True
  except subprocess.CalledProcessError:
      return False