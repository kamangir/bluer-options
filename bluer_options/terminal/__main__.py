import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_options import NAME
from bluer_options.terminal.functions import hr, hr_pattern
from bluer_options.logger.config import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="hr",
)
parser.add_argument(
    "--width",
    type=int,
    default=80,
)
parser.add_argument(
    "--pattern",
    type=str,
    default=hr_pattern,
)
parser.add_argument(
    "--mono",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()


success = False
if args.task == "hr":
    success = True
    print(
        hr(
            width=args.width,
            pattern=args.pattern,
            mono=args.mono,
        )
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
