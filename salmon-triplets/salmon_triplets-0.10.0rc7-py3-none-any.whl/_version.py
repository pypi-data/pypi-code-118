
# This file was generated by 'versioneer.py' (0.18) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2022-04-23T21:56:11-0400",
 "dirty": false,
 "error": null,
 "full-revisionid": "b1a940683c302f6cc61a2a4ffa5acbc9bde7470d",
 "version": "v0.10.0rc7"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
