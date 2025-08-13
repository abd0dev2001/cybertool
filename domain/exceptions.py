class CybertoolError(Exception):
    """Base exception for domain layer."""


class InvalidTargetError(CybertoolError):
    """Raised when target validation fails."""


class ToolNotFoundError(CybertoolError):
    """Raised when a requested tool is not available / unknown."""
