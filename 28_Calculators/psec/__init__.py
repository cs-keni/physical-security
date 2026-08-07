"""psec -- physical security engineering calculators.

Pure standard library. No dependencies, so it runs on a locked-down work laptop
without asking anyone for permission to pip install anything.

    from psec import optics, video, power, pps

Every module states its assumptions in its docstring. Read them. A calculator
you do not understand is a liability, not a tool -- the number it produces will
go into a document with your name on it, and "the spreadsheet said so" is not a
defence in a design review.

Work the corresponding lesson in ../../32_Engineering_Math/ by hand before you
use the matching module here.
"""

from . import optics, power, pps, video

__all__ = ["optics", "video", "power", "pps"]
__version__ = "0.1.0"
