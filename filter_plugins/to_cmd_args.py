#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError

def to_cmd_args(inputdict, prefix='--'):
    if not isinstance(inputdict, dict):
        raise AnsibleError('Filter input wasn\'t a dictionary')
    ret = list()
    for key, value in inputdict.items():
        if value is True:
            new_string = "{}{}".format(prefix, key)
            ret.append(new_string)
        elif type(value) == str:
            new_string = '{}{}=\'{}\''.format(prefix, key, value)
            ret.append(new_string)
    return ret

class FilterModule(object):
    def filters(self):
        return {
            'to_cmd_args': to_cmd_args,
        }
