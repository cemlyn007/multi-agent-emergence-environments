import os
import subprocess

import pytest

EXAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMINE_FILE_PATH = os.path.join(os.path.dirname(EXAMPLES_DIR), "bin", "examine.py")


class TestExamine:
    @pytest.mark.parametrize(['env'], [
        ("hide_and_seek_full.jsonnet",),
        ("hide_and_seek_quadrant.jsonnet",),
        ("blueprint.jsonnet",),
        ("lock_and_return.jsonnet",),
        ("sequential_lock.jsonnet",),
        ("shelter.jsonnet",),
    ])
    def test_examine_env(self, env):
        with pytest.raises(subprocess.TimeoutExpired):
            subprocess.check_call(["python", EXAMINE_FILE_PATH, os.path.join(EXAMPLES_DIR, env)], timeout=10)

    @pytest.mark.skip('Policy cannot be unpickled because: No module named \'gym.spaces.dict_space\'.')
    @pytest.mark.parametrize(['env', 'policy'], [
        ("hide_and_seek_full.jsonnet", "hide_and_seek_full.npz"),
        ("hide_and_seek_quadrant.jsonnet", "hide_and_seek_quadrant.npz"),
        ("blueprint.jsonnet", "blueprint.npz"),
        ("lock_and_return.jsonnet", "lock_and_return.npz"),
        ("sequential_lock.jsonnet", "sequential_lock.npz"),
        ("shelter.jsonnet", "shelter.npz"),
    ])
    def test_examine_policies(self, env, policy):
        with pytest.raises(subprocess.TimeoutExpired):
            subprocess.check_call(
                ["python", EXAMINE_FILE_PATH, os.path.join(EXAMPLES_DIR, env), os.path.join(EXAMPLES_DIR, policy)],
                timeout=15
            )
