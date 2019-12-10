Feature: Example of using Table as parameters

  Background:
    Given user opens webpage http://todomvc.com/examples/react/

  Scenario: Enter new todo-item and ensure it is added
    Given there are todo-items in the list
      | taskname             | completed |
      | Restructure my code  | true      |
      | Walk the dog         | false     |

    When there is todo-item 'Restructure my code' in the list
    And task 'Restructure my code' is completed
    And there is todo-item 'Walk the dog' in the list
    But task 'Walk the dog' is not completed

