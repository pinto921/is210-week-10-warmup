#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Adding keys task 3"""
import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED ['Van Halen']['David lee roth']

CORRECTED ['Van Halen']['Sammy Hagar'] = ['vocals']
