# --- start AI code ---
"""Exercise the actual terminal prompt on macOS/Linux, including Ctrl-C/D."""

import os
from pathlib import Path
import pty
import select
import signal
import subprocess
import sys
import termios
import time

ROOT = Path(__file__).resolve().parents[2]


def session(interrupt=False):
    master, slave = pty.openpty()
    attributes = termios.tcgetattr(slave)
    attributes[3] &= ~termios.ECHO
    termios.tcsetattr(slave, termios.TCSANOW, attributes)
    process = subprocess.Popen([sys.executable, str(ROOT / "src/main.py"), "--tokens"],
                               stdin=slave, stdout=slave, stderr=slave)
    # Keep the slave open until captured output is drained (including on macOS).
    transcript = []

    def read_prompt():
        data = b""
        deadline = time.monotonic() + 5
        while not data.endswith(b"ember> "):
            if time.monotonic() > deadline:
                raise AssertionError("Timed out waiting for the next prompt.")
            ready, _, _ = select.select([master], [], [], 0.1)
            if ready:
                data += os.read(master, 4096)
        transcript.append(data.decode("utf-8").replace("\r\n", "\n"))

    try:
        read_prompt()
        if interrupt:
            process.send_signal(signal.SIGINT)
        else:
            os.write(master, b"@\n")
            read_prompt()
            os.write(master, b"say\n")
            read_prompt()
            os.write(master, b"\x04")
        status = process.wait(timeout=5)
        # Drain the final newline emitted when the prompt exits.
        while select.select([master], [], [], 0.1)[0]:
            try:
                data = os.read(master, 4096)
            except OSError:
                break  # PTYs may report EIO once the slave closes.
            if not data:
                break
            transcript.append(data.decode("utf-8").replace("\r\n", "\n"))
        return "".join(transcript), status
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        os.close(master)
        os.close(slave)


def main():
    expected = (
        "ember> EOF '' None [line 1]\n"
        "[line 1] Error: Unexpected character '@'.\n"
        "ember> SAY 'say' None [line 1]\nEOF '' None [line 1]\nember> \n", 0)
    actual = session()
    interrupt_expected = ("ember> \n", 0)
    interrupt_actual = session(interrupt=True)
    print("Recovery and Ctrl-D:", "PASS" if actual == expected else "FAIL")
    print("Ctrl-C:", "PASS" if interrupt_actual == interrupt_expected else "FAIL")
    if "--report" in sys.argv:
        lines = ["# Terminal checks", "", "Run: `python3 test/lab1/terminal_test.py --report`.",
                 "", "These tests use a real pseudo-terminal with input echo disabled.",
                 "Ctrl-C is sent as SIGINT; Ctrl-D is sent as the terminal EOF character.", ""]
        for title, source, want, got in [
            ("Recovery and Ctrl-D", "@, Enter, say, Enter, Ctrl-D", expected, actual),
            ("Ctrl-C", "SIGINT while waiting at the first prompt", interrupt_expected, interrupt_actual),
        ]:
            lines.extend([f"## {title}", "", f"Input: {source}", "",
                          "Expected:", "```text", want[0], f"exit status: {want[1]}", "```", "",
                          "Actual:", "```text", got[0], f"exit status: {got[1]}", "```", "",
                          f"Result: {'PASS' if want == got else 'FAIL'}", ""])
        (ROOT / "report/terminal-results.md").write_text("\n".join(lines), encoding="utf-8")
    return 0 if actual == expected and interrupt_actual == interrupt_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
# --- end AI code ---
