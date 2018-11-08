"""
Blacklist is a plugin for Beets that can mark library items as "blacklisted".
Once marked, items can be filtered from beets queries.

To blacklist, issue the command:

beet blacklist <query>

To un-blacklist, issue the command:

beet clearblacklist <query>

Then, to filter out items from queries:

beet ls ^blacklist:true <query>

Or, to list the items that are currently blacklisted:

beet ls blacklist:true <query>

"""

from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.dbcore import types
from beets import ui

def set_blacklist(lib, opts, args):
    """Mark the results of a query as blacklisted"""
    items = lib.items(ui.decargs(args))
    for item in items:
        item.update({'blacklist':'true'})
        item.store()
    print ('Blacklisted ' + str(len(items)) + ' items')
set_blacklist_command = Subcommand('blacklist',
                             help='mark the results of a query as blacklisted',
                             aliases=('blk',))
set_blacklist_command.func = set_blacklist


def clear_blacklist(lib, opts, args):
    """Clear the blacklisting value of the results of a query"""
    items = lib.items(ui.decargs(args))
    for item in items:
        item.update({'blacklist':None})
        item.store()
    print ('Cleared blacklisting for ' + str(len(items)) + ' items')
clear_blacklist_command = Subcommand('clearblacklist',
                            help='clear the blacklisting of the results of a query',
                            aliases=('cblk',))
clear_blacklist_command.func = clear_blacklist


class BlacklistPlugin(BeetsPlugin):
    """Marks items as blacklisted and removes from queries, when desired"""
    item_types = {'blacklist': types.STRING}

    def __init__(self):
        super(BlacklistPlugin, self).__init__()

    def commands(self):
        return [set_blacklist_command,
                clear_blacklist_command]
