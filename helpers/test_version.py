import re
from unittest import TestCase

from .version import get_project_version

# https://github.com/semver/semver/issues/232
semver_re = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)" \
            r"(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*)?(\+[0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*)?$"


class TestGetProjectVersion(TestCase):
    def test_get_project_version(self):
        v = get_project_version()
        self.assertTrue(
            re.match(semver_re, v)
        )
