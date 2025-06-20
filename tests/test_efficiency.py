#!/usr/bin/env python3
"""
Simple verification script to test the efficiency improvements.
"""

import time
import sys
from urllib.parse import urlparse


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
            return True

        except Exception as e:
            print(f"❌ Fetch failed: {e}")
            return False

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


if __name__ == "__main__":
    print("=== Efficiency Test Script ===")
    success = test_fetch_function()

    if success:
        print("\n✅ All efficiency tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)
