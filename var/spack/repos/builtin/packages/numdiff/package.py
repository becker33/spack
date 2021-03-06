##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import sys

class Numdiff(Package):
    """Numdiff is a little program that can be used to compare putatively
    similar files line by line and field by field, ignoring small numeric
    differences or/and different numeric formats."""

    homepage  = 'https://www.nongnu.org/numdiff'
    url       = 'http://nongnu.askapache.com/numdiff/numdiff-5.8.1.tar.gz'

    version('5.8.1',    'a295eb391f6cb1578209fc6b4f9d994e')

    depends_on('gettext', when=sys.platform=='darwin', type='build')

    def install(self, spec, prefix):
        options = ['--prefix=%s' % prefix]
        configure(*options)
        make()
        make('install')
