import gui
import actions


def work():
    p = gui.path_file()
    act = gui.action()
    match act:
        case '/r':
            actions.read_file(p)
        case '/w':
            actions.write_in_file(p)
        case '/f':
            actions.find_in_file(p)
        case '/d':
            actions.delete_in_file(p)