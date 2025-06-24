#!/usr/bin/env python3
"""
Simple verification script to test the efficiency improvements.
"""

import time
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_fetch_function():
    """Test the new fetch_with_fallback function"""
    try:
        sys.argv = ["test_efficiency.py", "https://example.com"]
        from python_tools.scrape import fetch_with_fallback

        test_url = "https://httpbin.org/get"
        parsed = urlparse(test_url)

        print(f"Testing fetch_with_fallback with: {test_url}")
        start_time = time.time()

        try:
            response, used_proxy = fetch_with_fallback(test_url, parsed)
            end_time = time.time()

            print(f"✅ Fetch completed in {end_time - start_time:.2f}s")
            print(f"   Used proxy: {used_proxy}")
            print(f"   Response length: {len(response)} characters")

            assert isinstance(response, str) and response

        except Exception as e:
            print(f"❌ Fetch failed: {e}")
            assert False

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        assert False


if __name__ == "__main__":
    print("=== Efficiency Test Script ===")
    try:
        test_fetch_function()
    except AssertionError:
        print("\n❌ Some tests failed!")
        sys.exit(1)
    else:
        print("\n✅ All efficiency tests passed!")
        sys.exit(0)
