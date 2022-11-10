import pytest

from sorting.fraudulent_activity_notifications import activityNotifications

@pytest.mark.parametrize(
    "expenditure,d,expected",
    [
        ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2),
        ([10, 20, 30, 40, 50], 3, 1)
    ],
)
def test_activity_notifications(expenditure, d, expected):
    # given

    # when
    result = activityNotifications(expenditure, d)

    # then
    assert expected == result


def test_activity_notifications_from_file():
    # given
    with open("test_fraudulent_activity_notifications.txt", "r") as f:
        elements_count, d = f.readline().rstrip().split()
        expenditure = list(map(int, f.readline().rstrip().split()))

    # when
    result = activityNotifications(expenditure, int(d))

    # then
    assert result == 633