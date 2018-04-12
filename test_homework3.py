import unittest
from homework3 import create_dataframe  # not good generally for namespace reasons but ok for one method here

class TestCreateDataFrameMethods(unittest.TestCase):

    def setUp(self):
        # let tests assume a df created with a correct path
        self.df = create_dataframe('../HW1-aenfield/class.db')
        
    def test_df_has_only_correct_column_names(self):
        # contains only the columns video_id, category_id, language
        expected_columns = ['video_id','category_id','language']
        for colname in expected_columns:
            self.assertIn(colname, self.df.columns)
        # also need to confirm there's only three columns, for the 'only' part
        self.assertEqual(3, len(self.df.columns))
       
    def test_df_has_at_least_10_rows(self):
        self.assertTrue(len(self.df) >= 10)

    def test_df_vals_are_not_a_key(self):
        # I'm going to test that the specified values are _not_ a key, since
        # I know that they're not a key, and I want these tests to pass
        self.assertNotEqual(len(self.df), len(self.df.groupby(['video_id','language']).size()))

    def test_invalid_path_raises(self):
        with self.assertRaises(ValueError):
            create_dataframe('abadpath')
            

if __name__ == '__main__':
    unittest.main()
