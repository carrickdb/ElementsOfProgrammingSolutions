from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    s =[]
    for comp in path.split("/"):
        if comp=="" or comp==".":
            continue
        if comp=="..":
            if s and s[-1] != "..":
                s.pop()
            else:
                s.append(comp)
        else:
            s.append(comp)
    normpath = '/'.join(s)
    if path and path[0] == "/":
        return "/" + normpath
    return normpath


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
