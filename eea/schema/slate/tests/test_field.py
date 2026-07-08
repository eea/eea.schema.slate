"""Tests for SlateJSONField."""

import json
import unittest

from eea.schema.slate.field import SlateJSONField, ISlateJSONField, DEFAULT_JSON_SCHEMA


class TestSlateJSONField(unittest.TestCase):
    """Test SlateJSONField."""

    def setUp(self):
        self.field = SlateJSONField(title="Contact")

    def test_default_schema(self):
        """Test that default schema is a JSON array."""
        schema = json.loads(DEFAULT_JSON_SCHEMA)
        self.assertEqual(schema, {"type": "array", "items": {}})

    def test_from_unicode_simple_list(self):
        """Test fromUnicode with a simple JSON list."""
        result = self.field.fromUnicode("[1, 2, 3]")
        self.assertEqual(result, [1, 2, 3])

    def test_from_unicode_json_object(self):
        """Test fromUnicode with JSON booleans and null."""
        result = self.field.fromUnicode("[true, false, null]")
        self.assertEqual(result, [True, False, None])

    def test_from_unicode_python_list_string(self):
        """Test fromUnicode with a Python list stored as string."""
        result = self.field.fromUnicode("[True, False, None]")
        self.assertEqual(result, [True, False, None])

    def test_from_unicode_nested_list(self):
        """Test fromUnicode with nested lists."""
        result = self.field.fromUnicode("[[1, 2], [3, 4]]")
        self.assertEqual(result, [[1, 2], [3, 4]])

    def test_from_unicode_empty_list(self):
        """Test fromUnicode with empty list."""
        result = self.field.fromUnicode("[]")
        self.assertEqual(result, [])

    def test_from_unicode_dict_in_list(self):
        """Test fromUnicode with dict objects in list."""
        result = self.field.fromUnicode('[{"key": "value"}]')
        self.assertEqual(result, [{"key": "value"}])

    def test_from_unicode_string_elements(self):
        """Test fromUnicode with string elements."""
        result = self.field.fromUnicode('["hello", "world"]')
        self.assertEqual(result, ["hello", "world"])

    def test_field_title(self):
        """Test that field title is set."""
        self.assertEqual(self.field.title, "Contact")

    def test_custom_schema(self):
        """Test creating field with custom schema."""
        custom_schema = json.dumps({"type": "array", "items": {"type": "string"}})
        field = SlateJSONField(schema=custom_schema, title="Custom")
        self.assertEqual(field.title, "Custom")

    def test_widget_default_none(self):
        """Test that widget defaults to None."""
        self.assertIsNone(self.field.widget)

    def test_custom_widget(self):
        """Test creating field with custom widget."""
        field = SlateJSONField(widget="slate", title="Custom")
        self.assertEqual(field.widget, "slate")

    def test_implements_islatejsonfield(self):
        """Test that field implements ISlateJSONField."""
        self.assertTrue(ISlateJSONField.providedBy(self.field))


def test_suite():
    """Test suite."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
