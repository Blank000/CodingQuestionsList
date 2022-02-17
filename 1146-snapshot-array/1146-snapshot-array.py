import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.length = length
        self.dic = collections.defaultdict(list)
        for i in range(self.length):
            self.dic[i].append((0, 0))

    def set(self, index: int, val: int) -> None:
        if len(self.dic[index]) == 0 or self.dic[index][-1][0] < self.snap_id:
            self.dic[index].append((self.snap_id, val))
        else:
            arr = self.dic[index]
            snap_id, _ = arr[-1]
            arr[-1] = (snap_id, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1
                

    def get(self, index: int, snap_id: int) -> int:
        arr = self.dic[index]
        idx = bisect.bisect_left(arr, (snap_id, 0))
        if idx < len(arr) and arr[idx][0] == snap_id:
            return arr[idx][1]
        return arr[idx-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)