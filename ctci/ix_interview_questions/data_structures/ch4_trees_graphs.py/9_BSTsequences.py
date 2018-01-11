class BST_node(object):
    def __init__(self, value, lc=None, rc=None):
        self.value = value
        self.lc = lc
        self.rc = rc

def permute(perms, options):
    if len(options) == 0:
        return perms

    total_perms = []
    for i in range(len(options)):
        option = options[i]
        new_options = options[:i] + options[i+1:]
        if option.lc:
            new_options.append(option.lc)
        if option.rc:
            new_options.append(option.rc)
        new_perms = []
        for perm in perms:
            new_perms.append(perm[:])
        for new_perm in new_perms:
            new_perms.append(option.value)
        total_perms.extend(permute(new_perms, new_options))
    return total_perms

def BST_sequences(root):
    return permute([[]], [root])


BST_sequences()