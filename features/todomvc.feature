Feature: As a lazy developer I want to test todomvc.com automatically

  Background:
    Given user opens webpage http://todomvc.com/examples/react/

  @core
  Scenario: Enter new todo-item and ensure it is added
    Given there are no todo-item 'My first task' in the list
    # comment: we can comment our feature files
    When user add task 'My first task'
    Then there is todo-item 'My first task' in the list
    And task 'My first task' is not completed

  Scenario: user creates new item and mark it as complited
    Given user add task 'To complete'
    When click checkbox for task 'To complete'
    Then task 'To complete' is completed
