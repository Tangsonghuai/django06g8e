#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class gonggaoxinxi(BaseModel):
    __doc__ = u'''gonggaoxinxi'''
    __tablename__ = 'gonggaoxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    gonggaobiaoti=models.CharField ( max_length=255,null=False, unique=False, verbose_name='公告标题' )
    gonggaoleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='公告类型' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    neirong=models.TextField   (  null=True, unique=False, verbose_name='内容' )
    faburiqi=models.DateField   (  null=True, unique=False, verbose_name='发布日期' )
    '''
    gonggaobiaoti=VARCHAR
    gonggaoleixing=VARCHAR
    tupian=Text
    neirong=Text
    faburiqi=Date
    '''
    class Meta:
        db_table = 'gonggaoxinxi'
        verbose_name = verbose_name_plural = '公告信息'
class shangpinfenlei(BaseModel):
    __doc__ = u'''shangpinfenlei'''
    __tablename__ = 'shangpinfenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    fenlei=models.CharField ( max_length=255,null=False,unique=True, verbose_name='分类' )
    '''
    fenlei=VARCHAR
    '''
    class Meta:
        db_table = 'shangpinfenlei'
        verbose_name = verbose_name_plural = '商品分类'
class shangpinxinxi(BaseModel):
    __doc__ = u'''shangpinxinxi'''
    __tablename__ = 'shangpinxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
    fenlei=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类' )
    gongyi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='工艺' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    xiangqing=models.TextField   (  null=True, unique=False, verbose_name='详情' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    '''
    shangpinmingcheng=VARCHAR
    fenlei=VARCHAR
    gongyi=VARCHAR
    tupian=Text
    guige=VARCHAR
    pinpai=VARCHAR
    xiangqing=Text
    clicktime=DateTime
    clicknum=Integer
    price=Float
    '''
    class Meta:
        db_table = 'shangpinxinxi'
        verbose_name = verbose_name_plural = '商品信息'
class huodongshangpin(BaseModel):
    __doc__ = u'''huodongshangpin'''
    __tablename__ = 'huodongshangpin'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
    fenlei=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类' )
    gongyi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='工艺' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    xiangqing=models.TextField   (  null=True, unique=False, verbose_name='详情' )
    reversetime=models.DateTimeField  (  null=True, unique=False, verbose_name='倒计结束时间' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    '''
    shangpinmingcheng=VARCHAR
    fenlei=VARCHAR
    gongyi=VARCHAR
    tupian=Text
    guige=VARCHAR
    pinpai=VARCHAR
    xiangqing=Text
    reversetime=DateTime
    price=Float
    '''
    class Meta:
        db_table = 'huodongshangpin'
        verbose_name = verbose_name_plural = '活动商品'
class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuming'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuming'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuming=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='余额' )
    '''
    yonghuming=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    touxiang=Text
    shouji=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class yonghushangpin(BaseModel):
    __doc__ = u'''yonghushangpin'''
    __tablename__ = 'yonghushangpin'



    __authTables__={'yonghuming':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
    fenlei=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类' )
    gongyi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='工艺' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    xiangqing=models.TextField   (  null=True, unique=False, verbose_name='详情' )
    yonghuming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    '''
    shangpinmingcheng=VARCHAR
    fenlei=VARCHAR
    gongyi=VARCHAR
    tupian=Text
    guige=VARCHAR
    pinpai=VARCHAR
    xiangqing=Text
    yonghuming=VARCHAR
    shouji=VARCHAR
    price=Float
    '''
    class Meta:
        db_table = 'yonghushangpin'
        verbose_name = verbose_name_plural = '用户商品'
class tuihuohuanhuo(BaseModel):
    __doc__ = u'''tuihuohuanhuo'''
    __tablename__ = 'tuihuohuanhuo'



    __authTables__={'yonghuming':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='订单编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    yonghuming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    shenqingriqi=models.DateField   (  null=True, unique=False, verbose_name='申请日期' )
    shenqingyuanyin=models.TextField   (  null=True, unique=False, verbose_name='申请原因' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    dingdanbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    yonghuming=VARCHAR
    shenqingriqi=Date
    shenqingyuanyin=Text
    beizhu=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'tuihuohuanhuo'
        verbose_name = verbose_name_plural = '退货换货'
class tousufankui(BaseModel):
    __doc__ = u'''tousufankui'''
    __tablename__ = 'tousufankui'



    __authTables__={'yonghuming':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    biaotimingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题名称' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    neirongxiangqing=models.TextField   (  null=True, unique=False, verbose_name='内容详情' )
    riqi=models.DateField   (  null=True, unique=False, verbose_name='日期' )
    yonghuming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    biaotimingcheng=VARCHAR
    tupian=Text
    neirongxiangqing=Text
    riqi=Date
    yonghuming=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'tousufankui'
        verbose_name = verbose_name_plural = '投诉反馈'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '客服聊天表'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='yonghushangpin', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='单价' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = '购物车表'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='yonghushangpin', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   ( null=False, unique=False,default='0', verbose_name='价格' )
    total=models.FloatField   ( null=False, unique=False,default='0', verbose_name='总价格' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='支付类型' )
    status=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    tel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    consignee=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货人' )
    logistics=models.TextField   (  null=True, unique=False, verbose_name='物流' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    total=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    logistics=Text
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'
class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
    phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
    isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='是否默认地址[是/否]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = '地址'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '新闻资讯'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class discussgonggaoxinxi(BaseModel):
    __doc__ = u'''discussgonggaoxinxi'''
    __tablename__ = 'discussgonggaoxinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussgonggaoxinxi'
        verbose_name = verbose_name_plural = '公告信息评论表'
class discussshangpinxinxi(BaseModel):
    __doc__ = u'''discussshangpinxinxi'''
    __tablename__ = 'discussshangpinxinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussshangpinxinxi'
        verbose_name = verbose_name_plural = '商品信息评论表'
class discusshuodongshangpin(BaseModel):
    __doc__ = u'''discusshuodongshangpin'''
    __tablename__ = 'discusshuodongshangpin'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusshuodongshangpin'
        verbose_name = verbose_name_plural = '活动商品评论表'
class discussyonghushangpin(BaseModel):
    __doc__ = u'''discussyonghushangpin'''
    __tablename__ = 'discussyonghushangpin'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussyonghushangpin'
        verbose_name = verbose_name_plural = '用户商品评论表'
