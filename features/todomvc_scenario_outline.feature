@templates
Feature: Example of Scenario Outline and Examples

  Background:
    Given user opens webpage http://todomvc.com/examples/react/

 Scenario Template: Enter new todo-item and ensure it is added
    Given there are no todo-item '<taskname>' in the list
    When user add task '<taskname>'
    Then there is todo-item '<taskname>' in the list
    And task '<taskname>' <state>

    Examples: simple tasks list
      | taskname        | state                 |
      | Outline Task 1  | is not completed      |
      | Outline Task 2  | is not completed      |
