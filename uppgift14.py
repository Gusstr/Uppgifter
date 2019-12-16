Alist = ["A", "B", "A"]
def has_equalend_to(A):
    if A[0] == A[-1]:
        return True
    else:
        return False

print(has_equalend_to(Alist))
