.. _use_help:

学会使用命令帮助  
======================

.. contents:: 目录

概述  
--------------------
在python命令行，面对命令不知道怎么用，或不记得命令的拼写及参数时，我们需要求助于系统的帮助文档；
python内置的帮助文档很详细，通常能解决我们的问题，我们需要掌握如何正确的去使用它们；

- 使用help(object)内置函数，如help(list)
- 使用dir(object)查看函数常用方法，如dir(list)
- 使用pydoc.help(request)查看帮助文档，如pydoc.help(re)

下面介绍这些命令。


命令使用
--------------------

使用help方法查看帮助文档
^^^^^^^^^^^^^^^^^^^^^^^^^^

不需要导入模块的::

    >>> help(list)
    Help on class list in module builtins:
    
    class list(object)
     |  list() -> new empty list
     |  list(iterable) -> new list initialized from iterable's items
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
    -- More  --
    
需要导入模块的::

    >>> import os
    >>> help(os)
    Help on module os:
    
    NAME
        os - OS routines for NT or Posix depending on what system we're on.
    
    DESCRIPTION
        This exports:
          - all functions from posix or nt, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix' or 'nt'
          - os.curdir is a string representing the current directory (always '.')
          - os.pardir is a string representing the parent directory (always '..')
          - os.sep is the (or a most common) pathname separator ('/' or '\\')
          - os.extsep is the extension separator (always '.')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)
    
        Programs that import and use 'os' stand a better chance of being
        portable between different platforms.  Of course, they must then
        only use functions that are defined by all platforms (e.g., unlink
        and opendir), and leave all pathname manipulation to os.path
        (e.g., split and join).
    
    CLASSES
        builtins.Exception(builtins.BaseException)
            builtins.OSError
    -- More  --

    
使用dir方法查看帮助文档
^^^^^^^^^^^^^^^^^^^^^^^^^^

不需要导入模块的::

    >>> dir(list)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

导入模块的::

    >>> import os
    >>> dir(os)
    ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']

    
使用pydoc方法查看帮助文档
^^^^^^^^^^^^^^^^^^^^^^^^^^

进入到pydoc.help()的help帮助命令行查看帮助文档::

    >>> import pydoc
    >>> pydoc.help()

    Welcome to Python 3.6's help utility!

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, symbols, or topics, type
    "modules", "keywords", "symbols", or "topics".  Each module also comes
    with a one-line summary of what it does; to list the modules whose name
    or summary contain a given string such as "spam", type "modules spam".

    help> list
    Help on class list in module builtins:

    class list(object)
     |  list() -> new empty list
     |  list(iterable) -> new list initialized from iterable's items
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.n
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __reversed__(...)
     |      L.__reversed__() -- return a reverse iterator over the list
     |
     |  __rmul__(self, value, /)
     |      Return self*value.
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __sizeof__(...)
     |      L.__sizeof__() -- size of L in memory, in bytes
     |
     |  append(...)
     |      L.append(object) -> None -- append object to end
     |
     |  clear(...)
     |      L.clear() -> None -- remove all items from L
     |
     |  copy(...)
     |      L.copy() -> list -- a shallow copy of L
     |
     |  count(...)
     |      L.count(value) -> integer -- return number of occurrences of value
     |
     |  extend(...)
     |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
     |
     |  index(...)
     |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
     |
     |  insert(...)
     |      L.insert(index, object) -- insert object before index
     |
     |  pop(...)
     |      L.pop([index]) -> item -- remove and return item at index (default last).
     |      Raises IndexError if list is empty or index is out of range.
     |
     |  remove(...)
     |      L.remove(value) -> None -- remove first occurrence of value.
     |      Raises ValueError if the value is not present.
     |
     |  reverse(...)
     |      L.reverse() -- reverse *IN PLACE*
     |
     |  sort(...)
     |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None
    
    help> re
    Help on module re:
    
    NAME
        re - Support for regular expressions (RE).

    DESCRIPTION
        This module provides regular expression matching operations similar to
        those found in Perl.  It supports both 8-bit and Unicode strings; both
        the pattern and the strings being processed can contain null bytes and
        characters outside the US ASCII range.

        Regular expressions can contain both special and ordinary characters.
        Most ordinary characters, like "A", "a", or "0", are the simplest
        regular expressions; they simply match themselves.  You can
        concatenate ordinary characters, so last matches the string 'last'.
     
        The special characters are:
            "."      Matches any character except a newline.
            "^"      Matches the start of the string.
            "$"      Matches the end of the string or just before the newline at
                     the end of the string.
            "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                     Greedy means that it will match as many repetitions as possible.
            "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
            "?"      Matches 0 or 1 (greedy) of the preceding RE.
            *?,+?,?? Non-greedy versions of the previous three special characters.
            {m,n}    Matches from m to n repetitions of the preceding RE.
            {m,n}?   Non-greedy version of the above.
            "\\"     Either escapes special characters or signals a special sequence.
    -- More  --
    

使用ipython环境查看帮助文档
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

安装ipython::

    pip install ipython

进入到ipython环境，使用help或?查看帮助文档::

    $ ipython                                                                               
    Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)]        
    Type 'copyright', 'credits' or 'license' for more information                           
    IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.                     
                                                                                            
    In [1]: import os                                                                       
                                                                                            
    In [2]: help(os)                                                                        
    Help on module os:                                                                      
                                                                                            
    NAME                                                                                    
        os - OS routines for NT or Posix depending on what system we're on.                 
                                                                                            
    DESCRIPTION                                                                             
        This exports:                                                                       
          - all functions from posix or nt, e.g. unlink, stat, etc.                         
          - os.path is either posixpath or ntpath                                           
          - os.name is either 'posix' or 'nt'                                               
          - os.curdir is a string representing the current directory (always '.')           
          - os.pardir is a string representing the parent directory (always '..')           
          - os.sep is the (or a most common) pathname separator ('/' or '\\')               
          - os.extsep is the extension separator (always '.')                               
          - os.altsep is the alternate pathname separator (None or '/')                     
          - os.pathsep is the component separator used in $PATH etc                         
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')         
          - os.defpath is the default search path for executables                           
          - os.devnull is the file path of the null device ('/dev/null', etc.)              
                                                                                            
        Programs that import and use 'os' stand a better chance of being                    
        portable between different platforms.  Of course, they must then                    
        only use functions that are defined by all platforms (e.g., unlink                  
        and opendir), and leave all pathname manipulation to os.path                        
        (e.g., split and join).                                                             
                                                                                            
                                                                                            
    In [3]: os?                                                                             
    Type:        module                                                                     
    String form: <module 'os' from 'd:\\program files (x86)\\python3.6.2\\lib\\os.py'>      
    File:        d:\program files (x86)\python3.6.2\lib\os.py                               
    Docstring:                                                                              
    OS routines for NT or Posix depending on what system we're on.                          
                                                                                            
    This exports:                                                                           
      - all functions from posix or nt, e.g. unlink, stat, etc.                             
      - os.path is either posixpath or ntpath                                               
      - os.name is either 'posix' or 'nt'                                                   
      - os.curdir is a string representing the current directory (always '.')               
      - os.pardir is a string representing the parent directory (always '..')               
      - os.sep is the (or a most common) pathname separator ('/' or '\\')                   
      - os.extsep is the extension separator (always '.')                                   
      - os.altsep is the alternate pathname separator (None or '/')                         
      - os.pathsep is the component separator used in $PATH etc                             
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')             
      - os.defpath is the default search path for executables                               
      - os.devnull is the file path of the null device ('/dev/null', etc.)                  
                                                                                            
    Programs that import and use 'os' stand a better chance of being                        
    portable between different platforms.  Of course, they must then                        
    only use functions that are defined by all platforms (e.g., unlink                      
    and opendir), and leave all pathname manipulation to os.path                            
    (e.g., split and join).                                                                 
                                                                                            
    In [4]:                                                                                 

将帮助文档导出到文件
--------------------
    
help2file.py代码如下::

    import sys
    import pydoc
    
    def output_help_to_file(filepath, request):
        f = open(filepath, 'w')
        sys.stdout = f
        pydoc.help(request)
        f.close()
        sys.stdout = sys.__stdout__
        return
    
    if __name__ == '__main__':
        # 导出re的help文档
        output_help_to_file('re.txt', 're')

查看re.txt文档更详细的帮助内容::

    Help on module re:
    
    NAME
        re - Support for regular expressions (RE).
    
    DESCRIPTION
        This module provides regular expression matching operations similar to
        those found in Perl.  It supports both 8-bit and Unicode strings; both
        the pattern and the strings being processed can contain null bytes and
        characters outside the US ASCII range.
        
        Regular expressions can contain both special and ordinary characters.
        Most ordinary characters, like "A", "a", or "0", are the simplest
        regular expressions; they simply match themselves.  You can
        concatenate ordinary characters, so last matches the string 'last'.
        
        The special characters are:
            "."      Matches any character except a newline.
            "^"      Matches the start of the string.
            "$"      Matches the end of the string or just before the newline at
                     the end of the string.
            "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                     Greedy means that it will match as many repetitions as possible.
            "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
            "?"      Matches 0 or 1 (greedy) of the preceding RE.
            *?,+?,?? Non-greedy versions of the previous three special characters.
            {m,n}    Matches from m to n repetitions of the preceding RE.
            {m,n}?   Non-greedy version of the above.
            "\\"     Either escapes special characters or signals a special sequence.
            []       Indicates a set of characters.
                     A "^" as the first character indicates a complementing set.
            "|"      A|B, creates an RE that will match either A or B.
            (...)    Matches the RE inside the parentheses.
                     The contents can be retrieved or matched later in the string.
            (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
            (?:...)  Non-grouping version of regular parentheses.
            (?P<name>...) The substring matched by the group is accessible by name.
            (?P=name)     Matches the text matched earlier by the group named name.
            (?#...)  A comment; ignored.
            (?=...)  Matches if ... matches next, but doesn't consume the string.
            (?!...)  Matches if ... doesn't match next.
            (?<=...) Matches if preceded by ... (must be fixed length).
            (?<!...) Matches if not preceded by ... (must be fixed length).
            (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                               the (optional) no pattern otherwise.
        
        The special sequences consist of "\\" and a character from the list
        below.  If the ordinary character is not on the list, then the
        resulting RE will match the second character.
            \number  Matches the contents of the group of the same number.
            \A       Matches only at the start of the string.
            \Z       Matches only at the end of the string.
            \b       Matches the empty string, but only at the start or end of a word.
            \B       Matches the empty string, but not at the start or end of a word.
            \d       Matches any decimal digit; equivalent to the set [0-9] in
                     bytes patterns or string patterns with the ASCII flag.
                     In string patterns without the ASCII flag, it will match the whole
                     range of Unicode digits.
            \D       Matches any non-digit character; equivalent to [^\d].
            \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                     bytes patterns or string patterns with the ASCII flag.
                     In string patterns without the ASCII flag, it will match the whole
                     range of Unicode whitespace characters.
            \S       Matches any non-whitespace character; equivalent to [^\s].
            \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                     in bytes patterns or string patterns with the ASCII flag.
                     In string patterns without the ASCII flag, it will match the
                     range of Unicode alphanumeric characters (letters plus digits
                     plus underscore).
                     With LOCALE, it will match the set [0-9_] plus characters defined
                     as letters for the current locale.
            \W       Matches the complement of \w.
            \\       Matches a literal backslash.
        
        This module exports the following functions:
            match     Match a regular expression pattern to the beginning of a string.
            fullmatch Match a regular expression pattern to all of a string.
            search    Search a string for the presence of a pattern.
            sub       Substitute occurrences of a pattern found in a string.
            subn      Same as sub, but also return the number of substitutions made.
            split     Split a string by the occurrences of a pattern.
            findall   Find all occurrences of a pattern in a string.
            finditer  Return an iterator yielding a match object for each match.
            compile   Compile a pattern into a RegexObject.
            purge     Clear the regular expression cache.
            escape    Backslash all non-alphanumerics in a string.
        
        Some of the functions in this module takes flags as optional parameters:
            A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                           match the corresponding ASCII character categories
                           (rather than the whole Unicode categories, which is the
                           default).
                           For bytes patterns, this flag is the only available
                           behaviour and needn't be specified.
            I  IGNORECASE  Perform case-insensitive matching.
            L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
            M  MULTILINE   "^" matches the beginning of lines (after a newline)
                           as well as the string.
                           "$" matches the end of lines (before a newline) as well
                           as the end of the string.
            S  DOTALL      "." matches any character at all, including the newline.
            X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
            U  UNICODE     For compatibility only. Ignored for string patterns (it
                           is the default), and forbidden for bytes patterns.
        
        This module also defines an exception 'error'.
    
    CLASSES
        builtins.Exception(builtins.BaseException)
            sre_constants.error
        
        class error(builtins.Exception)
         |  Exception raised for invalid regular expressions.
         |  
         |  Attributes:
         |  
         |      msg: The unformatted error message
         |      pattern: The regular expression pattern
         |      pos: The index in the pattern where compilation failed (may be None)
         |      lineno: The line corresponding to pos (may be None)
         |      colno: The column corresponding to pos (may be None)
         |  
         |  Method resolution order:
         |      error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, msg, pattern=None, pos=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |      helper for pickle
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
    
    FUNCTIONS
        compile(pattern, flags=0)
            Compile a regular expression pattern, returning a pattern object.
        
        escape(pattern)
            Escape all the characters in pattern except ASCII letters, numbers and '_'.
        
        findall(pattern, string, flags=0)
            Return a list of all non-overlapping matches in the string.
            
            If one or more capturing groups are present in the pattern, return
            a list of groups; this will be a list of tuples if the pattern
            has more than one group.
            
            Empty matches are included in the result.
        
        finditer(pattern, string, flags=0)
            Return an iterator over all non-overlapping matches in the
            string.  For each match, the iterator returns a match object.
            
            Empty matches are included in the result.
        
        fullmatch(pattern, string, flags=0)
            Try to apply the pattern to all of the string, returning
            a match object, or None if no match was found.
        
        match(pattern, string, flags=0)
            Try to apply the pattern at the start of the string, returning
            a match object, or None if no match was found.
        
        purge()
            Clear the regular expression caches
        
        search(pattern, string, flags=0)
            Scan through string looking for a match to the pattern, returning
            a match object, or None if no match was found.
        
        split(pattern, string, maxsplit=0, flags=0)
            Split the source string by the occurrences of the pattern,
            returning a list containing the resulting substrings.  If
            capturing parentheses are used in pattern, then the text of all
            groups in the pattern are also returned as part of the resulting
            list.  If maxsplit is nonzero, at most maxsplit splits occur,
            and the remainder of the string is returned as the final element
            of the list.
        
        sub(pattern, repl, string, count=0, flags=0)
            Return the string obtained by replacing the leftmost
            non-overlapping occurrences of the pattern in string by the
            replacement repl.  repl can be either a string or a callable;
            if a string, backslash escapes in it are processed.  If it is
            a callable, it's passed the match object and must return
            a replacement string to be used.
        
        subn(pattern, repl, string, count=0, flags=0)
            Return a 2-tuple containing (new_string, number).
            new_string is the string obtained by replacing the leftmost
            non-overlapping occurrences of the pattern in the source
            string by the replacement repl.  number is the number of
            substitutions that were made. repl can be either a string or a
            callable; if a string, backslash escapes in it are processed.
            If it is a callable, it's passed the match object and must
            return a replacement string to be used.
        
        template(pattern, flags=0)
            Compile a template pattern, returning a pattern object
    
    DATA
        A = <RegexFlag.ASCII: 256>
        ASCII = <RegexFlag.ASCII: 256>
        DOTALL = <RegexFlag.DOTALL: 16>
        I = <RegexFlag.IGNORECASE: 2>
        IGNORECASE = <RegexFlag.IGNORECASE: 2>
        L = <RegexFlag.LOCALE: 4>
        LOCALE = <RegexFlag.LOCALE: 4>
        M = <RegexFlag.MULTILINE: 8>
        MULTILINE = <RegexFlag.MULTILINE: 8>
        S = <RegexFlag.DOTALL: 16>
        U = <RegexFlag.UNICODE: 32>
        UNICODE = <RegexFlag.UNICODE: 32>
        VERBOSE = <RegexFlag.VERBOSE: 64>
        X = <RegexFlag.VERBOSE: 64>
        __all__ = ['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'fi...
    
    VERSION
        2.2.1
    
    FILE
        d:\program files (x86)\python3.6.2\lib\re.py
    
    
将help2file.py文件复制到python的安装目录D:\\Program Files (x86)\\python3.6.2\\Lib下，再在其他位置导入help2file模板::

    D:\tmp>python
    Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import help2file
    >>> help2file.output_help_to_file('dict.txt','dict')
    
在D:\\tmp目录下新生成了文件dict.txt，打开可以详细查看字典dict的帮助说明。



