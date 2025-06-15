def index():
    with open("temledes/index.html") as f:
        return f.read()


def blog():
    with open("temledes/blog.html") as f:
        return f.read()

