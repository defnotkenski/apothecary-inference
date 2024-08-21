from utils import setup_logger
from ApothecaryComfy import ApothecaryComfy
from pathlib import Path

if __name__ == "__main__":
    log = setup_logger()
    input_path = Path.cwd().joinpath("input")
    output_path = Path.cwd().joinpath("output")

    log.info("Running ComfyUI server.")
    apot_comfy = ApothecaryComfy("127.0.0.1:8188")

    apot_comfy.start_server(input_dir=input_path, output_dir=output_path)
