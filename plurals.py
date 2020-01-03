import re

# def plural(noun):
#     if re.search("[xsz]$", noun):
#         return re.sub("$", "es", noun)
#     elif re.search("[^aeioudgkprt]h$", noun):
#         return re.sub("$", "es", noun)
#     elif re.search('[^aeiou]y$', noun):
#         return re.sub('y$', 'ies', noun)
#     else:
#         return noun + 's'

# print (plural("Boy"))

# def match_sxz(noun):
#     return re.search('[sxz]$', noun)
# def apply_sxz(noun):
#     return re.sub('$', 'es', noun)
# def match_h(noun):
#     return re.search('[^aeioudgkprt]h$', noun)
# def apply_h(noun):
#     return re.sub('$', 'es', noun)
# def match_y(noun):
#     return re.search('[^aeiou]y$', noun)
# def apply_y(noun):
#     return re.sub('y$', 'ies', noun)
# def match_default(noun):
#     return True
# def apply_default(noun):
#     return noun + 's'

# rules = ((match_sxz, apply_sxz),
#     (match_h, apply_h),
#     (match_y, apply_y),
#     (match_default, apply_default)
# )

# def plural(noun):
#     for matches_rule, apply_rule in rules:
#         if matches_rule(noun):
#             return apply_rule(noun)

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def rules(rules_filename):
    with open(rules_filename, encoding="utf-8") as pattern_file:
        for line in pattern_file:
            pattern, search ,replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename="plural4-rules.txt"):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError("No matching rule for {0}".format(noun))           

print(plural("an"))
