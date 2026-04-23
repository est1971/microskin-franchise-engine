from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "docs" / "validation" / "sandbox" / "VALIDATION_LOG.md"
FINAL = ROOT / "docs" / "FINAL_VALIDATION_REPORT.md"


def run(cmd: list[str]) -> tuple[int, str]:
    completed = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    output = (completed.stdout + "\n" + completed.stderr).strip()
    return completed.returncode, output


def main() -> None:
    steps = [
        ("Calibration importer", [str(ROOT / ".venv" / "bin" / "python"), "scripts/import_calibration.py"]),
        ("Sandbox smoke app", [str(ROOT / ".venv" / "bin" / "python"), "scripts/smoke_app.py"]),
        ("Pytest", [str(ROOT / ".venv" / "bin" / "pytest")]),
    ]
    lines = ["# Sandbox Validation Log", "", "Validation runs executed in sandbox mode with recursive repair expectations.", ""]
    critical_pass = True
    for name, cmd in steps:
        code, output = run(cmd)
        lines.extend([f"## {name}", "", f"- Command: `{' '.join(cmd)}`", f"- Exit code: `{code}`", "", "```text", output[:12000], "```", ""])
        if code != 0:
            critical_pass = False
    guardian = "PASS" if critical_pass else "FAIL"
    lines.extend(["## Guardian Completion Event", "", f"- Critical validation status: `{guardian}`", "- End-to-end sandbox flow executed.", ""])
    LOG.write_text("\n".join(lines), encoding="utf-8")
    FINAL.write_text(
        "\n".join(
            [
                "# Final Validation Report",
                "",
                f"- Critical validation pass: `{guardian}`",
                "- Validation scope: importer, API, engine, export path, and UI-contract coverage via automated tests.",
                "- Guardian completion event recorded in `/docs/validation/sandbox/VALIDATION_LOG.md`.",
                "",
            ]
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
