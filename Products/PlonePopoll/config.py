# -*- coding: utf-8 -*-
## PlonePopoll: A Plone poll tool
## Copyright (C)2005 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
PlonePopoll product
"""
# $Id: config.py 49717 2007-09-19 17:37:21Z glenfant $

__docformat__ = 'restructuredtext'

GLOBALS     = globals()
PROJECTNAME = 'PlonePopoll'
SKINS_DIR   = 'skins'
TOOL_ID     = 'portal_popoll'
I18N_DOMAIN = 'plonepopoll'
NEEDED_PRODUCTS = ['Archetypes']

# Default permissions for PlonePopoll
PlonePopoll_addPermission  = "Popoll: Add polls"
PlonePopoll_editPermission = "Popoll: Edit polls"
PlonePopoll_votePermission = "Popoll: Vote"


