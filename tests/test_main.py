import importlib
from unittest.mock import patch


class TestMainModule:
    def test_calls_sys_exit_with_main_return_value(self):
        with patch('open_meeting.cli.main', return_value=0), \
             patch('sys.exit') as mock_exit:
            import open_meeting.__main__  # noqa: F401
            importlib.reload(open_meeting.__main__)
        mock_exit.assert_called_with(0)

    def test_propagates_nonzero_exit_code(self):
        with patch('open_meeting.cli.main', return_value=1), \
             patch('sys.exit') as mock_exit:
            import open_meeting.__main__
            importlib.reload(open_meeting.__main__)
        mock_exit.assert_called_with(1)
