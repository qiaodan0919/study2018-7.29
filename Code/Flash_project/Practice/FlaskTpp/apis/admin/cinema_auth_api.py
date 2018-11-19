from flask_restful import fields, Resource, marshal, reqparse, abort

from apis.admin.utils import admin_user_login
from apis.api_constant import HTTP_OK
from models.cinema_admin.cinema_user_model import CinemaUser

cinema_user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "phone": fields.String,
    "password": fields.String(attribute="_password"),
    "is_verify": fields.Boolean
}

single_cinema_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(cinema_user_fields)
}

multi_cinema_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(cinema_user_fields))
}

class AdminCinemaUsersResource(Resource):

    @admin_user_login
    def get(self):
        cinema_users = CinemaUser.query.all()

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": cinema_users
        }

        return marshal(data, multi_cinema_user_fields)

parse = reqparse.RequestParser()
parse.add_argument("is_verify", type=bool, required=True, help="请提供操作")

class AdminCinemaUserResource(Resource):

    @admin_user_login
    def get(self):
        cinema_user = CinemaUser.query.get(id)

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": cinema_user
        }

        return marshal(data, single_cinema_user_fields)


    @admin_user_login
    def patch(self,id):
        args = parse.parse_args()

        is_verify = args.get("is_verify")

        cinema_user = CinemaUser.query.get(id)

        cinema_user.is_verify = is_verify

        if not cinema_user.save():
            abort(400, msg="change fail")

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": cinema_user
        }

        return marshal(data, single_cinema_user_fields)