class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        scomp = [(set(x), i) for i, x in enumerate(favoriteCompanies)]
        scomp.sort(key = lambda x: -len(x[0]))
        ans = set()
        for i, (comp, index) in enumerate(scomp):
            for p2, j in scomp[i + 1:]:
                
                if p2 < comp: ans.add(j)
       
        return sorted(set(range(len(favoriteCompanies))) - ans)