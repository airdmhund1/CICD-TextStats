import os
import tempfile

from textstat_mini.cli import main


def test_cli_with_text(capsys):
    rc = main(["--text", "Hello hello world", "--top", "2"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "# Text Stats" in out
    assert "words:" in out
    assert "\n# Top Words" in out
    assert "hello:" in out


def test_cli_with_file(tmp_path, capsys):
    p = tmp_path / "sample.txt"
    p.write_text("a b a c a", encoding="utf-8")
    rc = main(["--file", str(p), "--top", "1"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "a: 3" in out


def test_cli_conflicting_args_stderr(capsys):
    # providing both --text and --file should error

    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write("x")
        fname = f.name
    try:
        rc = main(["--text", "x", "--file", fname])
        err = capsys.readouterr().err
        assert rc != 0
        assert "either --text or --file" in err.lower()
    finally:
        try:
            os.remove(fname)
        except Exception:
            pass


def test_cli_missing_file(capsys, tmp_path):
    missing = tmp_path / "nope.txt"
    rc = main(["--file", str(missing)])
    err = capsys.readouterr().err
    assert rc != 0
    assert "file not found" in err.lower()
