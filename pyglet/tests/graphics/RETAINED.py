#!/usr/bin/env python
"""Tests vertex list drawing.
"""
import unittest

import pyglet

from graphics_common import GraphicsGenericTestCase, get_feedback, GL_TRIANGLES

__noninteractive = True


class GraphicsVertexListTestCase(GraphicsGenericTestCase, unittest.TestCase):
    def get_feedback(self, data):
        vertex_list = pyglet.graphics.vertex_list(self.n_vertices, *data)
        return get_feedback(lambda: vertex_list.draw(GL_TRIANGLES))

if __name__ == '__main__':
    unittest.main()
