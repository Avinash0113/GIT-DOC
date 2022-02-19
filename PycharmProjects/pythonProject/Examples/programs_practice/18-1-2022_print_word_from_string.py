# user_input = "https://www.interviewbit.com/event/free-mock-coding-interview/?utm_source=ib&utm_medium=top_nudge&utm_campaign=MoCo&utm_content=/practice/"

# output = www.interviewbit.com

# string_1 = user_input.split()
#
# print(string_1)

import re
user_input = "https://www.interviewbit.com/event/free-mock-coding-interview/?utm_source=ib&utm_medium=top_nudge&utm_campaign=MoCo&utm_content=/practice/"
pattern = re.compile(r"www.interviewbit.com")
matches = pattern.search(user_input)
print(matches)







