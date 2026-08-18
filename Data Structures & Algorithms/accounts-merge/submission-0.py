class uf:
    def __init__(self, n):
        self.rank = [1] * (n)
        self.parents = [i for i in range(n)]
    
    def find(self, n):
        p = self.parents[n]
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionfind = uf(len(accounts))
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    unionfind.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = unionfind.find(i)
            emailGroup[leader].append(e)
        res = []
        for i in range(len(accounts)):
            if emailGroup[i]:
                name = accounts[i][0]
                res.append([name] + sorted(emailGroup[i]))
        return res