from http import HTTPStatus
from typing import List

from kentik_api.api_calls import users
from kentik_api.api_resources.base_api import BaseAPI
from kentik_api.public.user import User
from kentik_api.requests_payload import users_payload


class UsersAPI(BaseAPI):
    """Exposes Kentik API operations related to users. """

    def get_all(self) -> List[User]:
        api_call = users.get_users()
        response = self.send(api_call)
        return users_payload.GetAllResponse.from_json(response.text).to_users()

    def get(self, user_id: int) -> User:
        api_call = users.get_user_info(user_id)
        response = self.send(api_call)
        return users_payload.GetResponse.from_json(response.text).to_user()

    def create(self, user: User) -> User:
        # Checking if required data is provided
        assert user.email is not None, "User email has to be provided"
        assert user.role is not None, "User role has to be provided"
        assert user.email_service is not None, "Email service has to be provided"
        assert user.email_product is not None, "Email product has to be provided"

        api_call = users.create_user()
        payload = users_payload.CreateRequest(
            user_name=user.username,
            user_full_name=user.full_name,
            user_email=user.email,
            user_password=user.password,
            role=user.role,
            email_service=user.email_service,
            email_product=user.email_product,
        )
        response = self.send(api_call, payload)
        return users_payload.CreateResponse.from_json(response.text).to_user()

    def update(self, user: User) -> User:
        assert user.id is not None, "User ID has to be provided"

        api_call = users.update_user(user.id)
        payload = users_payload.UpdateRequest(
            user_name=user.username,
            user_full_name=user.full_name,
            user_email=user.email,
            role=user.role,
            email_service=user.email_service,
            email_product=user.email_product,
        )
        response = self.send(api_call, payload)
        return users_payload.UpdateResponse.from_json(response.text).to_user()

    def delete(self, user_id: int) -> bool:
        api_call = users.delete_user(user_id)
        response = self.send(api_call)
        return response.http_status_code == HTTPStatus.NO_CONTENT
