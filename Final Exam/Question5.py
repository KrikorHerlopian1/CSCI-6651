#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


class Circle():
    def __init__(self,radius):
        self.radius = radius

    def compute_area(self):
        return 3.1416*(self.radius**2)


circle = Circle(10)
print(circle.compute_area())