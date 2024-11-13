Feature: Login functionality

Scenario: User logs in with valid credentials
  Given I open the login page
  When I enter "standard_user" and "secret_sauce" as credentials
  Then I should be redirected to the inventory page
