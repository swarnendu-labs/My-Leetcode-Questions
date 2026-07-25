class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        depth_len = {0: 0}
        
        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')
            
            if '.' in name:
                max_len = max(max_len, depth_len[depth] + len(name))
            else:
                depth_len[depth + 1] = depth_len[depth] + len(name) + 1
                
        return max_len