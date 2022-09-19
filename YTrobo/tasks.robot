*** Settings ***
Documentation     YouTube videos downloader from excel sheet
Library           RPA.Browser.Selenium        auto_close=${FALSE}
Library           RPA.Excel.Files
Library    RPA.Desktop.Windows

*** Tasks ***
YouTube videos downloader from excel sheet
    Open the intranet website
    
    Fill URL from sheet
    

*** Keywords ***
Open the intranet website
    Open Available Browser    https://en.savefrom.net/1-youtube-video-downloader-307/?url=http%3A%2F%2Fyoutube.com%2Fwatch%3Fv%3De4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=10&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=ssyoutube.com&a_ts=1661658173.125    maximized=${TRUE}    

Fill URL from sheet
    Open Workbook    /home/i3systems/Documents/CodeBeyond.xlsx
    ${vid url}=    Read Worksheet As Table    header=True
    Close Workbook
    FOR    ${current vid url}    IN    @{vid url}
        Input Text    sf_url    ${current vid url}[Video URL]
        Click Button    sf_submit
        Click Element When Visible   //*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a
        
        Switch Window    NEW
        Close Window
        Switch Window    MAIN

        Set Selenium Speed	0.5 seconds
    END


