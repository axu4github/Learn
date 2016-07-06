from django.db import models


class People(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)


class People1(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'PeopleOne'


class People2(models.Model):
    # Field name made lowercase.
    departmentid = models.IntegerField(
        db_column='departmentId', blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    # Field name made lowercase.
    createtime = models.CharField(
        db_column='createTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    createuser = models.CharField(
        db_column='createUser', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifytime = models.CharField(
        db_column='lastModifyTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifyuser = models.CharField(
        db_column='lastModifyUser', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'PeopleTwo'


class Businesstype(models.Model):
    # Field name made lowercase.
    departmentid = models.IntegerField(
        db_column='departmentId', blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    # Field name made lowercase.
    createtime = models.CharField(
        db_column='createTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    createuser = models.CharField(
        db_column='createUser', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifytime = models.CharField(
        db_column='lastModifyTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifyuser = models.CharField(
        db_column='lastModifyUser', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'BusinessType'


class Department(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId')
    code = models.CharField(max_length=20, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'Department'


class Dictionary(models.Model):
    # Field name made lowercase.
    groupname = models.CharField(
        db_column='groupName', max_length=40, blank=True, null=True)
    key = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    # Field name made lowercase.
    sortindex = models.IntegerField(
        db_column='sortIndex', blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Dictionary'


class Keyword(models.Model):
    # Field name made lowercase.
    keywordtypeid = models.IntegerField(
        db_column='keywordTypeId', blank=True, null=True)
    keyword = models.CharField(max_length=40, blank=True, null=True)
    synonym = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    # Field name made lowercase.
    createtime = models.CharField(
        db_column='createTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    createuser = models.CharField(
        db_column='createUser', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    usabletime = models.CharField(
        db_column='usableTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    forbiddentime = models.CharField(
        db_column='forbiddenTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifytime = models.CharField(
        db_column='lastModifyTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifyuser = models.CharField(
        db_column='lastModifyUser', max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KeyWord'


class Metadetail(models.Model):
    meta_id = models.CharField(max_length=40, blank=True, null=True)
    serial = models.IntegerField(blank=True, null=True)
    field = models.CharField(max_length=50, blank=True, null=True)
    field_name = models.CharField(max_length=50, blank=True, null=True)
    field_type = models.CharField(max_length=20, blank=True, null=True)
    primary_key = models.CharField(max_length=1, blank=True, null=True)
    field_info = models.CharField(max_length=1000, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetaDetail'


class Metainfo(models.Model):
    meta_id = models.CharField(max_length=40)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    table_cname = models.CharField(max_length=100, blank=True, null=True)
    file_location = models.CharField(max_length=200, blank=True, null=True)
    mutifile = models.CharField(max_length=1, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_split = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.CharField(max_length=20, blank=True, null=True)
    data_number = models.CharField(max_length=20, blank=True, null=True)
    response = models.CharField(max_length=20, blank=True, null=True)
    data_desc = models.CharField(max_length=1000, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    changeinfo = models.CharField(max_length=1000, blank=True, null=True)
    metatype = models.ForeignKey('Metatype', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetaInfo'


class Metamanager(models.Model):
    meta_id = models.CharField(max_length=40)
    lifecycle = models.IntegerField(blank=True, null=True)
    updatecycle = models.IntegerField(blank=True, null=True)
    share = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetaManager'


class Metamapping(models.Model):
    meta_id = models.CharField(max_length=40)
    meta_source = models.CharField(max_length=40, blank=True, null=True)
    etl_engine = models.CharField(max_length=40, blank=True, null=True)
    etl_config = models.CharField(max_length=200, blank=True, null=True)
    timespan = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)
    changeinfo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetaMapping'


class Metarelation(models.Model):
    meta_id = models.CharField(max_length=40, blank=True, null=True)
    field = models.CharField(max_length=50, blank=True, null=True)
    meta2_id = models.CharField(max_length=40, blank=True, null=True)
    field2 = models.CharField(max_length=50, blank=True, null=True)
    rules = models.CharField(max_length=200, blank=True, null=True)
    mapping = models.CharField(max_length=1, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    used = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetaRelation'


class Metatype(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetaType'


class Securitymodule(models.Model):
    # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    # Field name made lowercase.
    showname = models.CharField(
        db_column='showName', max_length=20, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    sortindex = models.IntegerField(
        db_column='sortIndex', blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    # Field name made lowercase.
    ismenu = models.CharField(
        db_column='isMenu', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    isopennew = models.CharField(
        db_column='isOpenNew', max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SecurityModule'


class Securityrole(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    # Field name made lowercase.
    showname = models.CharField(
        db_column='showName', max_length=20, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SecurityRole'


class Securityrolemodule(models.Model):
    # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')
    # Field name made lowercase.
    moduleid = models.IntegerField(db_column='moduleId')

    class Meta:
        managed = False
        db_table = 'SecurityRoleModule'
        unique_together = (('roleid', 'moduleid'),)


class Securityuser(models.Model):
    # Field name made lowercase.
    departmentid = models.IntegerField(
        db_column='departmentId', blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    # Field name made lowercase.
    realname = models.CharField(
        db_column='realName', max_length=40, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    identity = models.CharField(max_length=10, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    # Field name made lowercase.
    loginfailed = models.IntegerField(
        db_column='loginFailed', blank=True, null=True)
    # Field name made lowercase.
    createtime = models.CharField(
        db_column='createTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    createuser = models.IntegerField(
        db_column='createUser', blank=True, null=True)
    # Field name made lowercase.
    lastmodifytime = models.CharField(
        db_column='lastModifyTime', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    lastmodifyuser = models.IntegerField(
        db_column='lastModifyUser', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SecurityUser'


class Securityuserrole(models.Model):
    # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')
    # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')

    class Meta:
        managed = False
        db_table = 'SecurityUserRole'
        unique_together = (('userid', 'roleid'),)
