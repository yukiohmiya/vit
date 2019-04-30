from formatter.tags import Tags

class TagsCount(Tags):
    def format(self, tags, task):
        if not tags:
            return self.empty()
        elif len(tags) == 1:
            return (3, (self.colorizer.tag(list(tags)[0]), '[1]'))
        else:
            tag_length = len(tags)
            indicator = '[%d]' % tag_length
            return (tag_length + 2, (self.colorizer.tag(''), indicator))
