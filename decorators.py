"""Decorators"""

from progress.bar import Bar


class ProgressBar:
    bar_list = []

    def __init__(self, text, aim, recursion=False):
        if not recursion:
            self.bar_list.append(ProgressBar(text, aim, recursion=True))
        else:
            self.progress = Bar(text, max=aim)

    def __call__(self, func):
        def add_progress(*args):
            bar = self.bar_list[0]

            result = func(*args)
            bar.progress.next()

            if bar.progress.index == bar.progress.max:
                bar.progress.finish()
                self.bar_list.pop(0)

            return result

        return add_progress
