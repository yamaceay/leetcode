class Solution(object):
    def levelOrder(self, root):
        copyQueues = [[root]]
        queues = [[root]]
        for j in range(1000):
            queues.append([])
            copyQueues.append([])
        i = 0
        while len(queues[i]):
            tmp = queues[i].pop(0)
            if not tmp: continue
            for child in tmp.children:
                if not child: continue
                queues[i+1].append(child)
                copyQueues[i+1].append(child)
            if not len(queues[i]):
                i += 1
        nodeLevels = [[x.val for x in queue if x] for queue in copyQueues if len(queue)]
        return nodeLevels if nodeLevels[0] else []