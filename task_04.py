#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" task 04 dictionaries"""

import data

data.BANDS['Buckingham Nick'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                              'Stevie Nicks': ['vocals', 'tambourine']}
data.BANDS['fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])

