import copy
from typing import Any
from bluer_options import NAME


class Options(dict):
    def __add__(self, options: "Options") -> "Options":
        output = copy.deepcopy(self)
        output.update(Options(options))
        return output

    def __init__(self, *args):
        super().__init__()

        if not args:
            return

        if len(args) > 1:
            for index in range(0, len(args), 2):
                self[args[index]] = args[index + 1]
            return

        if isinstance(args[0], dict):
            self.update(args[0])
            return

        if not isinstance(args[0], str):
            raise NameError(f"-{NAME}: cannot read {args[0].__class__.__name__}.")

        for item in args[0].split(","):
            if item in "-+" or not item:
                continue

            if item.startswith("+"):
                self[item[1:]] = True
            elif item.startswith("-") or item.startswith("~") or item.startswith("!"):
                self[item[1:]] = False
            elif "=" in item:
                option_name = item.split("=")[0]
                option_value = "=".join(item.split("=")[1:])
                self[option_name] = option_value
            else:
                self[item] = True

    def get(self, keyword: str, default: Any) -> Any:
        output = super().get(keyword, default)

        if isinstance(default, bool):
            try:
                return bool(output)
            except:
                return default

        if isinstance(default, int):
            try:
                return int(output)
            except:
                return default

        if isinstance(default, float):
            try:
                return float(output)
            except:
                return default

        return output

    def to_str(self) -> str:
        return ",".join(
            sorted(
                [
                    (
                        f"+{keyword}"
                        if value is True
                        else f"~{keyword}" if value is False else f"{keyword}={value}"
                    )
                    for keyword, value in self.items()
                ]
            )
        )
