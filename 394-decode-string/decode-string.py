class Solution:
    def decodeString(self, s: str) -> str:
        def is_char(c):
            return "a" <= c <= "z"
        
        def is_bracket(c):
            return c in ["[", "]"]

        stack = []
        number_string = ""

        for c in s:
            if is_char(c):
                if number_string:
                    stack.append(int(number_string))
                    number_string = ""
                stack.append(c)

            elif is_bracket(c):
                if number_string:
                    stack.append(int(number_string))
                    number_string = ""
                if c == "[":
                    stack.append("[")

                else:
                    decoded_string = ""
                    s = None
                    while stack and stack[-1] != "[":
                        s = stack.pop()
                        decoded_string = s + decoded_string
                    else:
                        n = stack.pop()
                        n = int(stack.pop())
                        stack.append(decoded_string * n)
            else:
                number_string += c

        return "".join(stack)

            




            


