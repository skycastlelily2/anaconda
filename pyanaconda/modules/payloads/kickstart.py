#
# Kickstart handler for packaging.
#
# Copyright (C) 2018 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
from pykickstart.errors import KickstartParseError
from pykickstart.sections import PackageSection
from pykickstart.parser import Packages
from pykickstart.constants import KS_BROKEN_IGNORE

from pyanaconda.core.configuration.anaconda import conf
from pyanaconda.core.i18n import _
from pyanaconda.core.kickstart import VERSION, KickstartSpecification, commands as COMMANDS


class AnacondaPackageSection(PackageSection):

    def handleHeader(self, lineno, args):
        """Process packages section header.

        Add checks based on configuration settings.
        """
        super().handleHeader(lineno, args)

        if not conf.payload.enable_ignore_broken_packages \
           and self.handler.packages.handleBroken == KS_BROKEN_IGNORE:
            raise KickstartParseError(
                _("The %packages --ignorebroken feature is not supported on your product!"),
                lineno=lineno
            )


class PayloadKickstartSpecification(KickstartSpecification):

    version = VERSION

    commands = {
        "liveimg": COMMANDS.Liveimg
    }

    sections = {
        "packages": AnacondaPackageSection
    }

    sections_data = {
        "packages": Packages
    }
