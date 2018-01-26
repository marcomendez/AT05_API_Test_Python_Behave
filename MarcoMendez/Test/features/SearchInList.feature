Feature: search the prices
  Scenario Outline: Simulate a search of a total priced for a list clients
    Given I go to search Total priced
    When  I put the "<ClientName>"
      And I put "<UserId>"
    Then  I get this total priced "<TotalPrice>"
    Examples:
      |ClientName  | UserId| TotalPrice|
      | Marco      | 001   |   200     |
      | Marco      | 001   |   200     |
      | Franco     | 003   |   400     |

  Scenario: Verify a Client exist previously created
    Given I go to search to the Client Marco
    When I put the ClientName Marco
    Then I should have a message that say "Exist client"