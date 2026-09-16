class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        cur_line = []
        cur_length = 0

        for word in words:

            if cur_length + len(word) + len(cur_line) > maxWidth:

                total_spaces = maxWidth - cur_length
                gaps = len(cur_line) - 1

                if gaps == 0:

                    res.append(cur_line[0] + " " * total_spaces)
                else:
                    base_space = total_spaces // gaps
                    extra_space = total_spaces % gaps

                    line_str = ""
                    for i in range(gaps):

                        spaces = base_space + (1 if i < extra_space else 0)
                        line_str += cur_line[i] + " " * spaces
                    line_str += cur_line[-1]
                    res.append(line_str)

                cur_line = []
                cur_length = 0

            cur_line.append(word)
            cur_length += len(word)

        last_line_str = " ".join(cur_line)
        last_line_str += " " * (maxWidth - len(last_line_str))
        res.append(last_line_str)

        return res