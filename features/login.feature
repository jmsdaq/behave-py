Feature: Login functionality

Scenario: User logs in with valid credentials
  Given I open the login page
  When I enter "standard_user" and "secret_sauce" as credentials
  Then I should be redirected to the inventory page

Feature: Add item to cart

Scenario: User adds an item to the cart
  Given I am logged in
  When I add an item to the cart
  Then the item should appear in the cart
