#Elect Database

db.define_table('department',
                Field('name'),
                Field('level_up','reference department',
                requires=IS_IN_DB(db,'department.id','%(name)s'),
                format='%(name)s'),
                Field('notes'),
                auth.signature,format='%(name)s')


db.define_table('box',
                Field('dep_id','reference department'),
                Field('total','integer'),
                Field('box_date','date'),
                Field('notes'),
                auth.signature)

db.define_table('person',
                Field('name'),
                Field('notes'),
                auth.signature,format='%(name)s')

db.define_table('elect_inf',
                Field('person_id','reference person'),
                Field('elect_code'),
                Field('elect_date','date'),
                Field('elect_status'),
                Field('notes'),
                auth.signature)

db.define_table('elect_number',
                Field('dep_id','reference department',label='اللجنة',
                        requires=IS_IN_DB(db,db.department.id,'%(name)s')
                        
                        ),
                Field('person_id','reference person',label='المرشح',
                        requires=IS_IN_DB(db,db.person.id,'%(name)s')

                    ),
                Field('elector','integer' ,label='الرقم او النسبة'),
                Field('precentage','boolean',label='الرقم هو نسبة'),
                Field('box',requires = IS_INT_IN_RANGE(0, 10,error_message='too small or too large!'),
                label='رقم الصندوق'),
                Field('notes',label='ملاحظات'),
                auth.signature)


db.elect_number.dep_id.widget = SQLFORM.widgets.autocomplete(
request, db.department.name, limitby=(0,10), min_length=2,id_field=db.department.id)

db.elect_number.person_id.widget = SQLFORM.widgets.autocomplete(
request, db.person.name, limitby=(0,10), min_length=2,id_field=db.person.id)