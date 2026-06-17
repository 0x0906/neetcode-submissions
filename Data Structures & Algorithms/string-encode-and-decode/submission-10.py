class Solution:

    def encode(self, strs: List[str]) -> str:
        data = '->'.join(strs)
        encoded = ""
        for d in data:
            encoded = encoded + chr(ord(d) ^ len(strs))
        encoded += "[len]" + str(len(strs))
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = ""
        data = s.split('[len]')
        encoded = data[0]
        strlen = int(data[1])
        if strlen == 0:
            decoded = []
        elif not encoded and strlen == 1:
            decoded =  [""]
        else:
            for e in encoded:
                decoded = decoded + chr(ord(e) ^ strlen)
            decoded = decoded.split('->')
        return decoded