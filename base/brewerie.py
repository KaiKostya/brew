from dataclasses import dataclass, field
from typing import Optional

import marshmallow.validate
import marshmallow_dataclass
from dataclasses_json import dataclass_json
from marshmallow import Schema
from dict_to_dataclass import DataclassFromDict

from tests.conftest import date_time_regex, phone_regex, url_regex, coords_regex, postal_regex


@dataclass_json
@dataclass
class Brewerie(Schema, DataclassFromDict):
    """class with auto validation properties"""
    id: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    name: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    brewery_type: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    street: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    address_2: Optional[str, None]
    address_3: Optional[str, None]
    city: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    state: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    county_province: Optional[str, None]
    postal_code: field(metadata={"validate": marshmallow.validate.Regexp(postal_regex)})
    country: str = field(metadata={"validate": marshmallow.validate.Length(min=2)})
    longitude: str = field(metadata={"validate": marshmallow.validate.Regexp(coords_regex)})
    latitude: str = field(metadata={"validate": marshmallow.validate.Regexp(coords_regex)})
    phone: str = field(metadata={"validate": marshmallow.validate.Regexp(phone_regex)})
    website_url: str = field(metadata={"validate": marshmallow.validate.Regexp(url_regex)})
    updated_at: str = field(metadata={"validate": marshmallow.validate.Regexp(date_time_regex)})
    created_at: str = field(metadata={"validate": marshmallow.validate.Regexp(date_time_regex)})


BrewerieSchema = marshmallow_dataclass.class_schema(Brewerie)
