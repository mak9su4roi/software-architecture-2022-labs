#! /bin/env python3

import subprocess as sub
from argparse import ArgumentParser
from app.config import micro_config

def log_hoock(data: str) -> None:
    print(data)

def main():
    parser = ArgumentParser(prog="launcher", description="...")
    parser.add_argument('--services', metavar='N', type=str, nargs='+',
                        help='services to launch')
    args = parser.parse_args()

    selectes_srvs = micro_config.services.keys() if args.services is None else args.services

    launched = [ 
        srvs.launch() for lbl, srvs in micro_config.services.items()
            if lbl in selectes_srvs
    ]
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        [ srvs.terminate() for srvs in launched ]

if __name__ == "__main__":
    main()