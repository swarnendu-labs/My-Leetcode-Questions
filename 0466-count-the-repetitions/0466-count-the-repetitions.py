class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        recall = {}
        s1cnt = s2cnt = index = 0

        while True:
            s1cnt += 1
            for c in s1:
                if c == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt += 1
                        index = 0

            if s1cnt == n1:
                return s2cnt // n2

            if index in recall:
                pre_s1cnt, pre_s2cnt = recall[index]
                break

            recall[index] = (s1cnt, s2cnt)

        pre_loop_s1 = pre_s1cnt
        pre_loop_s2 = pre_s2cnt

        in_loop_s1 = s1cnt - pre_s1cnt
        in_loop_s2 = s2cnt - pre_s2cnt

        ans = pre_loop_s2

        remain = n1 - pre_loop_s1
        ans += (remain // in_loop_s1) * in_loop_s2

        rest = remain % in_loop_s1

        index = list(recall.keys())[list(recall.values()).index((pre_s1cnt, pre_s2cnt))]
        for _ in range(rest):
            for c in s1:
                if c == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0

        return ans // n2