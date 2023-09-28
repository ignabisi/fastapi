import json

import pytest


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries", data=json.dumps({"url": "https://myurl.com"})
    )

    assert response.status_code == 201
    assert response.json()["url"] == "https://myurl.com"


def test_create_summary_invalid_json(test_app):
    response = test_app.post("/summaries", data=json.dumps({}))

    assert response.status_code == 422, response.text
    assert response.json() == {
        "detail": [
            {
                "input": {},
                "loc": ["body", "url"],
                "msg": "Field required",
                "type": "missing",
                "url": "https://errors.pydantic.dev/2.4/v/missing",
            }
        ]
    }


def test_read_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://ignabisi.something"})
    )
    assert response.status_code == 201

    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"/summaries/{summary_id}")
    response_dict = response.json()

    assert response.status_code == 200
    assert response_dict["url"] == "https://ignabisi.something"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_wrong_id(test_app_with_db):
    response = test_app_with_db.get("/summaries/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_read_all_summaries(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://ignabisi.aaa"})
    )
    assert response.status_code == 201

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert all(
        list(
            filter(lambda d: d["url"].startswith("https://ignabisi.aaa"), response_list)
        )
    )
