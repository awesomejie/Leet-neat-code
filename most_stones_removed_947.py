# https://blog.csdn.net/fuxuemingzhu/article/details/84500642

并查集
这个题翻译一下就是，横或者纵坐标相等的坐标点会互相链接构成一个区域，问总的有多少个独立的区域。结果是总的石头数减去独立区域数。

其实上面这个版本可以做优化，我们不用对石头进行两两判断，而是对他们的横纵坐标同等看待。怎么区分横纵坐标呢？使用的方法是把纵坐标+10000，这样行的索引没变，纵坐标的范围跑到了后面去了。

这个做法的思路是，一个坐标其实就是把横纵坐标对应的两个区域进行了链接。所以，只需要对stones进行一次遍历把对应的区域链接到一起即可。在完成链接之后，我们最后统计一下有多少个独立的区域，需要使用set+find。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/84500642
版权声明：本文为博主原创文章，转载请附上博文链接！


https://buptwc.com/2018/11/25/Leetcode-947-Most-Stones-Removed-with-Same-Row-or-Column/
