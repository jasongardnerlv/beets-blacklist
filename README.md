# beets-blacklist

Provides blacklisting of items for
[beets](https://github.com/sampsyo/beets) queries.

To blacklist, issue the command:

```
beet blacklist <query>
```

To un-blacklist, issue the command:

```
beet clearblacklist <query>
```

Then, to filter out items from queries:

```
beet ls ^blacklist:true <query>
```

Or, to list the items that are currently blacklisted:

```
beet ls blacklist:true <query>
```

# Installation

Put the beetsplug folder somewhere in your PYTHONPATH and activate tbe plugin
in beets' config.yaml file. This is described in more detail in the [beets
documentation](http://beets.readthedocs.org/en/latest/index.html).