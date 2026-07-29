class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        lower = upper = digit = 1
        for c in password:
            if c.islower():
                lower = 0
            elif c.isupper():
                upper = 0
            elif c.isdigit():
                digit = 0

        missing = lower + upper + digit

        # Case 1: Too short
        if n < 6:
            return max(missing, 6 - n)

        # Count repeating groups
        replace = 0
        one = two = 0
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 3
                while i + 1 < n and password[i + 1] == password[i]:
                    length += 1
                    i += 1

                replace += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            i += 1

        # Case 2: Valid length
        if n <= 20:
            return max(missing, replace)

        # Case 3: Too long
        delete = n - 20

        # Use deletions optimally
        use = min(delete, one)
        replace -= use
        delete -= use

        use = min(delete, two * 2)
        replace -= use // 2
        delete -= use

        replace -= delete // 3

        return (n - 20) + max(missing, replace)