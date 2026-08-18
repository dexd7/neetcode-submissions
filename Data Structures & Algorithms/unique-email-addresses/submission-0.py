class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashSet = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0]
            nlocal = local.replace('.', '')
            hashSet.add(nlocal+'@'+domain)
        return len(hashSet)