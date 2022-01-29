class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def doDFS(mergedAccount, node, adjList, visited):
            if node in visited:
                return 
            mergedAccount.append(node)
            visited.add(node)
            neighbours = adjList[node]
            for acc in neighbours:
                doDFS(mergedAccount, acc, adjList, visited)
        
        adjList = collections.defaultdict(set)
        # create k-1 edges for k nodes and that would be fine 
        for i in range(len(accounts)):
            firstEmail = accounts[i][1]
            if firstEmail not in adjList:
                adjList[firstEmail] = set()
            for j in range(2,len(accounts[i])):
                adjList[firstEmail].add(accounts[i][j])
                adjList[accounts[i][j]].add(firstEmail)
        visited = set()
        res = []
        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            if firstEmail not in visited:
                mergedAccount = [name]
                emails = []
                doDFS(emails, firstEmail, adjList, visited)
                mergedAccount.extend(sorted(emails))
                res.append(mergedAccount)
        return res