"""Build temperature-logger.hex from main.py for micro:bit v2 drag-and-drop."""
from pathlib import Path

import micropython_microbit_fs as microbit_fs

root = Path(__file__).resolve().parent
source = (root / "main.py").read_text(encoding="utf-8")
firmware = microbit_fs.get_bundled_hex(2, "2.1.2")
hex_data = microbit_fs.add_files(
    firmware.content,
    [microbit_fs.File.from_text("main.py", source)],
)
output = root / "temperature-logger.hex"
with output.open("w", encoding="ascii", newline="\n") as f:
    f.write(hex_data)
print("Wrote", output)
