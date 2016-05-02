from __future__ import print_function
from string import split, upper
__author__ = 'Richard Primera'
__email__ = "rprimera at urbe.edu.ve"

"""
Copyright 2014 Richard Primera

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the:
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""


class CSconverter(object):
    bit = 1
    B = 8 * bit
    K = 1024 * B
    M = 1024 * K
    G = 1024 * M
    T = 1024 * G
    P = 1024 * T
    E = 1024 * P
    Z = 1024 * E
    Y = 1024 * Z
    units = locals()

    def __init__(self):
        pass

    def get_bits(self, prefix):
        """You give this method a prefix and it tells you
        how many bits there are in it. Useful for calculations"""
        prefix = upper(prefix)
        return self.units[prefix]

    @staticmethod
    def expression_parser(expression):
        """Parses the expression given to the converter, and
        splits it into three parts for calculation.

        A call such as expression_parser('100m:g') will parse
        the expression '100m:g' and format it in this way:

            scalar = 100
            scalar_prefix = uppercase(m)
            conversion_prefix = uppercase(g)

        And these are all the variables you need to perform
        the calculations.
            """
        expression = upper(expression)
        operands = split(expression, ":")
        scalar_part = operands[0]
        conversion_prefix = operands[1]
        scalar_prefix = str([token for token in scalar_part if not token.isdigit()][0])
        scalar = split(scalar_part, str(scalar_prefix))[0]
        return scalar, scalar_prefix, conversion_prefix

    def convert(self, expression):
        """convert(5K:G) should return how many GBytes are in 5KBytes"""
        gb, eparser = self.get_bits, self.expression_parser
        scalar, scalar_prefix, conversion_prefix = eparser(expression)
        scalar = int(scalar)
        scalar_prefix, conversion_prefix = gb(scalar_prefix), gb(conversion_prefix)

        if scalar_prefix == conversion_prefix:
                print("Are you stupid?")
        else:
            return scalar * scalar_prefix * conversion_prefix**-1


"""
Example usage:
% python2
import csconverter
a = csconverter.CSconverter()
a.convert("250M:G")
a.convert("128m:z")
"""
