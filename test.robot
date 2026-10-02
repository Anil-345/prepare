*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
test case
   Open Browser    https://wbscc.wb.gov.in/Applicant_Registration    Chrome
   Maximize Browser Window
   Sleep    2s

   Input Text    first_name    Anil
   Sleep    1s
   Input Text    middle_name    kumar
   Sleep    1s
   Input Text    last_name    gorla
   Sleep    1s

   Select From List By Value    sex    MQ==
   Sleep    1s

   Input Text    aadhaar_no    123456789123
   Sleep    1s

   Select From List By Value    programme_id    Mg==
   Sleep    1s

   Click Element    select2-course_id-container
   Sleep    1s

   Click Element    //span[@id="select2-course_id-container"]
   Sleep    1s

   Select From List By Value    inst_state_id    Mg==
   Sleep    1s
   
   Select From List By Value    inst_dist_id    MTY=
   Sleep    1s

   Select From List By Value    select2-inst_id-result-w4nw-MTM0Nzc=
   Sleep    2s

   Input Text    mob_no    9876543221
   Sleep    1s

   Input Text    email_id    anil@gmail.com
   Sleep    1s

   Input Text    re_email_id    anil@gmail.com
   Sleep    1s

   Input Password    pass    anil123
   Sleep    1s

   Input Password    confirm_pass    anil123
   Sleep    2s

#    Click Button    register
