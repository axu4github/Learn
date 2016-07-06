# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywordtypeid', models.IntegerField(null=True, db_column=b'keywordTypeId', blank=True)),
                ('keyword', models.CharField(max_length=40, null=True, blank=True)),
                ('synonym', models.CharField(max_length=100, null=True, blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('createtime', models.CharField(max_length=20, null=True, db_column=b'createTime', blank=True)),
                ('createuser', models.CharField(max_length=20, null=True, db_column=b'createUser', blank=True)),
                ('usabletime', models.CharField(max_length=20, null=True, db_column=b'usableTime', blank=True)),
                ('forbiddentime', models.CharField(max_length=20, null=True, db_column=b'forbiddenTime', blank=True)),
                ('lastmodifytime', models.CharField(max_length=20, null=True, db_column=b'lastModifyTime', blank=True)),
                ('lastmodifyuser', models.CharField(max_length=20, null=True, db_column=b'lastModifyUser', blank=True)),
                ('remark', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'KeyWord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metadetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_id', models.CharField(max_length=40, null=True, blank=True)),
                ('serial', models.IntegerField(null=True, blank=True)),
                ('field', models.CharField(max_length=50, null=True, blank=True)),
                ('field_name', models.CharField(max_length=50, null=True, blank=True)),
                ('field_type', models.CharField(max_length=20, null=True, blank=True)),
                ('primary_key', models.CharField(max_length=1, null=True, blank=True)),
                ('field_info', models.CharField(max_length=1000, null=True, blank=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('used', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'MetaDetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metainfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_id', models.CharField(max_length=40)),
                ('table_name', models.CharField(max_length=100, null=True, blank=True)),
                ('table_cname', models.CharField(max_length=100, null=True, blank=True)),
                ('file_location', models.CharField(max_length=200, null=True, blank=True)),
                ('mutifile', models.CharField(max_length=1, null=True, blank=True)),
                ('file_type', models.CharField(max_length=50, null=True, blank=True)),
                ('file_split', models.CharField(max_length=10, null=True, blank=True)),
                ('quantity', models.CharField(max_length=20, null=True, blank=True)),
                ('data_number', models.CharField(max_length=20, null=True, blank=True)),
                ('response', models.CharField(max_length=20, null=True, blank=True)),
                ('data_desc', models.CharField(max_length=1000, null=True, blank=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('used', models.CharField(max_length=1, null=True, blank=True)),
                ('changeinfo', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'db_table': 'MetaInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metamanager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_id', models.CharField(max_length=40)),
                ('lifecycle', models.IntegerField(null=True, blank=True)),
                ('updatecycle', models.IntegerField(null=True, blank=True)),
                ('share', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'MetaManager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metamapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_id', models.CharField(max_length=40)),
                ('meta_source', models.CharField(max_length=40, null=True, blank=True)),
                ('etl_engine', models.CharField(max_length=40, null=True, blank=True)),
                ('etl_config', models.CharField(max_length=200, null=True, blank=True)),
                ('timespan', models.IntegerField(null=True, blank=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('used', models.CharField(max_length=1, null=True, blank=True)),
                ('changeinfo', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'db_table': 'MetaMapping',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metarelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta_id', models.CharField(max_length=40, null=True, blank=True)),
                ('field', models.CharField(max_length=50, null=True, blank=True)),
                ('meta2_id', models.CharField(max_length=40, null=True, blank=True)),
                ('field2', models.CharField(max_length=50, null=True, blank=True)),
                ('rules', models.CharField(max_length=200, null=True, blank=True)),
                ('mapping', models.CharField(max_length=1, null=True, blank=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('used', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'MetaRelation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metatype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('parentid', models.IntegerField(null=True, db_column=b'parentId', blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'MetaType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securitymodule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parentid', models.IntegerField(null=True, db_column=b'parentId', blank=True)),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('showname', models.CharField(max_length=20, null=True, db_column=b'showName', blank=True)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
                ('sortindex', models.IntegerField(null=True, db_column=b'sortIndex', blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('ismenu', models.CharField(max_length=1, null=True, db_column=b'isMenu', blank=True)),
                ('isopennew', models.CharField(max_length=1, null=True, db_column=b'isOpenNew', blank=True)),
                ('remark', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'SecurityModule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securityrole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('showname', models.CharField(max_length=20, null=True, db_column=b'showName', blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('remark', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'SecurityRole',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securityrolemodule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleid', models.IntegerField(db_column=b'roleId')),
                ('moduleid', models.IntegerField(db_column=b'moduleId')),
            ],
            options={
                'db_table': 'SecurityRoleModule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securityuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmentid', models.IntegerField(null=True, db_column=b'departmentId', blank=True)),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('realname', models.CharField(max_length=40, null=True, db_column=b'realName', blank=True)),
                ('password', models.CharField(max_length=100, null=True, blank=True)),
                ('identity', models.CharField(max_length=10, null=True, blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('loginfailed', models.IntegerField(null=True, db_column=b'loginFailed', blank=True)),
                ('createtime', models.CharField(max_length=20, null=True, db_column=b'createTime', blank=True)),
                ('createuser', models.IntegerField(null=True, db_column=b'createUser', blank=True)),
                ('lastmodifytime', models.CharField(max_length=20, null=True, db_column=b'lastModifyTime', blank=True)),
                ('lastmodifyuser', models.IntegerField(null=True, db_column=b'lastModifyUser', blank=True)),
            ],
            options={
                'db_table': 'SecurityUser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Securityuserrole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.IntegerField(db_column=b'userId')),
                ('roleid', models.IntegerField(db_column=b'roleId')),
            ],
            options={
                'db_table': 'SecurityUserRole',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Businesstype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmentid', models.IntegerField(null=True, db_column=b'departmentId', blank=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('createtime', models.CharField(max_length=20, null=True, db_column=b'createTime', blank=True)),
                ('createuser', models.CharField(max_length=20, null=True, db_column=b'createUser', blank=True)),
                ('lastmodifytime', models.CharField(max_length=20, null=True, db_column=b'lastModifyTime', blank=True)),
                ('lastmodifyuser', models.CharField(max_length=20, null=True, db_column=b'lastModifyUser', blank=True)),
            ],
            options={
                'db_table': 'BusinessType',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('parentid', models.IntegerField(db_column=b'parentId')),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=40, null=True, db_column=b'groupName', blank=True)),
                ('key', models.CharField(max_length=100, null=True, blank=True)),
                ('desc', models.CharField(max_length=100, null=True, blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('sortindex', models.IntegerField(null=True, db_column=b'sortIndex', blank=True)),
                ('remark', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'Dictionary',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='People1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'PeopleOne',
            },
        ),
        migrations.CreateModel(
            name='People2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmentid', models.IntegerField(null=True, db_column=b'departmentId', blank=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
                ('createtime', models.CharField(max_length=20, null=True, db_column=b'createTime', blank=True)),
                ('createuser', models.CharField(max_length=20, null=True, db_column=b'createUser', blank=True)),
                ('lastmodifytime', models.CharField(max_length=20, null=True, db_column=b'lastModifyTime', blank=True)),
                ('lastmodifyuser', models.CharField(max_length=20, null=True, db_column=b'lastModifyUser', blank=True)),
            ],
            options={
                'db_table': 'PeopleTwo',
            },
        ),
    ]
