from operator import itemgetter
from beets.autotag.match import tag_album
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets import plugins
from beets import ui
from flask.debughelpers import attach_enctype_error_multidict

tagcloud_command = Subcommand('add-tag', help='Add a tag to the tagcloud. The first argument is the query the second is the tag' )


def add_tag(lib, opts, args):
    print 'Add tag here'
    #First param is the tag, second is the query
    #TODO check if both arguments included
    queryString = args[0]
    tagValue = args[1]
    print 'Tag: ' + str(tagValue)
    queryResults = lib.items(queryString)
    for item in queryResults:
        #TODO extract tag key from tag value
        if not (tagValue is None) and not (item is None):
            item.mood = tagValue

        print 'Item: ' + str(item)

    #Confirm that the user wants to write to these files
    #TODO Tell user what you are going to write
    attempt_write = ui.input_yn('You ready')
    print attempt_write

    if (attempt_write) :
        item.write()

    #TODO Write tags


tagcloud_command.func = add_tag

class TagCloud(BeetsPlugin):
    ATTRIB_1_NAME = "tag1"

    ATTRIB_2_NAME = "tag2"

    ATTRIB_3_NAME = "tag3"

    def commands(self):
        return [tagcloud_command]
