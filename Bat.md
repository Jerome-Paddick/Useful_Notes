BAT
===

`@Echo Off`

- `%cd%` 	-> current working directory  
- `%~dp0 `	-> directory of the bat file
- `"%~dp0Txt.txt"`

:: If no files passed to bat  

    if %1.==. (
        echo Please Drag Directory into Bat File
    ) else (
        dir %1 /A /S > "%~dp0DIR LOG 1.txt"
        echo DIR 1 - Done
    )

REM 	This is a Comment
:: 	This is also a comment (invalid label) (does not work inside ())
%=	This is a variable (could be used as a comment) % 

:: Navigate to file
explorer `<PATH>`

:: Dont Repeat inputs
`@Echo off `

:: OUTPUT File
`<Command> > <Filepath>`

:: pass files (% is many) to python file
`python "<FILEPATH>" %*`

:: Run Multiple Operations simultaneously
`python script1.py & script2.py & 
python script3.py & script4.py & script5.py &`

:: waits until operations have finished before continuing
`wait`

:: waits until user enters key before continuing
`pause`

:: `&&` runs next script only if preceeding script has completed successfully
`python script1 && script2 && script3 `

:: `||` runs scripts sequentially irrespective of the result of preceding script

`python loader.py || python cain.py || python able.py`

asdf & `:: INLINE COMMENT`