On each api method that contains some json with fields we create dataclass.
Example:

class Brewerie(Schema):
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

We're setting type hint on each field and we can validate field on loading from json.
When we want to load some json into our dataclass with validation all fields we need to use created schema:

BrewerieSchema.load(our_json_to_load)

When we want to load some invalid json to dataclass without validation for send invalid data:

invalid_dataclass = AutoDeletePlan(**our_json_to_load)

and then we can convert that dataclass to dict for sending: 

asdict(invalid_dataclass)