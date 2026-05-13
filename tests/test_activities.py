import pytest

def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activities = ["Chess Club", "Programming Class", "Gym Class"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 3
    assert set(data.keys()) == set(expected_activities)

def test_get_activities_includes_required_fields(client):
    # Arrange
    required_fields = ["description", "schedule", "max_participants", "participants"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    for activity_name, activity_data in data.items():
        for field in required_fields:
            assert field in activity_data, f"Missing {field} in {activity_name}"

def test_get_activities_participants_are_lists(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    for activity_name, activity_data in data.items():
        assert isinstance(activity_data["participants"], list), f"Participants not list in {activity_name}"