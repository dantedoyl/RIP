# Created by makst at 27.11.2020
Feature: Cook
  Test Cook

  Scenario: Create new Cook
    Given I want to create Cook named Cooker
    When I create it
    Then I expect that his name will be Cooker