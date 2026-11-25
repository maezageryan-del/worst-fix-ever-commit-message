"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes a single commit message, at most 100 characters, for a bug fix
that made everything worse, to /output/entry.txt (MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = "fix: the 500 error by returning 200 instead \u2014 the page still fails, but successfully"


def main() -> None:
    # The gate counts the file's characters (1-100), so write the line
    # exactly, with no trailing newline.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
