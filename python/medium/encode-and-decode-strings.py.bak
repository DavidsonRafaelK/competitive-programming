class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            eq = s.find('#', i)
            length = int(s[i:eq])
            res.append(s[eq + 1 : eq + 1 + length])
            i = eq + 1 + length

        return res
