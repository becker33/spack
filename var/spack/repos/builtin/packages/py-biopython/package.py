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

class PyBiopython(Package):
    """It is a distributed collaborative effort to develop Python libraries and applications which address the needs of current and future work in bioinformatics."""
    homepage = "http://biopython.org/wiki/Main_Page"
    url      = "http://biopython.org/DIST/biopython-1.65.tar.gz"

    version('1.65', '143e7861ade85c0a8b5e2bbdd1da1f67')

    extends('python')
    depends_on('py-mx', type=nolink)
    depends_on('py-numpy', type=nolink)

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
