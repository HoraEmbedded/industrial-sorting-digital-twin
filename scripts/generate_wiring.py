"""Generate the PLC wiring sheets of the sorting line (SVG and HTML).

The sheets are drawn from the I/O tables below, which follow
docs/en/electrical-design.md. Standard library only.

Usage, from the repository root:
    python scripts/generate_wiring.py

Outputs, written to electrical/:
    wiring-supply.svg, wiring-inputs.svg, wiring-outputs.svg, wiring-sheets.html
"""
from html import escape
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "electrical"
DATE = "2026-10-04"
TOTAL_SHEETS = 5

WIDTH = 1400
ROW_H = 32
FONT = "Consolas, 'Courier New', monospace"
INK = "#1a1a1a"
BLUE = "#1f4e9e"
RED = "#b3261e"
GREY = "#555555"
FILL = "#f3f6fb"

# Layout of the input sheet
RAIL_X, DEV_X, DEV_W = 70, 120, 340
IN_PLC_X, PLC_W = 900, 260

# Layout of the output sheet
OUT_PLC_X = 140
VIA_X = 520
LOAD_X, LOAD_W = 800, 380
GND_X = 1260

# (PLC tag, device label, description, terminal)
INPUTS_A1 = [
    ("I_EmergencyStop", "-S0", "Emergency stop, contact 2 (NC)", "I0.0"),
    ("I_Stop", "-S2", "Stop pushbutton (NC)", "I0.1"),
    ("I_Start", "-S1", "Start pushbutton (NO)", "I0.2"),
    ("I_Reset", "-S3", "Reset pushbutton (NO)", "I0.3"),
    ("I_Auto", "-S4", "Selector, Auto contact", "I0.4"),
    ("I_Manual", "-S4", "Selector, Manual contact", "I0.5"),
    ("I_AtEntry", "-B2", "Sensor at entry", "I0.6"),
    ("I_AtFront", "-B3", "Sensor at front", "I0.7"),
    ("I_AtTurntableEntry", "-B4", "Sensor at turntable entry", "I1.0"),
    ("I_AtLoadPosition", "-B5", "Sensor at load position", "I1.1"),
    ("I_AtUnloadPosition", "-B6", "Sensor at unload position", "I1.2"),
    ("I_AtLeftEntry", "-B7", "Sensor at left entry", "I1.3"),
    ("I_AtRightEntry", "-B9", "Sensor at right entry", "I1.4"),
    ("I_AtBack", "-B1", "Sensor at back", "I1.5"),
]
INPUTS_A2 = [
    ("I_AtLeftExit", "-B8", "Sensor at left exit", "DI 0"),
    ("I_AtRightExit", "-B10", "Sensor at right exit", "DI 1"),
    ("I_HighBox", "-B11", "Light curtain, high output", "DI 2"),
    ("I_LowBox", "-B11", "Light curtain, low output", "DI 3"),
]

# (PLC tag, device label, description, terminal, interlock contact or None)
OUTPUTS_A1 = [
    ("Q_FeederConveyor", "-KM1", "Contactor coil, feeder conveyor", "Q0.0", None),
    ("Q_EntryConveyor", "-KM2", "Contactor coil, entry conveyor", "Q0.1", None),
    ("Q_LeftConveyor", "-KM3", "Contactor coil, left conveyor", "Q0.2", None),
    ("Q_RightConveyor", "-KM4", "Contactor coil, right conveyor", "Q0.3", None),
    ("Q_Load", "-KM5", "Contactor coil, rollers forward", "Q0.4", "-KM6 NC"),
    ("Q_Unload", "-KM6", "Contactor coil, rollers reverse", "Q0.5", "-KM5 NC"),
    ("Q_Turn", "-YV1", "Solenoid valve, turntable rotation", "Q0.6", None),
    ("Q_RemoverLeft", "-YV2", "Solenoid valve, left remover", "Q0.7", None),
    ("Q_RemoverRight", "-YV3", "Solenoid valve, right remover", "Q1.0", None),
]
OUTPUTS_A3 = [
    ("Q_GreenIndicator", "-H1", "Tower lamp, green", "DQ 0", None),
    ("Q_YellowIndicator", "-H2", "Tower lamp, yellow", "DQ 1", None),
    ("Q_RedIndicator", "-H3", "Tower lamp, red", "DQ 2", None),
    ("Q_StartLight", "-H4", "Start pushbutton lamp", "DQ 3", None),
    ("Q_StopLight", "-H5", "Stop pushbutton lamp", "DQ 4", None),
    ("Q_ResetLight", "-H6", "Reset pushbutton lamp", "DQ 5", None),
]


class Sheet:
    """A drawing sheet collecting SVG elements."""

    def __init__(self, number, title):
        self.number = number
        self.title = title
        self.height = 0
        self.items = []

    def line(self, x1, y1, x2, y2, color=INK, width=1.6):
        self.items.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>')

    def rect(self, x, y, w, h, fill="#ffffff", width=1.6):
        self.items.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="{fill}" stroke="{INK}" stroke-width="{width}"/>')

    def dot(self, x, y, color=INK, r=3.5):
        self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')

    def text(self, x, y, s, size=13, anchor="start", color=INK, weight="normal"):
        self.items.append(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'text-anchor="{anchor}" fill="{color}" font-weight="{weight}">'
            f'{escape(s)}</text>')

    def device(self, x, y, w, label, desc):
        """Device box centred on y."""
        self.rect(x, y - 12, w, 24)
        self.text(x + 8, y + 5, f"{label}  {desc}")

    def finish(self, height):
        """Set the sheet height and draw the frame and the title block."""
        self.height = height
        tb = height - 70
        self.rect(10, 10, WIDTH - 20, height - 20, fill="none", width=2)
        self.text(40, 50, f"Sheet {self.number}: {self.title}", size=20, weight="bold")
        self.line(10, tb, WIDTH - 10, tb, width=2)
        for x in (560, 1000, 1200):
            self.line(x, tb, x, height - 10, width=1)
        self.text(25, tb + 27, "Industrial Sorting Line, control cabinet")
        self.text(25, tb + 48, "Theoretical design, not built, not certified", size=11, color=GREY)
        self.text(575, tb + 38, self.title, size=14, weight="bold")
        self.text(1015, tb + 27, "HoraEmbedded")
        self.text(1015, tb + 48, DATE, size=11, color=GREY)
        self.text(1215, tb + 38, f"Sheet {self.number} of {TOTAL_SHEETS}", size=14, weight="bold")

    def render(self):
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {self.height}" '
            f'width="{WIDTH}" height="{self.height}">\n'
            f'<rect width="{WIDTH}" height="{self.height}" fill="#ffffff"/>\n')
        return head + "\n".join(self.items) + "\n</svg>\n"


def draw_input_group(s, rows, y_first, title, power):
    """One block of PLC inputs: devices on the left, PLC terminals on the right."""
    y_last = y_first + (len(rows) - 1) * ROW_H
    y_power = y_last + ROW_H
    y_bottom = y_power + (len(power) - 1) * ROW_H + 25
    top = y_first - 35
    s.rect(IN_PLC_X, top, PLC_W, y_bottom - top, fill=FILL)
    s.text(IN_PLC_X + PLC_W / 2, top - 10, title, anchor="middle", weight="bold")
    s.line(RAIL_X, y_first, RAIL_X, y_last, color=RED)
    s.text(RAIL_X, y_first - 20, "+24V", size=12, anchor="middle", color=RED)
    for i, (tag, label, desc, addr) in enumerate(rows):
        y = y_first + i * ROW_H
        s.line(RAIL_X, y, DEV_X, y, color=RED)
        s.dot(RAIL_X, y, color=RED)
        s.device(DEV_X, y, DEV_W, label, desc)
        s.line(DEV_X + DEV_W, y, IN_PLC_X, y)
        s.text((DEV_X + DEV_W + IN_PLC_X) / 2, y - 5, tag, size=12, anchor="middle", color=BLUE)
        s.dot(IN_PLC_X, y)
        s.text(IN_PLC_X + 12, y + 4, addr)
    for k, (name, net) in enumerate(power):
        y = y_power + k * ROW_H
        s.dot(IN_PLC_X, y)
        s.text(IN_PLC_X + 12, y + 4, name)
        s.line(IN_PLC_X - 80, y, IN_PLC_X, y, color=RED)
        s.text(IN_PLC_X - 90, y + 4, net, size=12, anchor="end", color=RED)
    return y_bottom


def draw_output_group(s, rows, y_first, title, power):
    """One block of PLC outputs: PLC terminals on the left, loads on the right."""
    y_last = y_first + (len(rows) - 1) * ROW_H
    y_power = y_last + ROW_H
    y_bottom = y_power + (len(power) - 1) * ROW_H + 25
    top = y_first - 35
    right = OUT_PLC_X + PLC_W
    s.rect(OUT_PLC_X, top, PLC_W, y_bottom - top, fill=FILL)
    s.text(OUT_PLC_X + PLC_W / 2, top - 10, title, anchor="middle", weight="bold")
    s.line(GND_X, y_first, GND_X, y_last, color=GREY)
    s.text(GND_X, y_first - 20, "0V", size=12, anchor="middle", color=GREY)
    for i, (tag, label, desc, addr, via) in enumerate(rows):
        y = y_first + i * ROW_H
        x_end = VIA_X if via else LOAD_X
        s.dot(right, y)
        s.text(right - 12, y + 4, addr, anchor="end")
        s.line(right, y, x_end, y)
        s.text((right + x_end) / 2, y - 5, tag, size=12, anchor="middle", color=BLUE)
        if via:
            s.rect(VIA_X, y - 12, 120, 24)
            s.text(VIA_X + 60, y + 4, via, size=12, anchor="middle")
            s.line(VIA_X + 120, y, LOAD_X, y)
        s.device(LOAD_X, y, LOAD_W, label, desc)
        s.line(LOAD_X + LOAD_W, y, GND_X, y, color=GREY)
        s.dot(GND_X, y, color=GREY)
    for k, (name, net) in enumerate(power):
        y = y_power + k * ROW_H
        s.dot(right, y)
        s.text(right - 12, y + 4, name, anchor="end")
        s.line(right, y, right + 80, y, color=RED)
        s.text(right + 90, y + 4, net, size=12, color=RED)
    return y_bottom


def supply_sheet():
    """Sheet 3: control supply 24 V DC and emergency stop."""
    s = Sheet(3, "Control supply 24 V DC and emergency stop")

    # 230 V side: L1 and N
    s.text(50, 155, "L1")
    s.line(90, 150, 140, 150)
    s.rect(140, 135, 120, 30)
    s.text(150, 155, "-F2  2 A")
    s.line(260, 150, 330, 150)
    s.text(50, 215, "N")
    s.line(90, 210, 330, 210)
    s.text(50, 255, "230 V AC control supply", size=12, color=GREY)

    # Power supply -G1
    s.rect(330, 110, 190, 140, fill=FILL)
    s.text(345, 130, "-G1", size=14, weight="bold")
    s.text(338, 154, "L", size=12)
    s.text(338, 214, "N", size=12)
    s.text(512, 154, "+24V", size=12, anchor="end", color=RED)
    s.text(512, 214, "0V", size=12, anchor="end", color=GREY)
    s.text(425, 182, "PSU 230 V AC", size=12, anchor="middle")
    s.text(425, 200, "24 V DC, 5 A", size=12, anchor="middle")

    # 0V line
    s.line(520, 210, 550, 210, color=GREY)
    s.line(550, 210, 550, 600, color=GREY)
    s.line(550, 600, 1100, 600, color=GREY)
    s.text(1110, 605, "0V (to sheets 4 and 5)", size=12, color=GREY)

    # +24V rail
    s.line(520, 150, 600, 150, color=RED)
    s.line(600, 150, 600, 480, color=RED)
    s.text(606, 138, "+24V", size=12, color=RED)

    # Branch 1: PLC, sensors and lamps
    s.dot(600, 150, color=RED)
    s.line(600, 150, 680, 150, color=RED)
    s.rect(680, 135, 100, 30)
    s.text(690, 155, "-F3  2 A")
    s.line(780, 150, 1060, 150, color=RED)
    s.text(1070, 155, "+24V to sheets 4 and 5", size=12, color=RED)

    # Branch 2: loads, cut by the emergency relay contact
    s.dot(600, 260, color=RED)
    s.line(600, 260, 680, 260, color=RED)
    s.rect(680, 245, 100, 30)
    s.text(690, 265, "-F4  2 A")
    s.line(780, 260, 860, 260, color=RED)
    s.text(820, 252, "+24V-L", size=11, anchor="middle", color=RED)
    s.rect(860, 245, 150, 30)
    s.text(870, 265, "-KA1 NO (13-14)", size=12)
    s.line(1010, 260, 1060, 260, color=RED)
    s.text(1070, 265, "+24VS to sheet 5 (-A1 output supply)", size=12, color=RED)

    # Branch 3: emergency stop contact 2 to the PLC input
    s.dot(600, 370, color=RED)
    s.line(600, 370, 680, 370, color=RED)
    s.rect(680, 355, 170, 30)
    s.text(690, 375, "-S0 NC (21-22)")
    s.line(850, 370, 1060, 370)
    s.text(1070, 375, "I_EmergencyStop to -A1 I0.0 (sheet 4)", size=12, color=BLUE)

    # Branch 4: emergency stop contact 1 to the relay coil
    s.dot(600, 480, color=RED)
    s.line(600, 480, 680, 480, color=RED)
    s.rect(680, 465, 170, 30)
    s.text(690, 485, "-S0 NC (11-12)")
    s.line(850, 480, 900, 480)
    s.rect(900, 465, 130, 30)
    s.text(910, 485, "-KA1 coil")
    s.line(1030, 480, 1060, 480, color=GREY)
    s.line(1060, 480, 1060, 600, color=GREY)
    s.dot(1060, 600, color=GREY)

    s.text(40, 660, "-S0 is an emergency stop with two NC contacts. Contact 1 feeds -KA1, contact 2 is the PLC input.", size=12)
    s.text(40, 682, "-KA1 is a standard relay. A certified safety relay is required on a real machine.", size=12)
    s.finish(780)
    return s


def inputs_sheet():
    """Sheet 4: PLC inputs."""
    s = Sheet(4, "PLC inputs")
    b1 = draw_input_group(
        s, INPUTS_A1, 150, "-A1 CPU 1214C DC/DC/DC, digital inputs",
        [("L+", "+24V"), ("M", "0V"), ("1M", "0V")])
    b2 = draw_input_group(
        s, INPUTS_A2, b1 + 80, "-A2 SM 1221 DI 8 x 24 V DC, channels 0 to 3",
        [("1M", "0V")])
    s.text(40, b2 + 40, "Sensors -B1 to -B11: PNP, three-wire (brown +24V, blue 0V, black signal). Only the +24V and signal wires are drawn.", size=12)
    s.text(40, b2 + 60, "PLC terminal names (L+, M, 1M) must be checked against the Siemens S7-1200 System Manual. Spare channels are not drawn.", size=12)
    s.finish(b2 + 150)
    return s


def outputs_sheet():
    """Sheet 5: PLC outputs."""
    s = Sheet(5, "PLC outputs")
    b1 = draw_output_group(
        s, OUTPUTS_A1, 150, "-A1 CPU 1214C DC/DC/DC, digital outputs",
        [("L+", "+24VS (from sheet 3)"), ("M", "0V")])
    b2 = draw_output_group(
        s, OUTPUTS_A3, b1 + 80, "-A3 SM 1222 DQ 8 x 24 V DC, channels 0 to 5",
        [("L+", "+24V (not switched)"), ("M", "0V")])
    s.text(40, b2 + 40, "-KM5 and -KM6 are interlocked by NC auxiliary contacts. Motor power circuits are on sheets 1 and 2.", size=12)
    s.text(40, b2 + 60, "-A1 outputs are supplied from +24VS, cut by -KA1 on emergency stop. -A3 lamps are supplied from +24V and stay available.", size=12)
    s.text(40, b2 + 80, "Not wired (simulation only): Q_Emit and Q_Counter. PLC terminal names must be checked against the Siemens S7-1200 System Manual.", size=12)
    s.finish(b2 + 170)
    return s


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Industrial Sorting Line, PLC wiring sheets</title>
<style>
@page {{ size: A3 landscape; margin: 0; }}
html, body {{ margin: 0; padding: 0; background: #ffffff; }}
.sheet {{ width: 420mm; height: 297mm; overflow: hidden; page-break-after: always; break-after: page; }}
.sheet:last-child {{ page-break-after: auto; break-after: auto; }}
.sheet img {{ width: 100%; height: 100%; object-fit: contain; display: block; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("Written", path)


def main():
    OUT_DIR.mkdir(exist_ok=True)
    sheets = [
        ("wiring-supply.svg", supply_sheet()),
        ("wiring-inputs.svg", inputs_sheet()),
        ("wiring-outputs.svg", outputs_sheet()),
    ]
    divs = []
    for name, sheet in sheets:
        write(OUT_DIR / name, sheet.render())
        alt = f"Sheet {sheet.number}: {sheet.title}"
        divs.append(f'<div class="sheet"><img src="{name}" alt="{alt}"></div>')
    write(OUT_DIR / "wiring-sheets.html", PAGE.format(body="\n".join(divs)))


if __name__ == "__main__":
    main()