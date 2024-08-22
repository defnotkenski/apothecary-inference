import sys
import threading
import time

from utils import setup_logger
from pathlib import Path
import subprocess
from urllib import request
from urllib.error import URLError

log = setup_logger()
PYTHON = sys.executable


class ApothecaryComfy:
    def __init__(self, server_address):
        self.server_address = server_address

    def start_server(self, input_dir, output_dir) -> None:
        # Start the ComfyUI server on a seperate thread.

        log.info(f"Starting server on seperate thread on: {self.server_address}")
        start_time = time.time()

        server_thread = threading.Thread(target=self.run_server, args=(input_dir, output_dir))
        server_thread.start()

        while not self.is_server_running():
            if time.time() - start_time > 60:
                raise TimeoutError("Server did not start within 60 seconds.")

            time.sleep(1)

        elapsed_time = time.time() - start_time
        log.info(f"Server started in {elapsed_time}.")

        return

    def run_server(self, input_dir: str, output_dir: str) -> None:
        # Run Comfy on the seperate thread.

        path_to_comfy_exec = Path.cwd().joinpath("ComfyUI", "main.py")
        run_cmd = [
            PYTHON,
            str(path_to_comfy_exec),
            "--input-directory",
            str(input_dir),
            "--output-directory",
            str(output_dir),
            "--disable-metadata"
        ]

        log.info(f"Executing command: {run_cmd}")
        server_process = subprocess.Popen(run_cmd)
        server_process.wait()

        return

    def is_server_running(self) -> bool:
        try:
            with request.urlopen(f"http://{self.server_address}") as url_response:
                log.info(url_response)

                return url_response.status == 200
        except URLError as e:
            log.error(f"Error checking to see if server is running: {e}")
            return False
