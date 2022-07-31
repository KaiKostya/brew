import allure
from assertpy import assert_that

from base.brewerie import BrewerieSchema


@allure.feature("Positive Random Brewerie")
@allure.story("Check API request Random Brewerie")
class TestRandomBrewerie:
    command = "random"

    def test_get_brewerie(self, request_brewerie):
        response = request_brewerie
        with allure.step("Get random brewerie request"):
            assert_that(response).is_not_none()
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()).is_not_empty()
            assert_that(BrewerieSchema(response.json())).is_type_of(list)
            assert_that(BrewerieSchema(response.json())).is_length(1)


@allure.feature("Negative Random Brewerie")
@allure.story("Check API request Random Brewerie per_page=0")
class TestNegativeRandomBrewerie:
    command = "random"
    params = "per_page=0"

    def test_get_brewerie(self, request_brewerie):
        response = request_brewerie
        with allure.step("Get random brewerie request with param per_page=0"):
            assert_that(response).is_not_none()
            assert_that(response.status_code).is_equal_to(200)
            assert_that(BrewerieSchema(response.json())).is_type_of(list)
            assert_that(BrewerieSchema(response.json())).is_empty()

