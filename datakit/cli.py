import sys

from pyflags.flag import Flags

flag = Flags()
flag.add_file(["--file"], "What file do you want to parse", validator=lambda x: ".csv" in x)
flag.add(["--top"], "List the top n number of values", int)
flag.add(["--corr-threshold"], "How strong should the correclation be", float)
flag.add(["--include"], "What columns to include", str)
flag.add(["--exclude"], "What columns to exclude", str)
flag.add(["--format-text"], "What output should it use", str)
flag.add(["--no-insights"], "Quiet mode", bool)

flag.parse_and_resolve(sys.argv[1:])