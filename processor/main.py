import os
import logging

from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()

if __name__ == "__main__":
    config = Config()

    input_files = [
        f.path
        for f in os.scandir(config.INPUT_DIR)
        if f.is_file() and os.path.splitext(f.name)[1].lower() == config.InputType
    ]

    for input_file in input_files:
        log.info(f"input_file: {input_file}")

    # TODO: read input file
    # TODO: convert from input format to output format
    # TODO: write output file
