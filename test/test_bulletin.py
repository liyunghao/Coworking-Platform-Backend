# E2E testing
# Input space partitioning

# `/create`: userid(C1: is admin or not), 其餘 Variable(C2: Is valid or Not)
# `/read`: postId(C3: post exist or not)
# `/update`: userid(C1: is admin or not, C4: is author or not), postId(C3: post exist or not)
# `/delete`: userid(C1: is admin or not, C4: is author or not), postId(C3: post exist or not)

# Criteria: Base Choice Coverage(BCC)

# testcase

# `/create`(C1, C2):
# - (Basic) true, true
# - false, true
# - ture, false
# - false, false

# `/read`(C3):
# - (Basic) true
# - false

# `/update`(C1, C3, C4):
# - (Basic) true, true, true
# - false, true, true
# - true, false, true
# - true, true, false

# `/delete`(C1, C3, C4):
# - (Basic) true, true, true
# - false, true, true
# - true, false, true
# - true, true, false
