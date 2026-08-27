# Build: 46d07208a9df48b36f2eafbe0b259bbe

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
