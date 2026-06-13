import sys
import os

sys.path.append(os.path.abspath("."))

from src.services.diff.csharp_filter import CSharpFileFilter


class MockConfig:
    exclude_paths = []


def test_csharp_file_detection():
    filter_obj = CSharpFileFilter(MockConfig())

    assert filter_obj.should_review("LoginService.cs") is True


def test_non_csharp_file_detection():
    filter_obj = CSharpFileFilter(MockConfig())

    assert filter_obj.should_review("README.md") is False