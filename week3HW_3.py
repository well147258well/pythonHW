# -*- coding: utf-8 -*-

f = open('input.txt','r')
list= f.read()

print u'共有%d個e' %list.count('e')
print u'共有%d個空白' %list.count(' ')
print u'共有%d個字元' %len(list)

a=list.count('e')
b=list.count(' ')
c=len(list)

print u'e佔整個檔案%f' %(a/float(c))
print u'空白佔整個檔案%f' %(b/float(c))


