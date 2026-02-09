import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_options import NAME
from bluer_options.web.access.as_str import as_str
from bluer_options.web.access.check import check
from bluer_options.web.access.vars import dict_of_variables
from bluer_options.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = [
    "as_str",
    "check",
    "get_var_name",
]

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=" | ".join(list_of_tasks),
)
parser.add_argument(
    "--emoji",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--keyword",
    type=str,
)
parser.add_argument(
    "--timeout",
    type=int,
    default=3,
    help="in seconds",
)
parser.add_argument(
    "--timestamp",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--url",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = args.task in list_of_tasks
if args.task == "as_str":
    print(
        as_str(
            emoji=args.emoji == 1,
            timestamp=args.timestamp == 1,
        )
    )
elif args.task == "check":
    print(
        int(
            check(
                args.url,
                timeout=args.timeout,
                verbose=args.verbose == 1,
            )
        )
    )
elif args.task == "get_var_name":
    print(
        dict_of_variables()
        .get(args.keyword, {})
        .get(
            "name",
            "",
        )
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
