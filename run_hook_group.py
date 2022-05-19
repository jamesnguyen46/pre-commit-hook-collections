import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))

GROUP_MAPPING = {
    "common": "common/comgrp_hook.yaml",
    "python": "python/pygrp_hook.yaml",
}


def hook_group_selector(group: str):
    cfg = os.path.join(HERE, GROUP_MAPPING[group])
    cmd = ["pre-commit", "run", "--config", cfg, "--files"] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    raise SystemExit()
