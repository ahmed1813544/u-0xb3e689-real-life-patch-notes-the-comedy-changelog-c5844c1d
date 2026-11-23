"""Real-Life Patch Notes entry.

Writes a single-line patch note for a bug in real life / human biology
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, deterministic: every run writes the exact same bytes.
"""

import os

PATCH_NOTE = (
    "v3.1.4: fixed a bug where walking through a doorway cleared "
    "the user's short-term memory. Root cause: the doorway."
)


def main() -> None:
    # The gate requires 1-160 characters, not only whitespace.
    assert 1 <= len(PATCH_NOTE) <= 160, "patch note must be 1-160 chars"
    assert PATCH_NOTE.strip() == PATCH_NOTE
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PATCH_NOTE + "\n")


if __name__ == "__main__":
    main()
