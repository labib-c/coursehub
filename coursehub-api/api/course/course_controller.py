from flask import Blueprint, jsonify, request
import re

from api.auth import get_user_with_request
from api.course.course_manager import CourseManager

course_controller_bp = Blueprint("course_controller", __name__)


@course_controller_bp.route("/search_course", methods=["GET"])
def search_for_course():
    """
    :return: array of JSON dict of all matching courses
    """
    course_code = request.args.get("searchQuery")

    if course_code == "" or len(course_code) < 4 or not re.compile("^[A-Za-z]{3,4}[0-9]+$").match(course_code):
        return jsonify({"error": "No matching courses found for '" + course_code + "'"})

    courses = CourseManager.get_courses_by_code(course_code)

    if courses is None:
        return jsonify({"error": "No matching courses found for '" + course_code + "'"})

    return jsonify({"matching_courses": courses})


@course_controller_bp.route("/get_course_data", methods=["GET"])
def get_course_data():
    """
    :return: course by ID
    """
    id_ = request.args.get("courseId")

    return jsonify(CourseManager.get_course_by_id(id_).__dict__)


@course_controller_bp.route("/add_course_ratings", methods=["PUT"])
def update_rating():
    """
    :return: course object with updated rating
    """
    user = get_user_with_request(request)
    payload = request.get_json()

    workload = payload["workloadRating"]  # must be either 'workload' or 'recommendation'
    recommendation = payload["recommendationRating"]
    course_id = payload["courseId"]
    user_id = user.id

    rating_dict = {"workload_rating": workload, "recommendation_rating": recommendation}

    course = CourseManager.get_course_by_id(course_id)

    if CourseManager.did_user_already_rate_course(user_id, course_id):
        prev_ratings = CourseManager.get_prev_ratings(user_id, course_id)
        CourseManager.update_course_rating(course, prev_ratings, "remove")
        CourseManager.update_user_course_ratings(user_id, course_id, rating_dict)

    else:
        CourseManager.insert_course_rating(user_id, course_id, rating_dict)

    course = CourseManager.get_course_by_id(course_id)

    new_course = CourseManager.update_course_rating(course, rating_dict, "add")

    ratings = dict()
    ratings["overall_rating"] = new_course.overall_rating
    ratings["workload_rating"] = new_course.ratings["workload_rating"]
    ratings["recommendation_rating"] = new_course.ratings["recommendation_rating"]

    return jsonify(ratings)
