from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [
            {
                'name': ac[0],
                'mail': set(ac[1:])
            }
            for ac in accounts
        ]

        g = defaultdict(list)

        for i in range(len(accounts)):
            for j in range(i, len(accounts)):
                if len(accounts[i]['mail'] & accounts[j]['mail']) > 0:
                    g[i].append(j)
                    g[j].append(i)

        
        v = set([])
        components = []
        for source in list(g.keys()):
            if source in v:
                continue
            visited = set([source])
            stack = [source]
            while stack:
                current = stack.pop()
                
                for target in g[current]:
                    if target in visited:
                        continue
                    
                    visited.add(target)
                    stack.append(target)
            v.update(visited)
            components.append(visited)
        
        output = []
        for component in components:
            mails = set()
            for idx in component:
                mails = mails | accounts[idx]["mail"]
            
            output.append([
                accounts[idx]['name'],
                *sorted(list(mails))
            ])
                
                
        return output