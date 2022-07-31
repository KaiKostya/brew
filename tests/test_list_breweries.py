import allure
import pytest
from assertpy import assert_that

from base.brewerie import BrewerieSchema


@allure.feature("Positive Breweries list by city")
@allure.story("Check API request Breweries list by city")
class TestListBreweriesByCity:

    @pytest.fixture(scope="class", autouse=True)
    def set_params(self, get_city):
        self.requested_city = get_city
        TestListBreweriesByCity.params = f"by_city={get_city}&per_page=3"
        yield

    def test_get_breweries_list(self, request_brewerie):
        response = request_brewerie
        with allure.step(f"get breweries list by city {self.requested_city}"):
            assert_that(response).is_not_none()
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()).is_type_of(list)
            assert_that(response.json()).is_not_empty()
            assert_that(response.json()).is_length(3)
            for _brew in response.json():
                assert_that(BrewerieSchema(_brew).city).is_equal_to(self.requested_city)


@allure.feature("Negative Breweries list")
@allure.story("Check API request Breweries list by non-existent city")
class TestNonExistCityListBreweries:
    """response depends on business requirements. Assume that in this case response should be 404"""

    params = f"by_city=kash&per_page=3"

    def test_get_non_exist_brewerie(self, request_brewerie):
        with allure.step("Get breweries list by non-existent city kash"):
            assert_that(request_brewerie.status_code).is_equal_to(404)


@allure.feature("Positive Breweries list by type")
@allure.story("Check API request Breweries list by type")
class TestListBreweriesByType:

    @pytest.fixture(scope="class", autouse=True)
    def set_params(self, get_type):
        self.requested_type = get_type
        TestListBreweriesByType.params = f"by_type={get_type}&per_page=3"
        yield

    def test_get_breweries_list(self, request_brewerie):
        response = request_brewerie
        with allure.step(f"Get breweries list by type: {self.requested_type}"):
            assert_that(response).is_not_none()
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()).is_type_of(list)
            assert_that(response.json()).is_not_empty()
            assert_that(response.json()).is_length(3)
            for _brew in response.json():
                assert_that(BrewerieSchema(_brew).type).is_equal_to(self.requested_type)


@allure.feature("Negative Breweries list by type")
@allure.story("Check API request Breweries list by non-existent type")
class TestNonExistTypeListBreweries:
    """response depends on business requirements. Assume that in this case response should be 404"""
    params = f"by_type=not_exist&per_page=3"

    def test_get_non_exist_brewerie(self, request_brewerie):
        with allure.step("Get breweries list by non-existent type: not_exist"):
            assert_that(request_brewerie.status_code).is_equal_to(404)