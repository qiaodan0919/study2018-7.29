from flask_restful import reqparse, fields, Resource, abort, marshal
from App.ext import cache
from App.utils import generate_movie_user_token
from apis.api_constant import USER_ACTION_REGISTER, HTTP_CREATE_OK, USER_ACTION_LOGIN, HTTP_OK
from apis.movie_user.model_utils import get_movie_user
from models.movie_user import MovieUser


parse_base = reqparse.RequestParser()
parse_base.add_argument('password', type=str, required=True, help='请输入密码')
parse_base.add_argument('action', type=str, required=True, help='请确认请求参数')

parse_register = parse_base.copy()
parse_register.add_argument('username', type=str, required=True, help='请输入用户名')
parse_register.add_argument('phone', type=str, required=True, help='请输入手机号码')

parse_login = parse_base.copy()
parse_login.add_argument("username", type=str, help="请输入用户名")
parse_login.add_argument("phone", type=str, help="请输入手机号码")

movie_user_fields = {
    'username': fields.String,
    'phone': fields.String,
    'password': fields.String(attribute="_password"),
}

single_movie_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(movie_user_fields)
}


class MovieUsersResource(Resource):

    def post(self):
        args = parse_base.parse_args()
        password = args.get('password')
        print(password)
        action = args.get('action').lower()
        print(action)

        if action == USER_ACTION_REGISTER:
            args_register = parse_register.parse_args()
            phone = args_register.get('phone')
            username = args_register.get('username')

            movie_user = MovieUser()

            movie_user.username = username
            movie_user.password = password
            movie_user.phone = phone

            if not movie_user.save():
                abort(400, msg="create fail")

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "用户创建成功",
                "data": movie_user
            }

            return marshal(data, single_movie_user_fields)

        elif action == USER_ACTION_LOGIN:

            args_login = parse_login.parse_args()

            username = args_login.get("username")
            phone = args_login.get("phone")

            user = get_movie_user(username) or get_movie_user(phone)

            if not user:
                abort(400, msg="用户不存在")

            if not user.check_password(password):
                abort(401, msg="密码错误")

            if user.is_delete:
                abort(401, msg="用户不存在")

            token = generate_movie_user_token()

            cache.set(token, user.id, timeout=60*60*24*7)

            data = {
                "msg": "login success",
                "status": HTTP_OK,
                "token": token
            }

            return data

        else:
            abort(400, msg="其提供正确的参数")