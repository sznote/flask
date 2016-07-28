from  flask import Blueprint
tutor1 =  Blueprint('tutorial1',__name__)

print tutor1.root_path
#D:\mycode\flask\Flask_Tutorial\tutorial1

from  tutorial1  import  views
