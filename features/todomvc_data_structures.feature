@wip
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

  Scenario: Enter also more todo-items using json
    Given there are todo-items loaded from json
    """
    [{"taskname": "Task 1 From Json", "completed": false}, {"taskname": "Task 2 From Json", "completed": true}]
    """

    When there is todo-item 'Task 1 From Json' in the list
    But task 'Task 1 From Json' is not completed
    And there is todo-item 'Task 2 From Json' in the list
    And task 'Task 2 From Json' is completed

