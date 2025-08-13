from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class ToolMeta:
    """
    Represents metadata about an external scanner/tool.
    Keep this domain-only (no file IO here).
    """
    name: str
    display_name: str
    categories: List[str] = field(default_factory=list)   # e.g. ["code", "python"]
    supported_languages: List[str] = field(default_factory=list)  # e.g. ["python"]
    cli_entry: Optional[str] = None   # e.g. "bandit"
    license: Optional[str] = None
    description: Optional[str] = None

    def supports_language(self, language: str) -> bool:
        if not language:
            return False
        return language.lower() in [l.lower() for l in self.supported_languages]

    def supports_category(self, category: str) -> bool:
        if not category:
            return False
        return category.lower() in [c.lower() for c in self.categories]
