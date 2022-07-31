from assertpy import assert_that

from base.brewerie import BrewerieSchema
import allure


@allure.feature("Positive Single Brewerie")
@allure.story("Check API request Single Brewerie")
class TestSingleBrewerie:
    command = "madtree-brewing-cincinnati"

    def test_get_brewerie(self, request_brewerie):
        response = request_brewerie
        with allure.step(f"Sending request GET Brewerie by id {TestSingleBrewerie.command}"):
            assert_that(response).is_not_none()
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()).is_not_empty()
            assert_that(BrewerieSchema(response.json()).id).is_equal_to(TestSingleBrewerie.command)


@allure.feature("Negative Single Brewerie")
@allure.story("Check negative API request Single Brewerie")
class TestNonExistBrewerie:
    command = "madtree-brewing-cincinnati_non_exist"

    def test_get_non_exist_brewerie(self, request_brewerie):
        with allure.step(f"Sending request GET Brewerie by non-existent id {TestSingleBrewerie.command}"):
            assert_that(request_brewerie.status_code).is_equal_to(404)
