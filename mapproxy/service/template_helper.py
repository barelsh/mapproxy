# This file is part of the MapProxy project.
# Copyright (C) 2010 Omniscale <http://omniscale.de>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from cgi import escape
from mapproxy.template import bunch

__all__ = ['escape', 'indent', 'bunch', 'wms100format']

def indent(text, n=2):
  return '\n'.join(' '*n + line for line in text.split('\n'))

def wms100format(format):
    """
    >>> wms100format('image/png')
    'PNG'
    >>> wms100format('image/GeoTIFF')
    """
    _mime_class, sub_type = format.split('/')
    sub_type = sub_type.upper()
    if sub_type in ['PNG', 'TIFF', 'GIF', 'JPEG']:
        return sub_type
    else:
        return None