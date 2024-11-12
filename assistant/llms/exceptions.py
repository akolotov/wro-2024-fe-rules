class GenerationError(Exception):
    """Custom exception for generation errors."""
    pass

class UnexpectedFinishReason(GenerationError):
    """Custom exception for unexpected finish reasons."""
    pass