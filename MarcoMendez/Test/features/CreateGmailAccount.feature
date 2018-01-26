Feature: only letters and underscore
  Scenario: this scenario only allow letters ad underscore
    Given I go to create a new gmail account
       And I put name Marco and last Mendez
       And I put my username mmendez
       And I put my Password MM77863*mm@1564
       And I put my the self password MM77863*mm@
       And I put my day brithday Day 15 Month May Year 2018
       And I choose Genler Other
       And I put my Phono +59177884621345
       And I put my current email address marticus123@gmail.com
       And I my Location Bolivia
    When I press the Button Next step
    Then It should me to a page for notifacy me that my new account was created
