import allure
import pytest
from assertpy import assert_that

from base.base_request import BaseRequest
from base.brewerie import BrewerieSchema


@allure.feature("Positive Search Brewerie")
@allure.story("Check API request Search Brewerie")
class TestSearchBreweries:

    @pytest.mark.parametrize("_word", ["dog", "czech"])
    def test_get_breweries_list(self, _word):
        response = BaseRequest.get("search", f"query={_word}&per_page=3")
        with allure.step(f"search brewerie by word: {_word}"):
            assert_that(response).is_not_none()
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.json()).is_type_of(list)
            assert_that(response.json()).is_not_empty()
            assert_that(response.json()).is_length(3)
            for _brew in response.json():
                assert_that(BrewerieSchema(_brew).id).contains(_word)
                assert_that(BrewerieSchema(_brew).name).contains(_word.capitalize())


@allure.feature("Negative Search Brewerie")
@allure.story("Check API request Search Brewerieby non-existent word")
class TestNonExistSearchBreweries:
    """response depends on business requirements. Assume that in this case response should be 404"""

    def test_get_non_exist_brewerie(self):
        response = BaseRequest.get("search", "query=non_exist&per_page=3")
        with allure.step("search brewerie by non-existent word: non_exist"):
            assert_that(response.status_code).is_equal_to(404)
