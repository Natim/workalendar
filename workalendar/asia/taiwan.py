# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from gettext import gettext as _
from ..core import ChineseNewYearCalendar, WesternCalendar
from ..astronomy import solar_term
from ..registry_tools import iso_register


@iso_register('TW')
class Taiwan(ChineseNewYearCalendar, WesternCalendar):
    "Taiwan (Republic of China)"
    FIXED_HOLIDAYS = (
        WesternCalendar.FIXED_HOLIDAYS +
        (
            (2, 28, _("228 Peace Memorial Day")),
            (4, 4, _("Combination of Women's Day and Children's Day")),
            (10, 10, _("National Day/Double Tenth Day")),
        )
    )
    include_chinese_new_year_eve = True
    include_chinese_second_day = True

    def get_variable_days(self, year):
        days = super(Taiwan, self).get_variable_days(year)
        # Qingming begins when the sun reaches the celestial
        # longitude of 15° (usually around April 4th or 5th)
        qingming = solar_term(year, 15, 'Asia/Taipei')

        days.extend([
            (
                ChineseNewYearCalendar.lunar(year, 1, 3),
                _("Chinese New Year (3rd day)")
            ),
            (qingming, _("Qingming Festival")),
            (ChineseNewYearCalendar.lunar(year, 5, 5),
             _("Dragon Boat Festival")),
            (ChineseNewYearCalendar.lunar(year, 8, 15),
             _("Mid-Autumn Festival")),
        ])
        return days
