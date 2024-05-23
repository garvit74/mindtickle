from pydantic import BaseModel
from typing import Optional


class SearchQuery(BaseModel):
    q: str
    industry: Optional[str] = None
    use_case: Optional[str] = None
    geography: Optional[str] = None
