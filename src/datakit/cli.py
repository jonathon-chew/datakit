import sys

from .pyflags.flag import Flags

def cli():
    flag = Flags()
    
    flag.add_file(["--file", "-f"], "What file do you want to parse", validator=lambda x: ".csv" in x, required=True)
    flag.add(["--top"], "List the top n number of values", int, default=5)
    flag.add(["--corr-threshold"], "How strong should the correclation be", float, default=0.7)
    flag.add(["--include"], "What columns to include", list[str])
    flag.add(["--exclude"], "What columns to exclude", list[str])
    flag.add(["--format-text"], "What output should it use", str)
    flag.add(["--no-insights"], "Quiet mode", bool)

    flag.parse_and_resolve(sys.argv[1:])

    return flag

cli()