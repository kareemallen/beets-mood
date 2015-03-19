from beets.autotag.match import tag_album
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets import plugins
from beets import ui

tagcloud_command = Subcommand('add-tag', help='Add a tag to the tagcloud' )


def add_tag(lib, opts, args):
    print 'Add tag here'
    #First param is the tag, second is the query
    #TODO check if both arguments included
    tagValue = args[0]
    queryString = args[1]
    queryResults = lib.items(queryString)
    for item in queryResults:
        #TODO Add tag to item
        #TODO extract tag key from tag value
        print 'Item: ' + str(item)

    #Confirm that the user wants to write to these files
    #ui.input_yn('You ready')

    #TODO Write tags


tagcloud_command.func = add_tag

class TagCloud(BeetsPlugin):
    ATTRIB_1_NAME = "tag1"

    ATTRIB_2_NAME = "tag2"

    ATTRIB_3_NAME = "tag3"

    def commands(self):
        return [tagcloud_command]
