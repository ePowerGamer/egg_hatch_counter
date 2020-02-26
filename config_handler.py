def load(app):
    file = open('data.cfg', 'r')

    app.origin_x = file.readline().split(':')[1].strip()
    app.origin_y = file.readline().split(':')[1].strip()
    app.origin_txt.set("{0}, {1}".format(app.origin_x, app.origin_y))

    app.haystack_width = file.readline().split(':')[1].strip()
    app.haystack_height = file.readline().split(':')[1].strip()
    app.bottom_right_txt.set("{0}, {1}".format(int(app.haystack_width) + int(app.origin_x),
                                               int(app.haystack_height) + int(app.origin_y)))

    file.close()


def save(app):
    file = open('data.cfg', 'w')

    file.write("origin x: {0}\n".format(app.origin_x))
    file.write("origin y: {0}\n".format(app.origin_y))
    file.write("haystack width: {0}\n".format(app.haystack_width))
    file.write("haystack height: {0}\n".format(app.haystack_height))

    file.close()
