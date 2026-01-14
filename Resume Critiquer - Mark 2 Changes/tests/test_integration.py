"""
Integration tests for Resume Critiquer application.
Tests the complete application flow.
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src import config, validators
from src.utils import cleanup

print("=" * 60)
print("Integration Tests for Resume Critiquer")
print("=" * 60)

# Test 1: Config module
print("\n[TEST 1] Testing configuration...")
try:
    print(f"✓ Config module imported")
    print(f"  - DB Path: {config.DB_PATH}")
    print(f"  - Max file size: {config.MAX_FILE_SIZE_MB}MB")
    print(f"  - Max files per batch: {config.MAX_FILES_PER_BATCH}")
except Exception as e:
    print(f"✗ Config test FAILED: {e}")
    sys.exit(1)

# Test 2: Validators module
print("\n[TEST 2] Testing validators...")
try:
    # Test chunk validation
    is_valid, error = validators.validate_chunk_params(3000, 200)
    assert is_valid, f"Valid params rejected: {error}"
    print(f"✓ Chunk validation works")

    # Test filename sanitization
    safe = validators.sanitize_filename("../../bad/path.pdf")
    assert "/" not in safe and "\\" not in safe
    print(f"✓ Filename sanitization works: '{safe}'")
except Exception as e:
    print(f"✗ Validators test FAILED: {e}")
    sys.exit(1)

# Test 3: Cleanup utils
print("\n[TEST 3] Testing cleanup utilities...")
try:
    summary = cleanup.get_export_summary()
    print(f"✓ Export summary works")
    print(f"  - Total files: {summary['total_files']}")
    print(f"  - Total size: {summary['total_size_mb']:.2f} MB")

    db_size = cleanup.get_database_size()
    print(f"✓ Database size check works: {db_size:.2f} MB")
except Exception as e:
    print(f"✗ Cleanup utils test FAILED: {e}")
    sys.exit(1)

# All tests passed
print("\n" + "=" * 60)
print("✓✓✓ ALL INTEGRATION TESTS PASSED! ✓✓✓")
print("=" * 60)
print("\nThe application is ready to run!")
print("Start with: python run.py")
