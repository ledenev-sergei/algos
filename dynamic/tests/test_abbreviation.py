import pytest

from dynamic.abbreviation import abbreviation


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("daBcd", "ABC", "YES"),
        ("AbcE", "AFDE", "NO"),  # missed letter from b
        ("KXzQ", "K", "NO"),  # contains upper letter not in b
        ("LLZOSYAMQRMBTZXTQMQcKGLR", "LLZOSYAMBTZXMQKLR", "NO"),
        ("MGYXKOVSMAHKOLAZZKWXKS", "MGXKOVSAHKOLZKKDP", "NO"),
        ("VLKHNlpsrlrvfxftslslrrh", "VLKHN", "YES"),
        ("OQSVONTNZMDJAVRZAZCVPKh", "OSVONTNZMDJAVRZAZCVPK", "NO"),
        ("AXbosoh", "AX", "YES"),
        ("EYONDOCHNZYYlBZXPGzX", "EYONDOCHNZYYBZXPGXOG", "NO"),
        ("BJAFXKGENMFUvdsvcptrp", "BJAFXKGENMFU", "YES"),
        ("UBUFOOSIXXsdtfmeyongkhehq", "UBUFOOSIXX", "YES"),
        ("PWBIJLCOIAXGJGUXUZOutgic", "PWBIJLCOIAXGJGUXUZO", "YES"),
        ("EOWZEOHWYOJTBNMcefdsp", "EOWZEOHWYOJTBNM", "YES"),
        ("QOTLYiFECLAGIEWRQMWPSMWIOQSEBEOAuhuvo", "QOTLYFECLAGIEWRQMWPSMWIOQSEBEOA", "YES"),
        ("BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms",
         "BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF", "YES")
    ],
)
def test_abbreviation(a: str, b: str, expected):
    # given
    # when
    result = abbreviation(a, b)
    # then
    assert result == expected

def test_abbreviation_from_file():
    with open("test_abbreviation_input.txt") as data:
        data_lines = data.readlines()
        del data_lines[0]

    with open("test_abbreviation_expected.txt") as expected:
        expected_lines = expected.readlines()

    for i in range(0, len(expected_lines)):
        # given
        a = data_lines[i*2].strip()
        b = data_lines[i*2+1].strip()

        # when
        result = abbreviation(a, b)

        # then
        expected = expected_lines[i].strip()
        if result != expected:
            assert result == expected
        assert result == expected