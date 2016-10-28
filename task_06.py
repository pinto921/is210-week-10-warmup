#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 05"""
""" complete the code"""


import data

SUPER_SIDEKICKS = {}
for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    SUPER_SIDEKICKS[HERO] = #complete this line
    SUPER_SIDEKICKS[HERO] = HERO_DATA.get('pet')
