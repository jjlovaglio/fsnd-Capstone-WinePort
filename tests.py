from os import environ as env
import unittest
import json
from run import app, generate_auth_url, setup_db
from flask_sqlalchemy import SQLAlchemy

class WinePortTestCase(unittest.TestCase):
    """This class represents the WinePort test case.
       in order to run it, the psql testing database, environment
       variables and db_populate.py (database seeding) 
       need to be setup correctly as per README.md 
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.token1 = env["USER_1_TOKEN"]
        self.token2 = env["USER_2_TOKEN"]
        self.app = app
        self.client = self.app.test_client
        self.database_path = env["TEST_DATABASE_URL"]
        setup_db(self.app, self.database_path)
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass



    # begin RBAC tests
    def test_Winemaker_Role_succeeds_accessing_create_wine_form(self):
        """ Token 2 is authorized to access the create_wine_form: Http 200
        """
        headers = {
            "Authorization": self.token2
        }
        res = self.client().get('/wines/create', headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_Winemaker_Role_fails_to_create_a_winery_403(self):
        """ Token 2 is unauthorized to create a winery. Error 403, permission not found
        """
        headers = {
            "Authorization": self.token2
        }
        res = self.client().get('/wineries/create', headers=headers)
        self.assertEqual(res.status_code, 403)

    def test_Manager_Role_fails_to_have_a_header_401(self):
        """ Token 1 doesn't have a header token: HTTP 401 authorization header is expected
        """
        res = self.client().get('/wineries/create')
        # print(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 401)

    def test_Manager_Role_has_all_permissions(self):
        """ If token 1 is current, assert success 200
        """
        headers = {
            "Authorization": self.token1
        }
        res = self.client().get('/wines/create', headers=headers)
        self.assertEqual(res.status_code, 200)
    # end RBAC tests
    def test_index_success_200(self):
        """Test index endpoint for success"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_index_failure_error_405(self):
        """ Test index for failure by sending a post request"""
        res = self.client().post('/')
        self.assertEqual(res.status_code,405)

    def test_wineries_success_200(self):
        res = self.client().get('/wineries')
        self.assertIn(b'Tupungato, Mendoza', res.data)

    def test_wineries_failure_405(self):
        res = self.client().post('/wineries')
        self.assertEqual(res.status_code, 405)

    def test_search_wineries_success_200(self):
        res = self.client().post('/wineries/search')
        self.assertIn(b'Vaglio Wines', res.data)

    def test_search_wineries_failure_405(self):
        res = self.client().get('/wineries/search')
        self.assertEqual(res.status_code, 405)

    def test_show_winery_success_200(self):
        res = self.client().get('/wineries/1')
        self.assertEqual(res.status_code, 200)

    def test_show_winery_failure_405(self):
        res = self.client().post('/wineries/1')
        self.assertEqual(res.status_code,405)

    def test_create_winery_success_200(self):
        headers = {
            "Authorization": self.token1
        }
        res = self.client().get('/wineries/create', headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_create_winery_submission_success_200(self):
        pass

    def test_create_winery_submission_failure(self):
        pass

    def test_delete_winery_success_200(self):
        pass

    def test_delete_winery_failure(self):
        pass

    def test_winemakers_success_200(self):
        pass

    def test_winemakers_failure_405(self):
        pass

    def test_search_winemakers_success_200(self):
        pass

    def test_search_winemakers_failure_405(self):
        pass

    def test_show_winemaker_success_200(self):
        pass

    def test_show_winemaker_failure_405(self):
        pass

    def test_create_winemaker_form_success_200(self):
        pass

    def test_create_winemaker_form_failure(self):
        pass

    def test_create_winemaker_submission_success_200(self):
        pass

    def test_create_winemaker_submission_failure(self):
        pass

    def test_wines_success_200(self):
        pass

    def test_wines_failure(self):
        pass

    def test_create_wines_success_200(self):
        pass

    def test_create_wines_failure(self):
        pass

    def test_create_show_submission_success_200(self):
        pass

    def test_crate_show_submission_failure(self):
        pass

    def edit_winemaker_success_200(self):
        pass

    def edit_winemaker_failure(self):
        pass

    def edit_winemaker_submission_success_200(self):
        pass

    def edit_winemaker_submission_failure(self):
        pass

    def edit_winery_success_200(self):
        pass

    def edit_winery_failure(self):
        pass

    def edit_winery_submission_success(self):
        pass

    def edit_winery_submission_failure(self):
        pass

    # 38 tests!

# make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()