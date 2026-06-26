class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            # Greedily fit as many words as possible
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i
            total_chars = sum(len(word) for word in words[i:j])

            # Last line or single-word line
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                even_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""
                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (even_spaces + (1 if k < extra_spaces else 0))
                line += words[j - 1]

            res.append(line)
            i = j

        return res