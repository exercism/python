import unittest
import pytest
from enums import (
    LogLevel,
    LogLevelInt,
    parse_log_level,
    convert_to_short_log,
    get_warn_alias,
    get_members
)


class EnumsTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_parse_log_level_set_ing(self):
        self.assertIs(
            parse_log_level('[INF]: File deleted'),
            LogLevel.INFO,
            msg='The Log level is incorrect'
        )

    @pytest.mark.task(taskno=1)
    def test_parse_log_level_set_wrn(self):
        self.assertIs(
            parse_log_level('[WRN]: File is being overwritten'),
            LogLevel.WARNING,
            msg='The Log level is incorrect'
        )

    @pytest.mark.task(taskno=1)
    def test_parse_log_level_set_err(self):
        self.assertIs(
            parse_log_level('[ERR]: Some Random Log'),
            LogLevel.ERROR,
            msg='The Log level is incorrect'
        )

    @pytest.mark.task(taskno=2)
    def test_parse_log_level_set_xyz(self):
        self.assertIs(
            parse_log_level('[XYZ]: Some Random Log'),
            LogLevel.UNKNOWN,
            msg='The Log level is incorrect'
        )

    @pytest.mark.task(taskno=3)
    def test_convert_to_short_log_set1(self):
        self.assertEqual(
            convert_to_short_log(LogLevel.ERROR, 'Stack overflow'),
            '6:Stack overflow',
            msg='The converted short log is incorrect'
        )

    @pytest.mark.task(taskno=3)
    def test_convert_to_short_log_set2(self):
        self.assertEqual(
            convert_to_short_log(LogLevel.WARNING, 'This is a warning'),
            '5:This is a warning',
            msg='The converted short log is incorrect'
        )

    @pytest.mark.task(taskno=4)
    def test_get_warn_alias(self):
        self.assertIs(
            get_warn_alias(),
            LogLevel.WARN,
            msg='The warn alias returned is incorrect'
        )

    @pytest.mark.task(taskno=5)
    def test_get_members(self):
        self.assertListEqual(
            get_members(),
            [('TRACE', 'TRC'), ('DEBUG', 'DBG'), ('INFO', 'INF'),
                ('WARNING', 'WRN'), ('ERROR', 'ERR'), ('FATAL', 'FTL'), ('UNKNOWN', 'UKN')],
            msg='The Members list of the enum is incorrect'
        )
