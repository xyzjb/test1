import argparse
import sys

import subprocess

from pathlib import Path

    
def main(args):
    parser = argparse.ArgumentParser(description='Write prediction data to PVC')
    parser.add_argument("--srcdirname", type=str, required=True)
    #parser.add_argument("--subdirname1", type=str, required=True)
    
    args = parser.parse_args(args)
    
    srcdirname = args.srcdirname
    #subdirname1 = args.subdirname1
    
    filepath='/data/data/'
    Path(filepath).mkdir(parents=True, exist_ok=True)
    subprocess.run("cp -R "+ srcdirname + " "+filepath  , shell=True, capture_output=False)

if __name__ == '__main__':
    main(sys.argv[1:])
    
    