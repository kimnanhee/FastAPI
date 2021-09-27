from typing import List, Optional
from fastapi import Request

class LoginForm:
    def __init__(self, request: Request):
        self.request: Request=request
        self.errors: List=[]
        self.id: Optional[str]=None
        self.pw: Optional[str]=None

    async def load_data(self):
        form = await self.request.form()
        self.id = form.get("id")
        self.pw = form.get("pw")

    async def is_vaild(self):
        if not self.id or len(self.id) < 5:
            self.errors.append("A valid id is required")
        if not self.pw or len(self.pw) < 8:
            self.errors.append("A valid pw is required")

        if not self.errors:
            return True
        return False