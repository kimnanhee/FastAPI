from datetime import date, datetime
from typing import List, Optional
from fastapi import Request

class BookCreateForm:
    def __init__(self, request: Request):
        self.request: Request=request
        self.errors: List=[]
        self.title: Optional[str]=None
        self.price: Optional[int]=None
        self.publication_date: Optional[date]=None
        self.writer: Optional[str]=None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.price = int(form.get("price"))
        self.publication_date = datetime.strptime(form.get("publication_date"), "%Y-%m-%d").date()
        self.writer = form.get("writer")

    async def is_vaild(self):
        if not self.title:
            self.errors.append("A valid title is required")
        if not self.price or not (self.price >= 1):
            self.errors.append("A valid price is required")
        if not self.publication_date:
            self.errors.append("A valid publication date is required")
        if not self.writer or len(self.writer) < 2:
            self.errors.append("A valid writer date is required")

        if not self.errors:
            return True
        return False