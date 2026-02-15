import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_options import NAME
from bluer_options.host.functions import get_name, tensor_processing_signature
from bluer_options.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = [
    "get",
    "tensor_processing_signature",
]

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="get",
    help=" | ".join(list_of_tasks),
)
parser.add_argument(
    "--keyword",
    type=str,
    help="name",
)
args = parser.parse_args()


success = args.task in list_of_tasks
# bash-tested in test_bluer_ai_host in bluer-objects.
if args.task == "get":
    success = True
    output = f"unknown-{args.keyword}"

    if args.keyword == "name":
        output = get_name()

    print(output)
elif args.task == "tensor_processing_signature":
    print(", ".join(tensor_processing_signature()))
else:
    success = None


sys_exit(logger, NAME, args.task, success, log=False)
