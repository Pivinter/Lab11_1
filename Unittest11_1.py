import unittest

from Lab11_1 import add_term, find_term, load_from_file, remove_term, save_to_file, sort_terms, validate_filename, validate_menu_choice

class TestTermsMethods(unittest.TestCase):
    def test_add_term(self):
        terms_list = []
        add_term(terms_list, "term1", "explanation1")
        self.assertEqual(terms_list, [{"term": "term1", "explanation": "explanation1"}])

    def test_remove_term(self):
        terms_list = [{"term": "term1", "explanation": "explanation1"}]
        remove_term(terms_list, "term1")
        self.assertEqual(terms_list, [])

    def test_find_term(self):
        terms_list = [{"term": "term1", "explanation": "explanation1"}]
        explanation = find_term(terms_list, "term1")
        self.assertEqual(explanation, "explanation1")

    def test_sort_terms(self):
        terms_list = [{"term": "term2", "explanation": "explanation2"}, {"term": "term1", "explanation": "explanation1"}]
        sorted_terms = sort_terms(terms_list)
        self.assertEqual(sorted_terms, [{"term": "term1", "explanation": "explanation1"}, {"term": "term2", "explanation": "explanation2"}])

    def test_validate_menu_choice(self):
        self.assertTrue(validate_menu_choice("1"))
        self.assertFalse(validate_menu_choice("0"))
        self.assertFalse(validate_menu_choice("9"))

    def test_validate_filename(self):
        self.assertTrue(validate_filename("testfile.txt"))
        self.assertFalse(validate_filename(""))

if __name__ == "__main__":
    unittest.main()