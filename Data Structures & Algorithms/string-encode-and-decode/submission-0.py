import base64
import json


class Solution:
    def encode(self, strs: List[str]) -> str:
        s = json.dumps(strs)
        return base64.b64encode(s.encode("utf-8")).decode()

    def decode(self, s: str) -> List[str]:
        return json.loads(base64.b64decode(s).decode("utf-8"))
