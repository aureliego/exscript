# Copyright (C) 2007 Samuel Abels, http://debain.org
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
import threading
from Action import Action

True  = 1
False = 0

class Sequence(Action):
    def __init__(self, *args, **kwargs):
        Action.__init__(self)
        self.actions = []
        if kwargs.has_key('actions'):
            assert type(kwargs['actions']) == type([])
            for action in kwargs['actions']:
                self.add(action)


    def add(self, action):
        self.actions.append(action)


    def execute(self, global_context, local_context):
        assert local_context  is not None
        assert global_context is not None
        for action in self.actions:
            action.debug = self.debug
            if not action.execute(global_context, local_context):
                return False
        return True
