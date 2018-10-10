import unittest.mock as mock
import pytest

from mlagents.trainers.demo_loader import load_demonstration, make_demo_buffer


def test_load_demo():
    brain_parameters, brain_infos, total_expected = load_demonstration('./tests/trainers/test.demo')
    assert (brain_parameters.brain_name == "Ball3DBrain")
    assert (brain_parameters.vector_observation_space_size == 8)
    assert (len(brain_infos) == total_expected)

    demo_buffer = make_demo_buffer(brain_infos, brain_parameters, 1)
    assert (len(demo_buffer.update_buffer['actions']) == total_expected - 1)