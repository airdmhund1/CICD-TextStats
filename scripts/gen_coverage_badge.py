#!/usr/bin/env python3
# Generates assets/coverage.svg from coverage.xml without external deps.
import xml.etree.ElementTree as ET
from pathlib import Path

xml_path = Path("coverage.xml")
assets_dir = Path("assets")
assets_dir.mkdir(parents=True, exist_ok=True)

if not xml_path.exists():
    raise SystemExit("coverage.xml not found. Run tests with coverage first.")

tree = ET.parse(xml_path)
root = tree.getroot()
# Cobertura XML has 'line-rate' attribute on root
line_rate = root.attrib.get("line-rate", None)
pct = 0.0
if line_rate is not None:
    pct = round(float(line_rate) * 100, 1)
else:
    # Fallback: try totals/lines-valid/lines-covered
    lines_valid = root.find(".//lines-valid")
    lines_covered = root.find(".//lines-covered")
    if lines_valid is not None and lines_covered is not None:
        try:
            pct = round(100.0 * float(lines_covered.text) / float(lines_valid.text), 1)
        except Exception:
            pct = 0.0

label = "coverage"
color = "red"
if pct >= 90:
    color = "brightgreen"
elif pct >= 80:
    color = "green"
elif pct >= 70:
    color = "yellow"
elif pct >= 60:
    color = "orange"

svg = f"""
    <svg
        xmlns="http://www.w3.org/2000/svg" \
        width="120" \
        height="20" \
        role="img" \
        aria-label="{label}: {pct}%
    ">
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="m"><rect width="120" height="20" rx="3" fill="#fff"/></mask>
  <g mask="url(#m)">
    <rect width="65" height="20" fill="#555"/>
    <rect x="65" width="55" height="20" fill="#{color}"/>
    <rect width="120" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" \
    text-anchor="middle" \
    font-family="DejaVu Sans,Verdana,Geneva,sans-serif" \
    font-size="11">
    <text x="33" y="15">{label}</text>
    <text x="91" y="15">{pct}%</text>
  </g>
</svg>
"""
(assets_dir / "coverage.svg").write_text(svg, encoding="utf-8")
print(f"Wrote {assets_dir / 'coverage.svg'} with {pct}%")
