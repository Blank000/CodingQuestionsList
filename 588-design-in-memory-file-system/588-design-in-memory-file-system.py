class Directory:
    
    def __init__(self, name, isFile=False):
        self.isFile = isFile
        self.name = name
        self.child = {}
        self.content = []
        
class FileSystem:

    def __init__(self):
        self.rootDir = Directory("")

    def ls(self, path: str) -> List[str]:
        paths = path.split("/")
        curr_dir = self.rootDir
        for i in range(1, len(paths)):
            if paths[i] not in curr_dir.child:
                break
            curr_dir = curr_dir.child[paths[i]]
        if curr_dir.isFile:
            return [curr_dir.name]
        return sorted(list(curr_dir.child.keys()))

    def mkdir(self, path: str) -> None:
        paths = path.split("/")
        curr_dir = self.rootDir
        for i in range(1, len(paths)):
            #print(curr_dir.name, "+", curr_dir.child)
            if paths[i] not in curr_dir.child:
                curr_dir.child[paths[i]] = Directory(paths[i])
            curr_dir = curr_dir.child[paths[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split("/")
        curr_dir = self.rootDir
        for i in range(1, len(paths)-1):
            if paths[i] not in curr_dir.child:
                return
            curr_dir = curr_dir.child[paths[i]]
            
        if paths[-1] not in curr_dir.child:
            curr_dir.child[paths[-1]] = Directory(paths[-1], True)
        curr_dir = curr_dir.child[paths[-1]]
        curr_dir.content.append(content)
        
    def readContentFromFile(self, filePath: str) -> str:
        paths = filePath.split("/")
        curr_dir = self.rootDir
        #print(curr_dir.child["a"].child["b"].child["c"].child["d"].content)
        for i in range(1, len(paths)):
            if paths[i] not in curr_dir.child:
                return
            curr_dir = curr_dir.child[paths[i]]
        if not curr_dir.isFile:
            return ""
        return "".join(curr_dir.content)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)