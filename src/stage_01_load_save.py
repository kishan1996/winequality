from src.utils.all_utils import read_config
import argparse
import pandas as pd


if __name__ == '__main__':
    args = argparse.ArgumantParser()

    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_args = args.parse_args()

    print(parsed_args.config)
