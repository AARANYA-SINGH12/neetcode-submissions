class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq = {}
        tfreq = {}

        for i in s:
            if i in sfreq:
                sfreq[i] += 1
            else:
                sfreq[i] = 0

        for i in t:
            if i in tfreq:
                tfreq[i] += 1
            else:
                tfreq[i] = 0

        if sfreq == tfreq and len(s) == len(t):
            return True

        return False